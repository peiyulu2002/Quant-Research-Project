'''
import pandas as pd

# russell 3000 抽取270个
df = pd.read_csv('./iShares-Russell-3000-ETF_fund.csv')
# 获取总行数
total_rows = len(df)

# 提取前、中、后各90行
start = df.head(90)
mid_start = total_rows // 2 - 45
middle = df.iloc[mid_start:mid_start + 90]
end = df.tail(90)

# 合并并提取 Ticker 列，转换为向量（列表）
combined = pd.concat([start, middle, end])
ticker_vector = combined['Ticker'].tolist()

# 输出向量
print(ticker_vector)

'''

'''
import pandas as pd

# 读取原始数据文件
df = pd.read_csv('./iShares-Russell-3000-ETF_fund.csv')

# 总行数
total_rows = len(df)

# 提取前90行
start = df.head(90)

# 提取中间90行
mid_start = total_rows // 2 - 45
middle = df.iloc[mid_start:mid_start + 90]

# 提取最后90行
end = df.tail(90)


# 合并前中后数据
combined = pd.concat([start, middle, end])

# 只保留 Ticker 和 Sector 列
result = combined[['Ticker', 'Sector']].reset_index(drop=True)

# 输出结果
print(result['Ticker'].tolist())
'''

import pandas as pd
import yfinance as yf
import re

# 读取数据
df = pd.read_csv('./iShares-Russell-3000-ETF_fund.csv')

# 过滤掉空值
df = df[df['Ticker'].notna()]

# 提取更多行：前/中/后各500行（多抓一点确保有效ticker足够）
rows_needed = 150
total_rows = len(df)
start = df.head(rows_needed)
mid_start = total_rows // 2 - rows_needed // 2
middle = df.iloc[mid_start:mid_start + rows_needed]
end = df.tail(rows_needed)

# 合并并保留 Ticker 和 Sector
combined = pd.concat([start, middle, end])[['Ticker', 'Sector']].copy()

# 清洗 Ticker：移除无效或格式错误的代码
def clean_ticker(ticker):
    if not isinstance(ticker, str):
        return None
    ticker = ticker.strip().upper()
    if ticker in ['--', 'N/A', '', None]:
        return None
    if not re.fullmatch(r'[A-Z0-9.-]+', ticker):
        return None
    return ticker

combined['Ticker'] = combined['Ticker'].apply(clean_ticker)
combined = combined[combined['Ticker'].notna()].drop_duplicates(subset='Ticker')

# 验证有效性：尝试下载近几年数据，过滤掉没数据的
valid_tickers = []
for idx, row in combined.iterrows():
    ticker = row['Ticker']
    try:
        hist = yf.download(ticker, start="2020-01-01", end="2020-01-07", progress=False)
        if not hist.empty:
            valid_tickers.append((ticker, row['Sector']))
    except Exception:
        continue
    if len(valid_tickers) >= 270:
        break

# 转换为 DataFrame
valid_df = pd.DataFrame(valid_tickers, columns=['Ticker', 'Sector'])

# 输出或保存
print(f"最终有效 ticker 数量：{len(valid_df)}")
print(valid_df)

# 保存
valid_df.to_csv("valid_270_tickers.csv", index=False)


#头中尾各90 tickers
#'AAPL', 'MSFT', 'AMZN', 'BRKB', 'JPM', 'FB', 'JNJ', 'XOM', 'GOOG', 'GOOGL', 'BAC', 'V', 'UNH', 'PFE', 'T', 'CVX', 'HD', 'CSCO', 'WFC', 'VZ', 'INTC', 'PG', 'BA', 'MA', 'MRK', 'C', 'KO', 'DIS', 'NVDA', 'CMCSA', 'NFLX', 'PEP', 'DWDP', 'ABBV', 'IBM', 'ORCL', 'WMT', 'AMGN', 'MDT', 'ADBE', 'PM', 'MCD', 'ABT', 'HON', 'MMM', 'UNP', 'MO', 'ACN', 'CRM', 'QCOM', 'AVGO', 'TXN', 'GE', 'UTX', 'NKE', 'COST', 'PYPL', 'LLY', 'BMY', 'GILD', 'TMO', 'BKNG', 'LOW', 'COP', 'CAT', 'LMT', 'SLB', 'USB', 'UPS', 'CVS', 'GS', 'NEE', 'AXP', 'EOG', 'SBUX', 'ANTM', 'BDX', 'BIIB', 'TJX', 'DHR', 'ADP', 'AGN', 'AET', 'CELG', 'ISRG', 'OXY', 'PNC', 'AMT', 'ATVI', 'MDLZ', 'WD', 'RAVN', 'ODP', 'PTLA', 'SLCA', 'SEAS', 'MTH', 'BHLB', 'VRTU', 'BLDR', 'AYX', 'SRG', 'MTOR', 'CVGW', 'GHDX', 'SPN', 'SGMO', 'PRGS', 'AAWW', 'PFS', 'HUBG', 'HTH', 'LPSN', 'NWBI', 'WABC', 'CFFN', 'NBTB', 'SPXC', 'UNFI', 'HLI', 'NVRO', 'STBA', 'APAM', 'IPHI', 'OXM', 'I', 'FSS', 'MATW', 'KN', 'NP', 'EIG', 'LZB', 'AKS', 'MSGN', 'AAT', 'HDP', 'IMPV', 'TSRO', 'HF', 'MDGL', 'GME', 'EVBG', 'CENTA', 'ECOL', 'MCRN', 'OCLR', 'SASR', 'UNT', 'ALGT', 'GTN', 'CWEN US', 'NMIH', 'EDIT', 'CBPX', 'BMI', 'CORE', 'EVTC', 'TTMI', 'CTRE', 'MDC', 'HL', 'FIZZ', 'ABG', 'SIR', 'CPK', 'NPO', 'IMAX', 'PRK', 'WSFS', 'SCS', 'WHD', 'KTOS', 'SYNT', 'ALEX', 'CJ', 'HOME', 'KRA', 'TIVO', 'CALM', 'DIOD', 'ASC', 'AKAO', 'CTIC', 'ESCA', 'JILL', 'LCI', 'IDRA', 'PVBC', 'RYI', 'ICBK', 'JNCE', 'NGVC', 'ALCO', 'MPX', 'OCUL', 'VERI', 'HMTV', 'MXWL', 'OVID', 'TLGT', 'OSG', 'ARDX', 'CSLT', 'INNT', 'VSLR', 'ZN', 'DRRX', 'LIVX', 'DGICA', 'USLM', 'AE', 'GCBC', 'ISRL', 'PZN', 'REPH', 'NATR', 'SAMG', 'BGFV', 'IMH', 'KALA', 'GENC', 'MNLO', 'PCYG', 'SCPH', 'LCUT', 'BH A', 'GWRS', 'TTPH', 'AMBR', 'SCWX', 'AMPE', 'EPE', 'CLPR', 'SND', 'GEN', 'NWHM', '--', 'NWY', 'KODK', 'CSTR', 'IMDZ', 'NLNK', 'METC', 'SPKE', 'FBIO', 'MJCO', 'NL', 'VHI', 'AAC', 'HIVE', 'GFN', 'MLNT', 'SNDX', 'BW', 'FLNT', 'ASNS', 'CRVS', 'VALU', 'NYNY', 'GRIF', 'GTXI', 'CIX', 'TZOO', 'VTL', 'SHLD', 'NH', '--', 'RTYZ8', 'ESZ8', 'P5N994'

#suspended 列表抽取15个

#Suspension tickers 15
#AITR,GMFI,AIMAU,AQU,BNIX,DECA,IVCA,LDTC,MSSA,PLMJ,STAF,VMCA,WINV,ZAPP,NCNC

#disclosed
#‘DIBS’, ’SCWO’,’AKA’,’AMTX’,’ATOS’,’BLNK’,’CBUS’,’NOTE’,QRHC’,’RDZN’,’STI’,’STHO’,’NOVA’,’TNYA’,’URG’