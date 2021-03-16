from pyshorteners import Shortener

# passing instance
s = Shortener()
# asking user for choice
choice = int(input("1 or 2 ? (短縮化したいときは 1、元に戻したいときは 2 を入力してください) :"))


# link shortener
def short():
    link = input("短縮化したいリンクを入力してください: ")
    shortened_link = s.tinyurl.short(link)
    print(" The Shortened Link is: " + shortened_link)


# link expander
def expand():
    link = input("元に戻したいリンクを入力してください: ")
    expanded_link = s.tinyurl.expand(link)
    print("The Expanded link is: " + expanded_link)


if choice == 1:
    short()
elif choice == 2:
    expand()
else:
    print("1 か 2 を入力してください")
