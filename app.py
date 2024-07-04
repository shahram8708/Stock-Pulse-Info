from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
import logging
from datetime import datetime

app = Flask(__name__, static_url_path='/static')
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']
    if search_query:
        stock_info = get_stock_info(search_query)
        if stock_info:
            return render_template('result.html', stock_info=stock_info)
        error_msg = "Failed to retrieve stock information. Please try again."
        return render_template('index.html', error=error_msg)
    else:
        error_msg = "Please enter a valid stock ticker symbol."
        return render_template('index.html', error=error_msg)

def get_stock_info(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        historical_data = stock.history(period="1y")
        
        historical_data = historical_data.reset_index()
        historical_data['Date'] = pd.to_datetime(historical_data['Date'], format='%Y-%m-%d')
        historical_data = historical_data.set_index('Date').to_dict(orient='index')
        
        financials = stock.financials.transpose()
        balance_sheet = stock.balance_sheet.transpose()
        analyst_data = stock.recommendations
        sector = info.get('sector', 'N/A')
        industry = info.get('industry', 'N/A')
        economic_indicators = {
            'interest_rate': info.get('interestRate', 'N/A'),
            'inflation_rate': info.get('inflationRate', 'N/A'),
            'employment_data': info.get('fullTimeEmployees', 'N/A')
        }
        fundamental_analysis = {
            'pe_ratio': info.get('trailingPE', 'N/A'),
            'peg_ratio': info.get('pegRatio', 'N/A'),
            'pb_ratio': info.get('priceToBook', 'N/A'),
            'roe': info.get('returnOnEquity', 'N/A'),
            'debt_to_equity': info.get('debtToEquity', 'N/A')
        }
        other_metrics = {
            'beta': info.get('beta', 'N/A')
        }
        
        if isinstance(analyst_data, pd.DataFrame):
            analyst_ratings = []
            for idx, row in analyst_data.iterrows():
                analyst_ratings.append({
                    'Date': idx.strftime('%Y-%m-%d') if hasattr(idx, 'strftime') else str(idx),
                    'To Grade': row.get('To Grade', 'N/A'),
                    'From Grade': row.get('From Grade', 'N/A'),
                    'Firm': row.get('Firm', 'N/A')
                })
        else:
            analyst_ratings = []
        
        stock_info = {
            'symbol': info.get('symbol', 'N/A'),
            'name': info.get('longName', 'N/A'),
            'sector': sector,
            'industry': industry,
            'price': info.get('regularMarketPreviousClose', 'N/A'),
            'open': info.get('open', 'N/A'),
            'high': info.get('dayHigh', 'N/A'),
            'low': info.get('dayLow', 'N/A'),
            'close': info.get('previousClose', 'N/A'),
            'volume': info.get('volume', 'N/A'),
            'average_volume': info.get('averageVolume', 'N/A'),
            'market_cap': info.get('marketCap', 'N/A'),
            'dividend_yield': info.get('dividendYield', 'N/A'),
            'dividend_rate': info.get('dividendRate', 'N/A'),
            'dividend_date': info.get('dividendDate', 'N/A'),
            'eps': info.get('trailingEps', 'N/A'),
            'pe_ratio': info.get('trailingPE', 'N/A'),
            'earnings_date': info.get('earningsDate', 'N/A'),
            '52_week_high': info.get('fiftyTwoWeekHigh', 'N/A'),
            '52_week_low': info.get('fiftyTwoWeekLow', 'N/A'),
            'website': info.get('website', 'N/A'),
            'historical_data': historical_data,
            'financial_statements': {
                'income_statement': financials['Total Revenue'].to_dict() if isinstance(financials, pd.DataFrame) and 'Total Revenue' in financials else {},
                'balance_sheet': balance_sheet['Total Assets'].to_dict() if isinstance(balance_sheet, pd.DataFrame) and 'Total Assets' in balance_sheet else {}
            },
            'analyst_ratings': analyst_ratings,
            'economic_indicators': economic_indicators,
            'fundamental_analysis': fundamental_analysis,
            'other_metrics': other_metrics
        }
        
        return stock_info
    except Exception as e:
        logging.error(f"Error retrieving stock info: {e}")
        return None

if __name__ == '__main__':
    app.run(debug=True)
