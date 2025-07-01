# src/fetch.py
import yfinance as yf
import pandas as pd

def get_history(ticker: str, start='2020-01-01', end=None) -> pd.DataFrame:
    """
    Download historical data for a ticker and cache to CSV.
    """
    df = yf.Ticker(ticker).history(start=start, end=end)
    df.to_csv(f"data/raw/{ticker}.csv")
    return df

if __name__ == '__main__':
    # Quick test
    df = get_history('AAPL', start='2021-01-01')
    print(df.tail())
