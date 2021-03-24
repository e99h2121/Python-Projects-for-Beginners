import random
import pandas as pd

ZUNDOKO_PATTERN = ['ズン', 'ズン', 'ズン', 'ズン', 'ドコ']

# ズンドコキヨシを実行し、ズンドコ回数を返却する関数
def do_zundoko():
    zundoko_list = []
    while zundoko_list[-5:] != ZUNDOKO_PATTERN:
        zundoko_list.append(random.choice(['ズン', 'ドコ']))
    return len(zundoko_list)

# 100万回実行してリストに格納
zundoko_len_list = []
for i in range(1, 1000001):
    zundoko_len_list.append(do_zundoko())

# 実行結果の統計量やヒストグラムを表示
df = pd.DataFrame(zundoko_len_list, columns=["zundoko length"])
print(df.describe())
print(df.hist(bins=50))
