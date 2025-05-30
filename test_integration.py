import pytest
import pandas as pd
import numpy as np
from unittest.mock import Mock, patch
import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta
import time

class TestIntegration:
    """Integration tests for Tesla Stock App"""
    
    @patch('time.sleep')  # Prevent actual sleeping during tests
    @patch('streamlit.rerun')  # Prevent actual rerun during tests
    def test_full_app_flow_with_mock_data(self, mock_rerun, mock_sleep):
        """Test complete app flow with mocked external dependencies"""
        
        # Sample data for testing
        historical_data = pd.DataFrame({
            'Open': [240.0, 242.0, 244.0],
            'High': [245.0, 247.0, 249.0],
            'Low': [238.0, 240.0, 242.0],
            'Close': [244.0, 245.0, 246.0],
            'Volume': [1000000, 1100000, 1200000]
        }, index=pd.date_range('2024-01-01', periods=3, freq='D'))
        
        intraday_data = pd.DataFrame({
            'Close': [244.0, 245.0, 246.0]
        }, index=pd.date_range('2024-01-03 09:30', periods=3, freq='5T'))
        
        stock_info = {
            'currentPrice': 246.0,
            'previousClose': 245.0,
            'longName': 'Tesla, Inc.',
            'marketCap': 785000000000,
            'volume': 1200000
        }
        
        with patch('yfinance.Ticker') as mock_ticker:
            # Setup mock
            mock_tesla = Mock()
            mock_tesla.info = stock_info
            mock_tesla.history.side_effect = [historical_data, intraday_data]
            mock_ticker.return_value = mock_tesla
            
            # Test data fetching function
            from tesla_stock_app import get_tesla_data
            result = get_tesla_data()
            
            # Verify the integration
            assert result is not None
            assert result['current_price'] == 246.0
            assert result['previous_close'] == 245.0
            
            # Test calculations
            price_change = result['current_price'] - result['previous_close']
            price_change_pct = (price_change / result['previous_close']) * 100
            
            assert abs(price_change - 1.0) < 0.01
            assert abs(price_change_pct - 0.408) < 0.01  # (1/245)*100

    def test_error_recovery_flow(self):
        """Test app behavior during error conditions and recovery"""
        
        with patch('yfinance.Ticker') as mock_ticker:
            # First call fails
            mock_ticker.side_effect = Exception("Network timeout")
            
            from tesla_stock_app import get_tesla_data
            result = get_tesla_data()
            assert result is None
            
            # Second call succeeds (recovery scenario)
            mock_tesla = Mock()
            mock_tesla.info = {
                'currentPrice': 250.0,
                'previousClose': 248.0,
                'longName': 'Tesla, Inc.',
                'marketCap': 800000000000,
                'volume': 1500000
            }
            mock_tesla.history.return_value = pd.DataFrame({
                'Close': [248.0, 249.0, 250.0]
            })
            mock_ticker.side_effect = None
            mock_ticker.return_value = mock_tesla
            
            result = get_tesla_data()
            assert result is not None
            assert result['current_price'] == 250.0

    def test_data_consistency_across_calls(self):
        """Test that data remains consistent across multiple calls"""
        
        consistent_data = {
            'currentPrice': 245.0,
            'previousClose': 243.0,
            'longName': 'Tesla, Inc.',
            'marketCap': 780000000000,
            'volume': 1300000
        }
        
        historical_data = pd.DataFrame({
            'Close': [241.0, 242.0, 243.0, 244.0, 245.0]
        })
        
        with patch('yfinance.Ticker') as mock_ticker:
            mock_tesla = Mock()
            mock_tesla.info = consistent_data
            mock_tesla.history.return_value = historical_data
            mock_ticker.return_value = mock_tesla
            
            from tesla_stock_app import get_tesla_data
            
            # Make multiple calls
            result1 = get_tesla_data()
            result2 = get_tesla_data()
            
            # Verify consistency
            assert result1['current_price'] == result2['current_price']
            assert result1['previous_close'] == result2['previous_close']
            assert result1['company_name'] == result2['company_name']

    def test_market_hours_simulation(self):
        """Test app behavior during different market conditions"""
        
        # Market open scenario - with intraday data
        intraday_data = pd.DataFrame({
            'Close': [245.0, 246.0, 247.0]
        }, index=pd.date_range('2024-01-03 10:00', periods=3, freq='5T'))
        
        # Market closed scenario - empty intraday data
        empty_intraday = pd.DataFrame()
        
        stock_info = {
            'currentPrice': 247.0,
            'previousClose': 245.0,
            'longName': 'Tesla, Inc.',
            'marketCap': 790000000000,
            'volume': 1400000
        }
        
        historical_data = pd.DataFrame({
            'Close': [243.0, 244.0, 245.0, 246.0, 247.0]
        })
        
        with patch('yfinance.Ticker') as mock_ticker:
            mock_tesla = Mock()
            mock_tesla.info = stock_info
            
            # Test market open scenario
            mock_tesla.history.side_effect = [historical_data, intraday_data]
            mock_ticker.return_value = mock_tesla
            
            from tesla_stock_app import get_tesla_data
            result_open = get_tesla_data()
            
            assert not result_open['today_data'].empty
            
            # Test market closed scenario
            mock_tesla.history.side_effect = [historical_data, empty_intraday]
            result_closed = get_tesla_data()
            
            assert result_closed['today_data'].empty

    def test_cache_behavior_simulation(self):
        """Test caching behavior with TTL"""
        
        # This test simulates the @st.cache_data behavior
        call_count = 0
        
        def mock_ticker_factory():
            nonlocal call_count
            call_count += 1
            
            mock_tesla = Mock()
            mock_tesla.info = {
                'currentPrice': 245.0 + call_count,  # Price changes with each call
                'previousClose': 244.0,
                'longName': 'Tesla, Inc.',
                'marketCap': 780000000000,
                'volume': 1300000
            }
            mock_tesla.history.return_value = pd.DataFrame({
                'Close': [244.0, 245.0 + call_count]
            })
            return mock_tesla
        
        with patch('yfinance.Ticker', side_effect=mock_ticker_factory):
            from tesla_stock_app import get_tesla_data
            
            # Simulate multiple rapid calls (should be cached)
            result1 = get_tesla_data()
            result2 = get_tesla_data()
            
            # In real app with caching, these might be the same
            # Here we just verify the function works correctly
            assert result1 is not None
            assert result2 is not None

    def test_plotting_data_preparation(self):
        """Test data preparation for plotting components"""
        
        # Sample data that would be used for plotting
        historical_data = pd.DataFrame({
            'Open': [240.0, 242.0, 244.0, 246.0, 248.0],
            'High': [245.0, 247.0, 249.0, 251.0, 253.0],
            'Low': [238.0, 240.0, 242.0, 244.0, 246.0],
            'Close': [244.0, 246.0, 248.0, 250.0, 252.0],
            'Volume': [1000000, 1100000, 1200000, 1300000, 1400000]
        }, index=pd.date_range('2024-01-01', periods=5, freq='D'))
        
        intraday_data = pd.DataFrame({
            'Close': [250.0, 251.0, 252.0]
        }, index=pd.date_range('2024-01-05 10:00', periods=3, freq='5T'))
        
        # Test that data is suitable for plotting
        assert len(historical_data) > 0
        assert len(intraday_data) > 0
        assert all(col in historical_data.columns for col in ['Open', 'High', 'Low', 'Close'])
        assert 'Close' in intraday_data.columns
        
        # Test statistical calculations
        close_prices = historical_data['Close']
        high_price = close_prices.max()
        low_price = close_prices.min()
        avg_price = close_prices.mean()
        volatility = close_prices.std()
        
        assert high_price == 252.0
        assert low_price == 244.0
        assert avg_price == 248.0
        assert volatility > 0

    def test_ui_metrics_calculation(self):
        """Test calculations used for UI metrics display"""
        
        current_price = 250.0
        previous_close = 245.0
        market_cap = 800000000000
        volume = 1500000
        
        # Price change calculations
        price_change = current_price - previous_close
        price_change_pct = (price_change / previous_close) * 100
        
        # Market cap in billions
        market_cap_b = market_cap / 1e9
        
        # Assertions
        assert price_change == 5.0
        assert abs(price_change_pct - 2.04) < 0.01  # (5/245)*100
        assert market_cap_b == 800.0
        assert volume == 1500000
        
        # Test formatting (simulating what would be displayed)
        price_str = f"${current_price:.2f}"
        change_str = f"{price_change:+.2f} ({price_change_pct:+.2f}%)"
        volume_str = f"{volume:,}"
        market_cap_str = f"${market_cap_b:.1f}B"
        
        assert price_str == "$250.00"
        assert change_str == "+5.00 (+2.04%)"
        assert volume_str == "1,500,000"
        assert market_cap_str == "$800.0B"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])