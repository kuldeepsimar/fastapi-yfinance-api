from fastapi import FastAPI, HTTPException
import yfinance as yf
from typing import Optional, List, Dict, Any

app = FastAPI(title="yFinance API", version="1.0")

@app.get("/")
def root():
    return {"message": "yFinance API is running"}

# Get stock info such as market cap, PE ratio, etc.
@app.get("/stock/{ticker}/info")
def get_info(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        if not info:
            raise HTTPException(status_code=404, detail="Stock info not found")
        return info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get stock price history (default 1 month, 1-day intervals)
@app.get("/stock/{ticker}/history")
def get_history(
    ticker: str,
    period: str = "1mo",
    interval: str = "1d"
):
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period=period, interval=interval)
        if df.empty:
            raise HTTPException(status_code=404, detail="No history found")
        return df.reset_index().to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get the stock's balance sheet
@app.get("/stock/{ticker}/balance-sheet")
def get_balance_sheet(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        balance_sheet = stock.balance_sheet
        if balance_sheet.empty:
            raise HTTPException(status_code=404, detail="Balance sheet not available")
        return balance_sheet.fillna(0).to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get the stock's cash flow statement
@app.get("/stock/{ticker}/cashflow")
def get_cashflow(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        cashflow = stock.cashflow
        if cashflow.empty:
            raise HTTPException(status_code=404, detail="Cash flow statement not available")
        return cashflow.fillna(0).to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get the stock's financials (income statement)
@app.get("/stock/{ticker}/financials")
def get_financials(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        financials = stock.financials
        if financials.empty:
            raise HTTPException(status_code=404, detail="Financials not available")
        return financials.fillna(0).to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get the stock's major and institutional holders
@app.get("/stock/{ticker}/holders")
def get_holders(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        major_holders = stock.major_holders
        institutional_holders = stock.institutional_holders

        holders = {
            "major_holders": major_holders.to_dict() if not major_holders.empty else {},
            "institutional_holders": institutional_holders.to_dict() if institutional_holders is not None and not institutional_holders.empty else {}
        }
        return holders
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get stock recommendations (analyst recommendations)
@app.get("/stock/{ticker}/recommendations")
def get_recommendations(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        recommendations = stock.recommendations
        if recommendations.empty:
            raise HTTPException(status_code=404, detail="No recommendations found")
        return recommendations.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get stock's dividends
@app.get("/stock/{ticker}/dividends")
def get_dividends(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        dividends = stock.dividends
        if dividends.empty:
            raise HTTPException(status_code=404, detail="No dividend data available")
        return dividends.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get stock's splits (for stock split history)
@app.get("/stock/{ticker}/splits")
def get_splits(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        splits = stock.splits
        if splits.empty:
            raise HTTPException(status_code=404, detail="No stock split data available")
        return splits.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get stock's sustainability (ESG data)
@app.get("/stock/{ticker}/sustainability")
def get_sustainability(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        sustainability = stock.sustainability
        if sustainability.empty:
            raise HTTPException(status_code=404, detail="No sustainability data available")
        return sustainability.to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get stock's actions (corporate actions like buybacks)
@app.get("/stock/{ticker}/actions")
def get_actions(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        actions = stock.actions
        if actions.empty:
            raise HTTPException(status_code=404, detail="No actions data available")
        return actions.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get stock's earnings
@app.get("/stock/{ticker}/earnings")
def get_earnings(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        earnings = stock.earnings
        if earnings.empty:
            raise HTTPException(status_code=404, detail="No earnings data available")
        return earnings.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
