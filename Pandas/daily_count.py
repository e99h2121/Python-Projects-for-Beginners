import pandas as pd
import sys

args = sys.argv
print(args)
print("第1引数：" + args[1])
print("第2引数：" + args[2])

#df = pd.read_csv('./files/data_count_.csv', header=0, parse_dates=['日時'])
#ret = df.groupby(df['更新日時'].dt.date).agg({'datacount':'count','datacount':'sum'})

# 引数:countbydate
def countbydate():
    df = pd.read_csv(args[1], header=0, parse_dates=['更新日時'])
    ret = df.groupby(df['更新日時'].dt.date).agg({'URL':'count'})
    ret.to_csv('output.csv', index=True, header=True)

# 引数:countbydateandver
def countbydateandver():
    df = pd.read_csv(args[1], header=0, parse_dates=['更新日'])
    ret = df.groupby(['バージョン','更新日']).agg({'URL':'count'})
    ret.to_csv('output.csv', index=True, header=True)

# 引数:countbypersonandver
def countbypersonandver():
    df = pd.read_csv(args[1], header=0, parse_dates=['更新日'])
    ret = df.groupby(['記入者', 'バージョン']).agg({'URL':'count'})
    ret.to_csv('output.csv', index=True, header=True)

# 引数:countbyversiont 
def countbyversion():
    df = pd.read_csv(args[1], header=0, parse_dates=['更新日'])
    ret = df.groupby(['バージョン']).agg({'URL':'count'})
    ret.to_csv('output.csv', index=True, header=True)


if (args[2] == "countbydate"):
    countbydate()
elif (args[2] == "countbydateandver"):
    countbydateandver()
elif (args[2] == "countbypersonandver"):
    countbypersonandver()
elif (args[2] == "countbyversion"):
    countbyversion()
