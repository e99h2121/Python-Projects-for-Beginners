# TODO: https://python3.hateblo.jp/entry/2019/02/26/090618

# 入力: 金額、わる人数
import math

amount = int(input("金額: "))
ninzu = int(input("人数: "))

q = math.ceil(amount / ninzu / 1000) * 1000
amari = amount - q * (ninzu)
print(f'1,000円単位では、一人あたり{q} 円で、余りは {amari} 円です。')

# print(f'winner will pay:{winner_amount}, other pay:{q}')
# 3 1
