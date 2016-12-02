import pandas as pd
csvfile = pd.read_csv('bts_all_stat.csv')
print(csvfile[0:2])