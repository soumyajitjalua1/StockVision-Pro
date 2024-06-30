# StockVision Pro

StockVision Pro is an interactive stock analysis application built with Streamlit, yfinance, and Plotly. It allows users to visualize stock price movements, analyze fundamental data, and stay updated with the latest news.

## Features

- **Stock Price Visualization**: Plot the adjusted close price of any stock along with Simple Moving Average (SMA) and Exponential Moving Average (EMA).
- **Pricing Data Analysis**: View daily percentage changes, annual return, standard deviation, and risk-adjusted return.
- **Fundamental Data**: Access balance sheets, income statements, and cash flow statements.
- **News Updates**: Get the latest news for the selected stock with sentiment analysis.
- **Data Download**: Download stock data as a CSV file.
- **Portfolio Management**: Add and track your portfolio performance.
- **Educational Resources**: Learn about various aspects of stock market analysis (under development).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/StockVisionPro.git


2. Change to the project directory:
   ```bash
   cd StockVisionPro

3. Install the required packages:
   ```bash
   pip install -r requirements.txt


## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py


2. Select Ticker:
   
   Enter the ticker symbol of the stock you want to analyze in the sidebar text input.
   Here some examples of the company's name and there tickers
   
   - Apple Inc. - AAPL
   - Microsoft Corporation - MSFT
   - Amazon.com Inc. - AMZN
   - Alphabet Inc. (Class A) - GOOGL
   - Alphabet Inc. (Class C) - GOOG
   - Facebook, Inc. (Meta Platforms, Inc.) - META
   - Tesla, Inc. - TSLA
   - Berkshire Hathaway Inc. (Class A) - BRK.A
   - Berkshire Hathaway Inc. (Class B) - BRK.B
   - NVIDIA Corporation - NVDA
   - Johnson & Johnson - JNJ
   - JPMorgan Chase & Co. - JPM
   - Visa Inc. - V
   - Procter & Gamble Co. - PG
   - UnitedHealth Group Incorporated - UNH
   - Walmart Inc. - WMT
   - Mastercard Incorporated - MA
   - Walt Disney Company - DIS
   - PayPal Holdings, Inc. - PYPL
   - Netflix, Inc. - NFLX
  
3. Select Date Range:
  - Choose the start date for your analysis using the start date selector.
  - Choose the end date for your analysis using the end date selector. 


## Technical Indicators
  ### Simple Moving Average (SMA):

  
  The Simple Moving Average (SMA) is a calculation that takes the arithmetic mean of a given set of prices over a specific number of days in the past. For example, a 20-day SMA is the average closing price over     the last 20 days. SMA is used to identify the trend direction and smooth out price data to help look at the big picture.

  ### Exponential Moving Average (EMA):


  The Exponential Moving Average (EMA) is similar to the SMA, but it gives more weight to the most recent prices, making it more responsive to new information. This means the EMA will react more quickly to price changes than the SMA. EMA is commonly used to identify trends more quickly.


  ### Additional Features:

  
  ### 1. Pricing Data Analysis:   
  View daily percentage changes, annual return, standard deviation, and risk-adjusted return.
  ### 2. Fundamental Data: 
  Access balance sheets, income statements, and cash flow statements using the Alpha Vantage API.
  ### 3. News Updates:
  Get the latest news for the selected stock with sentiment analysis provided by the StockNews API.
  ### 4. Portfolio Management:
  Add and track your portfolio performance.
  ### 5. Educational Resources:
  Learn about various aspects of stock market analysis. This section is under development and will include topics such as:
  - Introduction to Stock Market
  - Fundamental Analysis
  - Technical Analysis
  - Key Financial Ratios
  - Moving Averages (SMA and EMA)
  - Risk Management
  - Portfolio Diversification

## Screenshots

  1. [Stock Price Visualization](https://github.com/soumyajitjalua1/StockVision-Pro/blob/main/Plot.png)

  2. [Pricing Data Analysis](https://github.com/soumyajitjalua1/StockVision-Pro/blob/main/Pricing%20Movement.png)

  3. [Fundamental Data](https://github.com/soumyajitjalua1/StockVision-Pro/blob/main/Fundamental%20data.png)

  4. [News Updates](https://github.com/soumyajitjalua1/StockVision-Pro/blob/main/Top%2010%20News.png)
  5. [Landing Page]()

## Contributing

  Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## App Link 
      https://stockvision-pro-wribbfrzqct8tjwxpcn3nn.streamlit.app/


## License

  This project is licensed under the MIT License. See the [LICENSE](https://github.com/soumyajitjalua1/StockVision-Pro/blob/main/LICENSE) file for details.

## Acknowledgements

  - Streamlit
  - yfinance
  - Plotly
  - Alpha Vantage
  - StockNews API


