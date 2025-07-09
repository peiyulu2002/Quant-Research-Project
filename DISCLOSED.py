#‘DIBS’, ’SCWO’,’AKA’,’AMTX’,’ATOS’,’BLNK’,’CBUS’,’NOTE’,QRHC’,’RDZN’,’STI’,’STHO’,’NOVA’,’TNYA’,’URG’
import yfinance as yf
import pandas as pd
import time

# 时间范围
start_date = "2015-01-01"
end_date = "2024-12-31"

# 你的 ticker 列表（去掉无效项 '--' 和重复的）
tickers = [
'DIBS', 'SCWO','AKA','AMTX','ATOS','BLNK','CBUS','NOTE','QRHC','RDZN','STI','STHO','NOVA','TNYA','URG'
]

# 下载每个 ticker 的数据
for ticker in tickers:
    try:
        print(f"正在下载 {ticker} 数据...")
        df = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False)
        if df.empty:
            print(f"警告：{ticker} 无数据，跳过。")
            continue
        df = df.reset_index()[['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
        df.to_csv(f"{ticker}_2015_2024.csv", index=False)
        time.sleep(1)  # 防止请求过快被封 IP
    except Exception as e:
        print(f"错误：无法下载 {ticker}，原因：{e}")
