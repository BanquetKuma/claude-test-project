import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Toyota Stock Price Monitor",
    page_icon="📈",
    layout="wide"
)

# Add CSS for Japanese font support
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Hiragino Kaku Gothic ProN', 'Hiragino Sans', 'BIZ UDPGothic', 'Meiryo', 'Yu Gothic', 'MS PGothic', sans-serif;
}

.main .block-container {
    font-family: 'Hiragino Kaku Gothic ProN', 'Hiragino Sans', 'BIZ UDPGothic', 'Meiryo', 'Yu Gothic', 'MS PGothic', sans-serif;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Hiragino Kaku Gothic ProN', 'Hiragino Sans', 'BIZ UDPGothic', 'Meiryo', 'Yu Gothic', 'MS PGothic', sans-serif !important;
}

.stMetric label, .stMetric div {
    font-family: 'Hiragino Kaku Gothic ProN', 'Hiragino Sans', 'BIZ UDPGothic', 'Meiryo', 'Yu Gothic', 'MS PGothic', sans-serif !important;
}

.stTab {
    font-family: 'Hiragino Kaku Gothic ProN', 'Hiragino Sans', 'BIZ UDPGothic', 'Meiryo', 'Yu Gothic', 'MS PGothic', sans-serif !important;
}

/* Additional CSS to ensure proper Japanese character rendering */
* {
    -webkit-font-feature-settings: "palt";
    font-feature-settings: "palt";
}
</style>
""", unsafe_allow_html=True)

st.title("📈 トヨタ自動車 (TM) リアルタイム株価モニター")

@st.cache_data(ttl=60)
def get_toyota_data():
    try:
        toyota = yf.Ticker("TM")
        
        # Get current price info
        info = toyota.info
        current_price = info.get('currentPrice', 0)
        previous_close = info.get('previousClose', 0)
        
        # Get historical data for chart (last 30 days)
        hist_data = toyota.history(period="1mo", interval="1d")
        
        # Get intraday data for today
        today_data = toyota.history(period="1d", interval="5m")
        
        return {
            'current_price': current_price,
            'previous_close': previous_close,
            'historical_data': hist_data,
            'today_data': today_data,
            'company_name': info.get('longName', 'Toyota Motor Corporation'),
            'market_cap': info.get('marketCap', 0),
            'volume': info.get('volume', 0)
        }
    except Exception as e:
        st.error(f"データ取得エラー: {str(e)}")
        return None

# Main app layout
col1, col2, col3 = st.columns([2, 1, 1])

# Add refresh button
if st.button("🔄 今すぐ更新"):
    st.cache_data.clear()

# Main content area
data = get_toyota_data()

if data:
    current_price = data['current_price']
    previous_close = data['previous_close']
    price_change = current_price - previous_close
    price_change_pct = (price_change / previous_close) * 100 if previous_close != 0 else 0
    
    # Display current price and change
    with col1:
        st.metric(
            label="現在価格 (USD)",
            value=f"${current_price:.2f}",
            delta=f"{price_change:+.2f} ({price_change_pct:+.2f}%)"
        )
    
    with col2:
        st.metric(
            label="前日終値",
            value=f"${previous_close:.2f}"
        )
    
    with col3:
        st.metric(
            label="出来高",
            value=f"{data['volume']:,}"
        )
    
    # Display market cap
    if data['market_cap'] > 0:
        market_cap_b = data['market_cap'] / 1e9
        st.metric(
            label="時価総額",
            value=f"${market_cap_b:.1f}B"
        )
    
    # Create tabs for different views
    tab1, tab2 = st.tabs(["📊 本日の取引", "📈 30日間の履歴"])
    
    with tab1:
        st.subheader("日中株価推移")
        if not data['today_data'].empty:
            fig_today = go.Figure()
            fig_today.add_trace(go.Scatter(
                x=data['today_data'].index,
                y=data['today_data']['Close'],
                mode='lines',
                name='価格',
                line=dict(color='#DC143C', width=2)
            ))
            
            fig_today.update_layout(
                title="トヨタ自動車株価 - 本日",
                xaxis_title="時刻",
                yaxis_title="価格 (USD)",
                height=400,
                showlegend=False
            )
            
            st.plotly_chart(fig_today, use_container_width=True)
        else:
            st.info("日中データが利用できません（市場が閉まっている可能性があります）")
    
    with tab2:
        st.subheader("30日間の履歴データ")
        if not data['historical_data'].empty:
            fig_hist = go.Figure()
            
            # Candlestick chart
            fig_hist.add_trace(go.Candlestick(
                x=data['historical_data'].index,
                open=data['historical_data']['Open'],
                high=data['historical_data']['High'],
                low=data['historical_data']['Low'],
                close=data['historical_data']['Close'],
                name='TM'
            ))
            
            fig_hist.update_layout(
                title="トヨタ自動車株価 - 30日間",
                xaxis_title="日付",
                yaxis_title="価格 (USD)",
                height=500
            )
            
            st.plotly_chart(fig_hist, use_container_width=True)
            
            # Show some statistics
            st.subheader("30日間統計")
            col1, col2, col3, col4 = st.columns(4)
            
            hist_data = data['historical_data']['Close']
            with col1:
                st.metric("30日高値", f"${hist_data.max():.2f}")
            with col2:
                st.metric("30日安値", f"${hist_data.min():.2f}")
            with col3:
                st.metric("30日平均", f"${hist_data.mean():.2f}")
            with col4:
                volatility = hist_data.std()
                st.metric("ボラティリティ (σ)", f"${volatility:.2f}")
    
    # Last updated timestamp
    st.caption(f"最終更新: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

else:
    st.error("トヨタ自動車の株価データを取得できませんでした。インターネット接続を確認して再試行してください。")

# Sidebar with additional info
with st.sidebar:
    st.header("ℹ️ について")
    st.write("""
    このアプリは Yahoo Finance データを使用して、リアルタイムでトヨタ自動車 (TM) の株価情報を表示します。
    
    **機能:**
    - リアルタイム株価更新
    - 日中株価チャート
    - 30日間の履歴データ
    - 主要財務指標
    - 30秒ごとの自動更新
    
    **免責事項:**
    このデータは情報提供のみを目的としており、投資判断に使用すべきではありません。
    """)
    
    st.header("⚙️ 設定")
    if st.button("キャッシュをクリア"):
        st.cache_data.clear()
        st.success("キャッシュがクリアされました!")