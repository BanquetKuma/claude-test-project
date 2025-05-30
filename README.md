# Claude Test Project

## Tesla Stock Price Monitor

A real-time Streamlit application that displays Tesla (TSLA) stock price information with interactive charts and key financial metrics.

### Features

- 📈 Real-time Tesla stock price updates
- 📊 Intraday price movement charts
- 📈 30-day historical data with candlestick charts
- 💰 Key financial metrics (market cap, volume, statistics)
- 🔄 Auto-refresh every 30 seconds
- 📱 Responsive design

### Installation & Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To start the Streamlit app:

```bash
streamlit run tesla_stock_app.py
```

The app will open in your browser at `http://localhost:8501`

### Usage

- The app automatically refreshes every 30 seconds
- Use the "🔄 Refresh Now" button for manual updates
- Switch between "Today's Trading" and "30-Day History" tabs
- View additional information and settings in the sidebar

### Data Source

This application uses Yahoo Finance API through the `yfinance` library to fetch real-time and historical Tesla stock data.

**Disclaimer:** This data is for informational purposes only and should not be used for investment decisions.
