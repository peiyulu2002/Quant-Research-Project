'''
import pandas as pd
df = pd.read_csv('./valid_270_tickers.csv')
print(df['Ticker'].tolist())


#'AAPL', 'MSFT', 'AMZN', 'JPM', 'JNJ', 'XOM', 'GOOG', 'GOOGL', 'BAC', 'V', 'UNH', 'PFE', 'T', 'CVX', 'HD', 'CSCO', 'WFC', 'VZ', 'INTC', 'PG', 'BA', 'MA', 'MRK', 'C', 'KO', 'DIS', 'NVDA', 'CMCSA', 'NFLX', 'PEP', 'ABBV', 'IBM', 'ORCL', 'WMT', 'AMGN', 'MDT', 'ADBE', 'PM', 'MCD', 'ABT', 'HON', 'MMM', 'UNP', 'MO', 'ACN', 'CRM', 'QCOM', 'AVGO', 'TXN', 'GE', 'NKE', 'COST', 'PYPL', 'LLY', 'BMY', 'GILD', 'TMO', 'BKNG', 'LOW', 'COP', 'CAT', 'LMT', 'SLB', 'USB', 'UPS', 'CVS', 'GS', 'NEE', 'AXP', 'EOG', 'SBUX', 'BDX', 'BIIB', 'TJX', 'DHR', 'ADP', 'ISRG', 'OXY', 'PNC', 'AMT', 'MDLZ', 'WBA', 'CB', 'CSX', 'SYK', 'SCHW', 'CME', 'FDX', 'BLK', 'CL', 'MS', 'DUK', 'CHTR', 'INTU', 'SPG', 'BSX', 'ILMN', 'GD', 'MU', 'NOC', 'NSC', 'DE', 'VLO', 'CI', 'SPGI', 'VRTX', 'EMR', 'FOXA', 'ITW', 'PSX', 'BK', 'AIG', 'TGT', 'HUM', 'D', 'COF', 'CTSH', 'CCI', 'ZTS', 'SO', 'GM', 'ICE', 'PRU', 'EXC', 'MMC', 'HPQ', 'PLD', 'PGR', 'TSLA', 'ECL', 'KMB', 'AMAT', 'MET', 'WM', 'BAX', 'ETN', 'HCA', 'AON', 'SPSC', 'FCPT', 'MRC', 'SHAK', 'UVV', 'AROC', 'LTC', 'FN', 'JELD', 'NWS', 'ATRA', 'FCF', 'AIR', 'UVE', 'PAG', 'EGBN', 'ADC', 'SYNA', 'FIBK', 'BJRI', 'WD', 'ODP', 'MTH', 'BHLB', 'BLDR', 'SRG', 'CVGW', 'SGMO', 'PRGS', 'PFS', 'HUBG', 'HTH', 'LPSN', 'NWBI', 'WABC', 'CFFN', 'NBTB', 'SPXC', 'UNFI', 'HLI', 'STBA', 'APAM', 'OXM', 'FSS', 'MATW', 'KN', 'EIG', 'LZB', 'AAT', 'MDGL', 'GME', 'CENTA', 'ALGT', 'GTN', 'NMIH', 'EDIT', 'BMI', 'EVTC', 'TTMI', 'CTRE', 'HL', 'FIZZ', 'ABG', 'SIR', 'CPK', 'NPO', 'IMAX', 'PRK', 'WSFS', 'SCS', 'WHD', 'KTOS', 'ALEX', 'CALM', 'DIOD', 'ROCK', 'CAL', 'BRKL', 'TBPH', 'AAON', 'PBYI', 'OSIS', 'ANF', 'GNL', 'HLX', 'USNA', 'ICFI', 'MEDP', 'RUN', 'MCY', 'INN', 'COLD', 'CROX', 'LCNB', 'NHTC', 'BBGI', 'HOV', 'MLP', 'NBN', 'PWOD', 'SGA', 'TLYS', 'INBK', 'HALL', 'SPWH', 'CLFD', 'WATT', 'IESC', 'WLFC', 'ACTG', 'CUE', 'KOPN', 'MRSN', 'GRBK', 'III', 'NDLS', 'GMRE', 'SGC', 'CHMG', 'ESSA', 'PLSE', 'FTK', 'LQDT', 'MCRB', 'VLGEA', 'ASC', 'ESCA', 'JILL', 'PVBC', 'RYI', 'NGVC', 'ALCO'

import yfinance as yf
import pandas as pd
import time

# 时间范围
start_date = "2015-01-01"
end_date = "2024-12-31"

# 你的 ticker 列表（去掉无效项 '--' 和重复的）
tickers = [
'AAPL', 'MSFT', 'AMZN', 'JPM', 'JNJ', 'XOM', 'GOOG', 'GOOGL', 'BAC', 'V', 'UNH', 'PFE', 'T', 'CVX', 'HD', 'CSCO', 'WFC', 'VZ', 'INTC', 'PG', 'BA', 'MA', 'MRK', 'C', 'KO', 'DIS', 'NVDA', 'CMCSA', 'NFLX', 'PEP', 'ABBV', 'IBM', 'ORCL', 'WMT', 'AMGN', 'MDT', 'ADBE', 'PM', 'MCD', 'ABT', 'HON', 'MMM', 'UNP', 'MO', 'ACN', 'CRM', 'QCOM', 'AVGO', 'TXN', 'GE', 'NKE', 'COST', 'PYPL', 'LLY', 'BMY', 'GILD', 'TMO', 'BKNG', 'LOW', 'COP', 'CAT', 'LMT', 'SLB', 'USB', 'UPS', 'CVS', 'GS', 'NEE', 'AXP', 'EOG', 'SBUX', 'BDX', 'BIIB', 'TJX', 'DHR', 'ADP', 'ISRG', 'OXY', 'PNC', 'AMT', 'MDLZ', 'WBA', 'CB', 'CSX', 'SYK', 'SCHW', 'CME', 'FDX', 'BLK', 'CL', 'MS', 'DUK', 'CHTR', 'INTU', 'SPG', 'BSX', 'ILMN', 'GD', 'MU', 'NOC', 'NSC', 'DE', 'VLO', 'CI', 'SPGI', 'VRTX', 'EMR', 'FOXA', 'ITW', 'PSX', 'BK', 'AIG', 'TGT', 'HUM', 'D', 'COF', 'CTSH', 'CCI', 'ZTS', 'SO', 'GM', 'ICE', 'PRU', 'EXC', 'MMC', 'HPQ', 'PLD', 'PGR', 'TSLA', 'ECL', 'KMB', 'AMAT', 'MET', 'WM', 'BAX', 'ETN', 'HCA', 'AON', 'SPSC', 'FCPT', 'MRC', 'SHAK', 'UVV', 'AROC', 'LTC', 'FN', 'JELD', 'NWS', 'ATRA', 'FCF', 'AIR', 'UVE', 'PAG', 'EGBN', 'ADC', 'SYNA', 'FIBK', 'BJRI', 'WD', 'ODP', 'MTH', 'BHLB', 'BLDR', 'SRG', 'CVGW', 'SGMO', 'PRGS', 'PFS', 'HUBG', 'HTH', 'LPSN', 'NWBI', 'WABC', 'CFFN', 'NBTB', 'SPXC', 'UNFI', 'HLI', 'STBA', 'APAM', 'OXM', 'FSS', 'MATW', 'KN', 'EIG', 'LZB', 'AAT', 'MDGL', 'GME', 'CENTA', 'ALGT', 'GTN', 'NMIH', 'EDIT', 'BMI', 'EVTC', 'TTMI', 'CTRE', 'HL', 'FIZZ', 'ABG', 'SIR', 'CPK', 'NPO', 'IMAX', 'PRK', 'WSFS', 'SCS', 'WHD', 'KTOS', 'ALEX', 'CALM', 'DIOD', 'ROCK', 'CAL', 'BRKL', 'TBPH', 'AAON', 'PBYI', 'OSIS', 'ANF', 'GNL', 'HLX', 'USNA', 'ICFI', 'MEDP', 'RUN', 'MCY', 'INN', 'COLD', 'CROX', 'LCNB', 'NHTC', 'BBGI', 'HOV', 'MLP', 'NBN', 'PWOD', 'SGA', 'TLYS', 'INBK', 'HALL', 'SPWH', 'CLFD', 'WATT', 'IESC', 'WLFC', 'ACTG', 'CUE', 'KOPN', 'MRSN', 'GRBK', 'III', 'NDLS', 'GMRE', 'SGC', 'CHMG', 'ESSA', 'PLSE', 'FTK', 'LQDT', 'MCRB', 'VLGEA', 'ASC', 'ESCA', 'JILL', 'PVBC', 'RYI', 'NGVC', 'ALCO'
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

'''

import pandas as pd
import os

# Step 1: 加载 Sector 信息
fund_csv_path = './iShares-Russell-3000-ETF_fund.csv'
df_fund = pd.read_csv(fund_csv_path)

# 创建 {ticker: sector} 映射字典
sector_map = dict(zip(df_fund['Ticker'], df_fund['Sector']))

# Step 2: 批量重命名文件
csv_folder = '/Users/huangyuqi/Document/GitHub/Quant-Research-Project'  
files = os.listdir(csv_folder)

for file in files:
    if file.endswith('_2015_2024.csv'):
        ticker = file.split('_')[0]
        
        # 查找 sector
        sector = sector_map.get(ticker)
        if not sector:
            print(f"⚠️ 无 sector 信息：{ticker}")
            continue
        
        # 生成新文件名
        new_file_name = f"{sector}_{file}"
        
        # 执行重命名
        src_path = os.path.join(csv_folder, file)
        dst_path = os.path.join(csv_folder, new_file_name)
        os.rename(src_path, dst_path)
        print(f"✅ 重命名：{file} → {new_file_name}")
