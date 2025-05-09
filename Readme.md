# 📈 yFinance API

A FastAPI-based RESTful API to fetch stock market data using the [yfinance](https://pypi.org/project/yfinance/) library. Supports detailed stock information, historical data, financials, holders, dividends, and more.

---

## 🚀 Getting Started

1. Install dependencies:
pip install fastapi uvicorn yfinance

## Run the API
uvicorn main:app --reload

##🔗 API Endpoints
Endpoint	Description

/	Health check: returns API status.

/stock/{ticker}/info	Returns stock info (company name, market cap, etc.).

/stock/{ticker}/history	Returns historical price data (customizable via period & interval).

/stock/{ticker}/balance-sheet	Returns balance sheet.

/stock/{ticker}/cashflow	Returns cash flow data.

/stock/{ticker}/financials	Returns income statement.

/stock/{ticker}/holders	Returns major and institutional holders.

/stock/{ticker}/recommendations	Returns analyst recommendations. 

/stock/{ticker}/dividends	Returns dividend history.

/stock/{ticker}/splits	Returns stock splits history.

/stock/{ticker}/sustainability	Returns ESG/sustainability data.

/stock/{ticker}/actions	Returns corporate actions like buybacks and dividends.

/stock/{ticker}/earnings	Returns earnings reports.


##📅 period and interval Guide

period – Time Span

Value	Meaning

1d	1 day

5d	5 days
1mo	1 month
3mo	3 months
6mo	6 months
1y	1 year
2y	2 years
5y	5 years
10y	10 years
ytd	Year to date
max	Maximum available

##interval – Data Frequency
Value	Meaning
1m	1 minute (7 days max)
2m	2 minutes
5m	5 minutes
15m	15 minutes
30m	30 minutes
60m	60 minutes
90m	90 minutes
1d	1 day
5d	5 days
1wk	1 week
1mo	1 month
3mo	3 months

⚠️ Not all combinations are valid. For example, interval=1m only works with period=7d or less.

##📌 Example Request

###Get 1-month daily history for TCS:
GET /stock/TCS.NS/history?period=1mo&interval=1d


##Get stock info for Reliance:
GET /stock/RELIANCE.NS/info


##🇮🇳 Indian Stock Support
###For Indian stocks:
Append .NS for NSE (e.g., TCS.NS, RELIANCE.NS)
Append .BO for BSE (e.g., TCS.BO)


