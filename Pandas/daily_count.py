import pandas as pd

df = pd.read_csv('./files/daily_count_.csv', header=0, parse_dates=['日時'])
ret = df.groupby(df['日時'].dt.date).agg({'datacount':'count','datacount':'sum'})
ret.to_csv('output.csv', index=True, header=True)
