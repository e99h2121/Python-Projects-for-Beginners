# https://betterprogramming.pub/10-useful-python-snippets-to-code-like-a-pro-e3d9a34e6145

# Swap Two Variables With One Line of Code
a = 1
b = 2
a, b = b, a

print(a, b);
# 2, 1


# Duplicate Strings Without Looping
name = "Banana"
print(name * 4)
# BananaBananaBananaBanana



# Reverse a String
sentence = "This is just a test"
reversed = sentence[::-1]
print(reversed)
# tset a tsuj si sihT


# Reverse a String
sentence = "やらと"
reversed = sentence[::-1]
print(reversed)
# とらや


# Squash a List of Strings Into One String
words = ["This", "is", "a", "Test"]
combined = " ".join(words)
print(combined)
# This is a Test


# Comparison Chains
# In Python, you can combine comparisons neatly together instead of splitting the statement into two or more parts. For example:
x = 100
y = 10000
res = 0 < x < 1000
print(res)
# True
res = 0 < y < 1000
print(res)
# False


# Find the Most Frequent Element in a List
test = [6, 2, 2, 3, 4, 2, 2, 90, 2, 41]
most_frequent = max(set(test), key = test.count)
print(most_frequent)
# 2 


# Unpack List to Separate Variables
arr = [1, 2, 3]
a,b,c = arr
print(a, b, c)
# 1 2 3



# One-Liner If-Else Statements
age = 30
age_group = "Adult" if age > 18 else "Child"
print(age_group)
# Adult


# Loop Through a List With One Line of Code
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)
# [1, 4, 9, 16, 25]


dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
squared_dict = {key: num * num for (key, num) in dict1.items()}
print(squared_dict)

