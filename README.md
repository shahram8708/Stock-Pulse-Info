# Stock Pulse Info

Stock Pulse Info is a web application built with Flask that provides real-time and historical information about stocks. Users can enter a stock ticker symbol to retrieve comprehensive data including current price, market cap, historical prices, financial statements, economic indicators, and fundamental analysis.

## Features

- **Real-time Stock Information**: Retrieve live data such as current price, open price, high/low prices, volume, market cap, dividend yield, and more.
- **Historical Data**: View historical prices and trading volumes over a specified period.
- **Financial Statements**: Access detailed financial statements including income statements and balance sheets.
- **Analyst Ratings**: Check recent analyst ratings and recommendations.
- **Economic Indicators**: Stay informed with key economic indicators like interest rates, inflation rates, and employment data.
- **Fundamental Analysis**: Evaluate fundamental metrics such as P/E ratio, PEG ratio, ROE, and debt-to-equity ratio.
- **Responsive Design**: User-friendly interface designed to work seamlessly across desktop and mobile devices.

## Usage

1. **Search**: Enter a stock ticker symbol in the search box and click "Get Info" to retrieve detailed information about the stock.
2. **Explore**: Navigate through tabs to explore different sections including historical data, financial statements, economic indicators, and fundamental analysis.
3. **Learn**: Gain insights into stock performance and make informed investment decisions.

## Installation

To run the application locally:

1. Clone this repository:
   ```
   git clone <https://github.com/shahram8708/Stock-Pulse-Info.git>
   cd stock-pulse-info
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your web browser and navigate to `http://localhost:5000` to access Stock Pulse Info.

## Technologies Used

- **Flask**: Web framework used for backend development.
- **HTML/CSS**: Frontend templates and styling.
- **Python**: Programming language for backend logic and data processing.
- **yfinance**: Python library for retrieving stock market data from Yahoo Finance.
- **Pandas**: Data manipulation and analysis tool for handling financial data.

## Contributing

Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss potential updates.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
