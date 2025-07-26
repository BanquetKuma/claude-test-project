import pytest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

@pytest.fixture
def sample_stock_info():
    """Fixture providing sample stock information"""
    return {
        'currentPrice': 245.67,
        'previousClose': 240.15,
        'longName': 'Tesla, Inc.',
        'marketCap': 782500000000,
        'volume': 23456789
    }

@pytest.fixture
def sample_historical_data():
    """Fixture providing sample historical stock data"""
    dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
    np.random.seed(42)  # For reproducible test data
    
    return pd.DataFrame({
        'Open': np.random.uniform(200, 250, 30),
        'High': np.random.uniform(250, 300, 30),
        'Low': np.random.uniform(180, 220, 30),
        'Close': np.random.uniform(200, 280, 30),
        'Volume': np.random.randint(1000000, 10000000, 30)
    }, index=dates)

@pytest.fixture
def sample_intraday_data():
    """Fixture providing sample intraday stock data"""
    times = pd.date_range(start='2024-01-30 09:30', periods=78, freq='5T')
    np.random.seed(42)  # For reproducible test data
    
    return pd.DataFrame({
        'Open': np.random.uniform(240, 260, 78),
        'High': np.random.uniform(250, 270, 78),
        'Low': np.random.uniform(230, 250, 78),
        'Close': np.random.uniform(240, 260, 78),
        'Volume': np.random.randint(100000, 1000000, 78)
    }, index=times)

@pytest.fixture
def complete_tesla_data(sample_stock_info, sample_historical_data, sample_intraday_data):
    """Fixture providing complete Tesla data structure"""
    return {
        'current_price': sample_stock_info['currentPrice'],
        'previous_close': sample_stock_info['previousClose'],
        'historical_data': sample_historical_data,
        'today_data': sample_intraday_data,
        'company_name': sample_stock_info['longName'],
        'market_cap': sample_stock_info['marketCap'],
        'volume': sample_stock_info['volume']
    }

@pytest.fixture
def empty_tesla_data():
    """Fixture providing empty Tesla data structure for error testing"""
    return {
        'current_price': 0,
        'previous_close': 0,
        'historical_data': pd.DataFrame(),
        'today_data': pd.DataFrame(),
        'company_name': 'Tesla, Inc.',
        'market_cap': 0,
        'volume': 0
    }

@pytest.fixture
def market_closed_data(sample_stock_info, sample_historical_data):
    """Fixture providing data when market is closed (no intraday data)"""
    return {
        'current_price': sample_stock_info['currentPrice'],
        'previous_close': sample_stock_info['previousClose'],
        'historical_data': sample_historical_data,
        'today_data': pd.DataFrame(),  # Empty for market closed
        'company_name': sample_stock_info['longName'],
        'market_cap': sample_stock_info['marketCap'],
        'volume': sample_stock_info['volume']
    }

@pytest.fixture(autouse=True)
def reset_streamlit_state():
    """Reset Streamlit state before each test"""
    # This fixture automatically runs before each test
    # In a real Streamlit testing environment, you might need to clear session state
    yield
    # Cleanup after test if needed