import pandas as pd
from pathlib import Path

# Define file paths for raw data
raw_data_2024_opp = Path('data/raw/24_25_NBA_opp.csv')
raw_data_2024_team = Path('data/raw/24_25_NBA_team.csv')
raw_data_2025_opp = Path('data/raw/25_26_NBA_opp.csv')
raw_data_2025_team = Path('data/raw/25_26_NBA_team.csv')

# Load datasets into DataFrames
df_24_opp = pd.read_csv(raw_data_2024_opp)
df_24_team = pd.read_csv(raw_data_2024_team)
df_25_opp = pd.read_csv(raw_data_2025_opp)
df_25_team = pd.read_csv(raw_data_2025_team)


#display the first few rows of each dataframe

print(df_24_opp.head())
print(df_24_team.head())
print(df_25_opp.head())
print(df_25_team.head())

#check the structure of the dataframe

""" df_24_opp.info()
df_24_team.info()
df_25_opp.info()
df_25_team.info() """