# Claude Test Project

## Stock Price Monitoring Applications

This repository contains real-time Streamlit applications for monitoring stock prices with interactive charts and key financial metrics.

### Tesla Stock Price Monitor

A real-time Streamlit application that displays Tesla (TSLA) stock price information with interactive charts and key financial metrics.

### Toyota Stock Price Monitor (トヨタ自動車株価モニター)

A real-time Streamlit application that displays Toyota Motor Corporation (TM) stock price information with Japanese localization and interactive charts.

### Features

**Tesla Stock App:**
- 📈 Real-time Tesla (TSLA) stock price updates
- 📊 Intraday price movement charts
- 📈 30-day historical data with candlestick charts
- 💰 Key financial metrics (market cap, volume, statistics)
- 🔄 Auto-refresh every 30 seconds
- 📱 Responsive design

**Toyota Stock App (トヨタ自動車アプリ):**
- 📈 Real-time Toyota Motor Corporation (TM) stock price updates
- 📊 Intraday price movement charts with Japanese localization
- 📈 30-day historical data with candlestick charts
- 💰 Key financial metrics (market cap, volume, statistics)
- 🔄 Auto-refresh every 30 seconds with Japanese UI
- 📱 Responsive design with Japanese text support

### Installation & Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Applications

To start the Tesla stock app:

```bash
streamlit run tesla_stock_app.py
```

To start the Toyota stock app:

```bash
streamlit run toyota_stock_app.py
```

The apps will open in your browser at `http://localhost:8501` (or next available port)

### Usage

**Tesla Stock App:**
- The app automatically refreshes every 30 seconds
- Use the "🔄 Refresh Now" button for manual updates
- Switch between "Today's Trading" and "30-Day History" tabs
- View additional information and settings in the sidebar

**Toyota Stock App:**
- 30秒ごとに自動更新されます (Auto-refreshes every 30 seconds)
- 手動更新には "🔄 今すぐ更新" ボタンを使用 (Use "🔄 今すぐ更新" button for manual updates)
- "本日の取引" と "30日間の履歴" タブを切り替え (Switch between "Today's Trading" and "30-Day History" tabs)
- サイドバーで追加情報と設定を確認 (View additional information and settings in the sidebar)

### Data Source

These applications use Yahoo Finance API through the `yfinance` library to fetch real-time and historical stock data for Tesla (TSLA) and Toyota Motor Corporation (TM).

**Disclaimer:** This data is for informational purposes only and should not be used for investment decisions.
**免責事項:** このデータは情報提供のみを目的としており、投資判断に使用すべきではありません。
