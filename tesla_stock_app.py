import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

st.set_page_config(
    page_title="Tesla Stock Price Monitor",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Tesla (TSLA) Real-time Stock Price Monitor")

@st.cache_data(ttl=60)
def get_tesla_data():
    try:
        tesla = yf.Ticker("TSLA")
        
        # Get current price info
        info = tesla.info
        current_price = info.get('currentPrice', 0)
        previous_close = info.get('previousClose', 0)
        
        # Get historical data for chart (last 30 days)
        hist_data = tesla.history(period="1mo", interval="1d")
        
        # Get intraday data for today
        today_data = tesla.history(period="1d", interval="5m")
        
        return {
            'current_price': current_price,
            'previous_close': previous_close,
            'historical_data': hist_data,
            'today_data': today_data,
            'company_name': info.get('longName', 'Tesla, Inc.'),
            'market_cap': info.get('marketCap', 0),
            'volume': info.get('volume', 0)
        }
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}")
        return None

# Main app layout
col1, col2, col3 = st.columns([2, 1, 1])

# Auto-refresh every 30 seconds
placeholder = st.empty()

# Add refresh button
if st.button("🔄 Refresh Now"):
    st.cache_data.clear()

# Create placeholder for dynamic content
with placeholder.container():
    data = get_tesla_data()
    
    if data:
        current_price = data['current_price']
        previous_close = data['previous_close']
        price_change = current_price - previous_close
        price_change_pct = (price_change / previous_close) * 100 if previous_close != 0 else 0
        
        # Display current price and change
        with col1:
            st.metric(
                label="Current Price (USD)",
                value=f"${current_price:.2f}",
                delta=f"{price_change:+.2f} ({price_change_pct:+.2f}%)"
            )
        
        with col2:
            st.metric(
                label="Previous Close",
                value=f"${previous_close:.2f}"
            )
        
        with col3:
            st.metric(
                label="Volume",
                value=f"{data['volume']:,}"
            )
        
        # Display market cap
        if data['market_cap'] > 0:
            market_cap_b = data['market_cap'] / 1e9
            st.metric(
                label="Market Cap",
                value=f"${market_cap_b:.1f}B"
            )
        
        # Create tabs for different views
        tab1, tab2 = st.tabs(["📊 Today's Trading", "📈 30-Day History"])
        
        with tab1:
            st.subheader("Intraday Price Movement")
            if not data['today_data'].empty:
                fig_today = go.Figure()
                fig_today.add_trace(go.Scatter(
                    x=data['today_data'].index,
                    y=data['today_data']['Close'],
                    mode='lines',
                    name='Price',
                    line=dict(color='#00D4AA', width=2)
                ))
                
                fig_today.update_layout(
                    title="Tesla Stock Price - Today",
                    xaxis_title="Time",
                    yaxis_title="Price (USD)",
                    height=400,
                    showlegend=False
                )
                
                st.plotly_chart(fig_today, use_container_width=True)
            else:
                st.info("No intraday data available (market may be closed)")
        
        with tab2:
            st.subheader("30-Day Historical Data")
            if not data['historical_data'].empty:
                fig_hist = go.Figure()
                
                # Candlestick chart
                fig_hist.add_trace(go.Candlestick(
                    x=data['historical_data'].index,
                    open=data['historical_data']['Open'],
                    high=data['historical_data']['High'],
                    low=data['historical_data']['Low'],
                    close=data['historical_data']['Close'],
                    name='TSLA'
                ))
                
                fig_hist.update_layout(
                    title="Tesla Stock Price - 30 Days",
                    xaxis_title="Date",
                    yaxis_title="Price (USD)",
                    height=500
                )
                
                st.plotly_chart(fig_hist, use_container_width=True)
                
                # Show some statistics
                st.subheader("30-Day Statistics")
                col1, col2, col3, col4 = st.columns(4)
                
                hist_data = data['historical_data']['Close']
                with col1:
                    st.metric("30-Day High", f"${hist_data.max():.2f}")
                with col2:
                    st.metric("30-Day Low", f"${hist_data.min():.2f}")
                with col3:
                    st.metric("30-Day Average", f"${hist_data.mean():.2f}")
                with col4:
                    volatility = hist_data.std()
                    st.metric("Volatility (σ)", f"${volatility:.2f}")
        
        # Last updated timestamp
        st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Auto-refresh every 30 seconds
        time.sleep(30)
        st.rerun()
    
    else:
        st.error("Unable to fetch Tesla stock data. Please check your internet connection and try again.")

# Sidebar with additional info
with st.sidebar:
    st.header("ℹ️ About")
    st.write("""
    This app displays real-time Tesla (TSLA) stock price information using Yahoo Finance data.
    
    **Features:**
    - Real-time price updates
    - Intraday price charts
    - 30-day historical data
    - Key financial metrics
    - Auto-refresh every 30 seconds
    
    **Disclaimer:**
    This data is for informational purposes only and should not be used for investment decisions.
    """)
    
    st.header("⚙️ Settings")
    if st.button("Clear Cache"):
        st.cache_data.clear()
        st.success("Cache cleared!")