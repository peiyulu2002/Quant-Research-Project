import os
import pandas as pd

# 获取当前脚本所在路径
base_dir = os.path.dirname(os.path.abspath(__file__))

# 文件路径
fund_csv_path = os.path.join(base_dir, 'iShares-Russell-3000-ETF_fund.csv')
csv_folder = base_dir  # 所有CSV都在这个目录

# 加载 fund 数据
df_fund = pd.read_csv(fund_csv_path)
sector_map = dict(zip(df_fund['Ticker'], df_fund['Sector']))

# 遍历重命名
for file in os.listdir(csv_folder):
    if file.endswith('_2015_2024.csv'):
        ticker = file.split('_')[0]
        sector = sector_map.get(ticker)
        if not sector:
            print(f"⚠️ 缺失 sector：{ticker}")
            continue
        new_name = f"{sector}_{file}"
        os.rename(os.path.join(csv_folder, file), os.path.join(csv_folder, new_name))
        print(f"✅ 重命名成功：{file} → {new_name}")
