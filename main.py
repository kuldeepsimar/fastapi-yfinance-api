from fastapi import FastAPI, Query
import yfinance as yf
import pandas as pd

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/fetch-ohlc")
def fetch_ohlc(
    ticker: str = Query(...),
    period: str = Query("1y"),
    interval: str = Query("1d")
):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)

    hist.reset_index(inplace=True)
    hist = hist[["Date", "Open", "High", "Low", "Close", "Volume"]]
    return hist.to_dict(orient="records")
