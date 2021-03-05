import random

max_num = 30

random_number = random.randint(1, max_num)
guess = 0
while guess != random_number:
    guess = int(input(f"1 から {max_num}: の間の数を当ててください！"))
    if guess < random_number:
        print("はずれ！ もっと大きい数です")
    elif guess > random_number:
        print("はずれ！ もっと小さい数です")
print(f"正解！答えは {random_number} でした")
