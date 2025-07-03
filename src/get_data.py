"Getting Data"

import yfinance as yf


def get_data (ticker, start, end, filename):
    "Function used to get stock data and put it in a nice little bow"
    df = yf.Ticker(ticker).history(start = start, end = end)
    df.to_csv(filename)
    return df

df_aapl = get_data("AAPL", "2010-1-1", "2025-07-01", "AAPL.csv")


