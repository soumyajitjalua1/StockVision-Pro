import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from alpha_vantage.fundamentaldata import FundamentalData
from stocknews import StockNews

# Set up Streamlit app
st.markdown("<h1 style='text-align: center;'>StockVision Pro</h1>", unsafe_allow_html=True)


# Sidebar inputs for ticker and date range
ticker = st.sidebar.text_input('Ticker', 'AAPL')
start_date = st.sidebar.date_input('Start date')
end_date = st.sidebar.date_input('End date')

# Ensure dates are in proper format
if isinstance(start_date, datetime):
    start_date = start_date.strftime('%Y-%m-%d')
if isinstance(end_date, datetime):
    end_date = end_date.strftime('%Y-%m-%d')

# Download data
try:
    data = yf.download(ticker, start=start_date, end=end_date)
    if data.empty:
        st.error("No data found for the given ticker and date range.")
    else:
        # Plotting adjusted close price
        fig = px.line(data, x=data.index, y=data['Adj Close'], title=ticker)
        fig.update_xaxes(title='Date')
        fig.update_yaxes(title='Adjusted Close Price')
        
        # Adding Moving Averages
        data['SMA'] = data['Adj Close'].rolling(window=20).mean()
        data['EMA'] = data['Adj Close'].ewm(span=20, adjust=False).mean()
        fig.add_scatter(x=data.index, y=data['SMA'], mode='lines', name='SMA')
        fig.add_scatter(x=data.index, y=data['EMA'], mode='lines', name='EMA')

        st.plotly_chart(fig)
except Exception as e:
    st.error(f"Error fetching data: {e}")

# Tabs for Pricing Data, Fundamental Data, and Top 10 News
pricing_data, fundamental_data, news = st.tabs(["Pricing Data", "Fundamental Data", "Top 10 News"])

# Pricing Data Tab
with pricing_data:
    st.header("Pricing Movement")
    if not data.empty:
        data2 = data.copy()
        data2['% Change'] = data['Adj Close'] / data['Adj Close'].shift(1) - 1
        data2.dropna(inplace=True)
        st.write(data2)
        annual_return = data2['% Change'].mean() * 252 * 100
        st.write("Annual Return is", annual_return, '%')
        stdev = np.std(data2['% Change']) * np.sqrt(252)
        st.write("Standard Deviation is", stdev * 100, '%')
        st.write('Risk Adj. Return is', annual_return / (stdev * 100))

# Fundamental Data Tab
with fundamental_data:
    key = 'PNUXIP0FNV1FZ2PF'
    fd = FundamentalData(key, output_format='pandas')
    st.subheader('Balance Sheet')
    try:
        balance_sheet = fd.get_balance_sheet_annual(ticker)[0]
        bs = balance_sheet.T[2:]
        bs.columns = list(balance_sheet.T.iloc[0])
        st.write(bs)
    except Exception as e:
        st.error(f"Error fetching balance sheet data: {e}")
    
    st.subheader('Income Statement')
    try:
        income_statement = fd.get_income_statement_annual(ticker)[0]
        is1 = income_statement.T[2:]
        is1.columns = list(income_statement.T.iloc[0])
        st.write(is1)
    except Exception as e:
        st.error(f"Error fetching income statement data: {e}")
    
    st.subheader('Cash Flow Statement')
    try:
        cash_flow = fd.get_cash_flow_annual(ticker)[0]
        cf = cash_flow.T[2:]
        cf.columns = list(cash_flow.T.iloc[0])
        st.write(cf)
    except Exception as e:
        st.error(f"Error fetching cash flow statement data: {e}")

# News Tab
with news:
    st.header(f'News of {ticker}')
    try:
        sn = StockNews(ticker, save_news=False)
        df_news = sn.read_rss()
        for i in range(10):
            st.subheader(f'News {i+1}')
            st.write(df_news['published'][i])
            st.write(df_news['title'][i])
            st.write(df_news['summary'][i])
            title_sentiment = df_news['sentiment_title'][i]
            st.write(f'Title Sentiment: {title_sentiment}')
            news_sentiment = df_news['sentiment_summary'][i]
            st.write(f'News Sentiment: {news_sentiment}')
    except Exception as e:
        st.error(f"Error fetching news data: {e}")

# Additional Features: Download Data
st.sidebar.subheader('Download Data')
if not data.empty:
    csv = data.to_csv().encode('utf-8')
    st.sidebar.download_button(
        label="Download data as CSV",
        data=csv,
        file_name=f'{ticker}_data.csv',
        mime='text/csv',
    )

# Portfolio Management Placeholder (can be expanded)
st.sidebar.subheader('Portfolio Management')
st.sidebar.write("Track your portfolio performance here. (Feature under development)")

# Educational Resources Placeholder (can be expanded)
st.sidebar.subheader('Educational Resources')
st.sidebar.write("Learn more about stock market analysis. (Feature under development)")
