# TODO: https://python3.hateblo.jp/entry/2019/02/26/090618

# 入力: 金額、わる人数
import math

amount = int(input("合計支払い金額: "))
ninzu = int(input("人数: "))
unit = int(input("単位（例:100円→100、1000円→1000 等）: "))

q = math.ceil(amount / ninzu / unit) * unit
amari = amount - q * (ninzu)
print(f'{unit} 円単位では、一人あたり{q} 円で、余りは {amari} 円です。')

# print(f'winner will pay:{winner_amount}, other pay:{q}')
# 3 1
