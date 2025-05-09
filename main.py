from fastapi import FastAPI, HTTPException
import yfinance as yf

app = FastAPI(title="yFinance API", version="1.0")

@app.get("/")
def root():
    return {"message": "yFinance API is running"}

@app.get("/stock/{ticker}/info")
def get_info(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        return stock.info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stock/{ticker}/history")
def get_history(ticker: str, period: str = "1mo", interval: str = "1d"):
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period=period, interval=interval)
        return df.reset_index().to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stock/{ticker}/balance-sheet")
def get_balance_sheet(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        return stock.balance_sheet.fillna(0).to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stock/{ticker}/cashflow")
def get_cashflow(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        return stock.cashflow.fillna(0).to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stock/{ticker}/financials")
def get_financials(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        return stock.financials.fillna(0).to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stock/{ticker}/holders")
def get_holders(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        return {
            "major_holders": stock.major_holders.to_dict(),
            "institutional_holders": stock.institutional_holders.to_dict() if stock.institutional_holders is not None else {}
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))