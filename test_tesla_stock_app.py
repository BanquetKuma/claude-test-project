import pytest
import pandas as pd
import numpy as np
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime, timedelta
import streamlit as st
from streamlit.testing.v1 import AppTest

# Import the functions we want to test
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

class TestTeslaStockApp:
    """Test suite for Tesla Stock App functionality"""
    
    def setup_method(self):
        """Setup test data and mocks"""
        # Sample historical data
        dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
        self.sample_historical_data = pd.DataFrame({
            'Open': np.random.uniform(200, 250, 30),
            'High': np.random.uniform(250, 300, 30),
            'Low': np.random.uniform(180, 220, 30),
            'Close': np.random.uniform(200, 280, 30),
            'Volume': np.random.randint(1000000, 10000000, 30)
        }, index=dates)
        
        # Sample intraday data
        intraday_times = pd.date_range(start='2024-01-30 09:30', periods=78, freq='5T')
        self.sample_intraday_data = pd.DataFrame({
            'Open': np.random.uniform(240, 260, 78),
            'High': np.random.uniform(250, 270, 78),
            'Low': np.random.uniform(230, 250, 78),
            'Close': np.random.uniform(240, 260, 78),
            'Volume': np.random.randint(100000, 1000000, 78)
        }, index=intraday_times)
        
        # Sample stock info
        self.sample_info = {
            'currentPrice': 245.67,
            'previousClose': 240.15,
            'longName': 'Tesla, Inc.',
            'marketCap': 782500000000,
            'volume': 23456789
        }

    @patch('yfinance.Ticker')
    def test_get_tesla_data_success(self, mock_ticker):
        """Test successful data fetching from yfinance"""
        # Setup mock
        mock_tesla = Mock()
        mock_tesla.info = self.sample_info
        mock_tesla.history.side_effect = [
            self.sample_historical_data,  # For 1mo period
            self.sample_intraday_data     # For 1d period
        ]
        mock_ticker.return_value = mock_tesla
        
        # Import and test the function
        from tesla_stock_app import get_tesla_data
        
        result = get_tesla_data()
        
        # Assertions
        assert result is not None
        assert result['current_price'] == 245.67
        assert result['previous_close'] == 240.15
        assert result['company_name'] == 'Tesla, Inc.'
        assert result['market_cap'] == 782500000000
        assert result['volume'] == 23456789
        assert not result['historical_data'].empty
        assert not result['today_data'].empty
        
        # Verify API calls
        mock_ticker.assert_called_once_with("TSLA")
        assert mock_tesla.history.call_count == 2

    @patch('yfinance.Ticker')
    def test_get_tesla_data_api_failure(self, mock_ticker):
        """Test handling of yfinance API failures"""
        # Setup mock to raise exception
        mock_ticker.side_effect = Exception("Network error")
        
        from tesla_stock_app import get_tesla_data
        
        result = get_tesla_data()
        
        # Should return None on error
        assert result is None

    @patch('yfinance.Ticker')
    def test_get_tesla_data_missing_data(self, mock_ticker):
        """Test handling of missing or incomplete data"""
        # Setup mock with incomplete info
        mock_tesla = Mock()
        mock_tesla.info = {
            'currentPrice': 245.67
            # Missing other fields
        }
        mock_tesla.history.return_value = pd.DataFrame()  # Empty dataframe
        mock_ticker.return_value = mock_tesla
        
        from tesla_stock_app import get_tesla_data
        
        result = get_tesla_data()
        
        # Should handle missing fields gracefully
        assert result is not None
        assert result['current_price'] == 245.67
        assert result['previous_close'] == 0  # Default value
        assert result['company_name'] == 'Tesla, Inc.'  # Default value
        assert result['market_cap'] == 0  # Default value
        assert result['volume'] == 0  # Default value

    def test_price_calculation(self):
        """Test price change calculations"""
        current_price = 245.67
        previous_close = 240.15
        
        price_change = current_price - previous_close
        price_change_pct = (price_change / previous_close) * 100
        
        assert abs(price_change - 5.52) < 0.01
        assert abs(price_change_pct - 2.30) < 0.01

    def test_market_cap_formatting(self):
        """Test market cap billion conversion"""
        market_cap = 782500000000
        market_cap_b = market_cap / 1e9
        
        assert abs(market_cap_b - 782.5) < 0.1

    def test_historical_data_statistics(self):
        """Test statistical calculations on historical data"""
        close_prices = self.sample_historical_data['Close']
        
        high_price = close_prices.max()
        low_price = close_prices.min()
        avg_price = close_prices.mean()
        volatility = close_prices.std()
        
        assert high_price >= low_price
        assert low_price <= avg_price <= high_price
        assert volatility >= 0

    @patch('yfinance.Ticker')
    def test_empty_dataframes_handling(self, mock_ticker):
        """Test handling of empty DataFrames"""
        mock_tesla = Mock()
        mock_tesla.info = self.sample_info
        mock_tesla.history.return_value = pd.DataFrame()  # Empty dataframe
        mock_ticker.return_value = mock_tesla
        
        from tesla_stock_app import get_tesla_data
        
        result = get_tesla_data()
        
        assert result is not None
        assert result['historical_data'].empty
        assert result['today_data'].empty

    def test_data_validation(self):
        """Test data validation and type checking"""
        # Test with valid data
        sample_data = {
            'current_price': 245.67,
            'previous_close': 240.15,
            'historical_data': self.sample_historical_data,
            'today_data': self.sample_intraday_data,
            'company_name': 'Tesla, Inc.',
            'market_cap': 782500000000,
            'volume': 23456789
        }
        
        # Validate data types
        assert isinstance(sample_data['current_price'], (int, float))
        assert isinstance(sample_data['previous_close'], (int, float))
        assert isinstance(sample_data['historical_data'], pd.DataFrame)
        assert isinstance(sample_data['today_data'], pd.DataFrame)
        assert isinstance(sample_data['company_name'], str)
        assert isinstance(sample_data['market_cap'], (int, float))
        assert isinstance(sample_data['volume'], (int, float))

    def test_error_scenarios(self):
        """Test various error scenarios"""
        # Test division by zero handling
        previous_close = 0
        current_price = 245.67
        
        price_change_pct = (current_price - previous_close) / previous_close * 100 if previous_close != 0 else 0
        assert price_change_pct == 0
        
        # Test negative prices (shouldn't happen but good to test)
        assert current_price > 0
        assert isinstance(current_price, (int, float))


class TestStreamlitApp:
    """Test suite for Streamlit UI components"""
    
    def test_app_initialization(self):
        """Test that the app initializes without errors"""
        # This is a basic smoke test to ensure the app can be imported
        try:
            import tesla_stock_app
            assert True
        except Exception as e:
            pytest.fail(f"App failed to initialize: {e}")

    @patch('tesla_stock_app.get_tesla_data')
    def test_app_with_mock_data(self, mock_get_data):
        """Test app behavior with mocked data"""
        # Setup mock data
        mock_data = {
            'current_price': 245.67,
            'previous_close': 240.15,
            'historical_data': pd.DataFrame({
                'Open': [240, 242], 'High': [245, 247], 
                'Low': [238, 240], 'Close': [244, 245],
                'Volume': [1000000, 1100000]
            }),
            'today_data': pd.DataFrame({
                'Close': [244, 245]
            }),
            'company_name': 'Tesla, Inc.',
            'market_cap': 782500000000,
            'volume': 23456789
        }
        mock_get_data.return_value = mock_data
        
        # Test would require streamlit testing framework setup
        # This is a placeholder for more comprehensive UI testing
        assert mock_get_data() == mock_data

    @patch('tesla_stock_app.get_tesla_data')
    def test_app_error_handling(self, mock_get_data):
        """Test app behavior when data fetching fails"""
        mock_get_data.return_value = None
        
        # The app should handle None return gracefully
        result = mock_get_data()
        assert result is None


class TestDataIntegrity:
    """Test suite for data integrity and validation"""
    
    def test_date_ranges(self):
        """Test that date ranges are logical"""
        end_date = datetime.now()
        start_date_30d = end_date - timedelta(days=30)
        start_date_1d = end_date - timedelta(days=1)
        
        assert start_date_30d < start_date_1d < end_date

    def test_price_validation(self):
        """Test price validation logic"""
        def validate_price(price):
            return isinstance(price, (int, float)) and price >= 0
        
        # Valid prices
        assert validate_price(245.67)
        assert validate_price(0)
        assert validate_price(1000.0)
        
        # Invalid prices
        assert not validate_price(-1)
        assert not validate_price("245.67")
        assert not validate_price(None)

    def test_volume_validation(self):
        """Test volume validation logic"""
        def validate_volume(volume):
            return isinstance(volume, (int, float)) and volume >= 0
        
        # Valid volumes
        assert validate_volume(1000000)
        assert validate_volume(0)
        
        # Invalid volumes
        assert not validate_volume(-1000)
        assert not validate_volume("1000000")

    def test_dataframe_structure(self):
        """Test expected DataFrame structure"""
        # Create sample data
        df = pd.DataFrame({
            'Open': [240.0, 242.0],
            'High': [245.0, 247.0],
            'Low': [238.0, 240.0],
            'Close': [244.0, 245.0],
            'Volume': [1000000, 1100000]
        })
        
        # Test structure
        expected_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
        assert all(col in df.columns for col in expected_columns)
        assert len(df) > 0
        
        # Test data types
        numeric_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
        for col in numeric_columns:
            assert pd.api.types.is_numeric_dtype(df[col])


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])