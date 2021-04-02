# TODO: https://python3.hateblo.jp/entry/2019/02/26/090618

# 入力: 金額、わる人数
import random

amount = input("金額: ")
ninzu = input("人数: ")

q, mod = divmod(int(amount), int(ninzu))
print(q, mod)
winner_amount = q+mod

mylist = list(range(int(ninzu)))
print(mylist)  # [0, 1, 2, 3, 4]

winner = random.choice(mylist)
print(winner)

print(f'winner will pay:{winner_amount}, other pay:{q}')
# 3 1
