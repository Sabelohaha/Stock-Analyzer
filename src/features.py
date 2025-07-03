"Reads csv and adds signals"

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics   import accuracy_score

def load_and_feature(csv_path):
    "Analysis"
    df = pd.read_csv(csv_path, parse_dates=["Date"], index_col="Date")
    # Ensure index is datetime, convert to UTC, then remove timezone
    df.index = pd.to_datetime(df.index, utc=True).tz_convert(None)
    # 1-day return
    df["Ret1"] = df["Close"].pct_change()
    # 20-day moving average
    df["MA20"] = df["Close"].rolling(20).mean()
    # 20-day volatility (annualized)
    df["Vol20"] = df["Ret1"].rolling(20).std() * (252**0.5)
    # Next-day target for classification
    df["Up"] = (df["Close"].shift(-1) > df["Close"]).astype(int)
    return df.dropna()

if __name__ == "__main__":
    df_feat = load_and_feature("AAPL.csv")
    print(df_feat.tail())

df2 = load_and_feature("AAPL.csv")
train = df2.loc["2010-01-01":"2021-12-31"]
test  = df2.loc["2022-01-01":"2022-07-01"]

X_train, y_train = train[["Ret1","MA20","Vol20"]], train["Up"]
X_test,  y_test  = test[["Ret1","MA20","Vol20"]],  test["Up"]


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

preds = model.predict(X_test)
print("AAPL test accuracy:", accuracy_score(y_test, preds))
