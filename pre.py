import yfinance as yf
import pandas as pd

# 指数代码 ^RUA
ticker = "^RUA"
start = "2015-01-01"
end = "2024-12-31"

# 下载数据
df = yf.download(ticker, start=start, end=end, auto_adjust=False)

# 保留并重命名列
df = df.reset_index()[['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

# 保存到 CSV
df.to_csv("russell_3000_2015_2024.csv", index=False)
print(df.head(), df.tail())