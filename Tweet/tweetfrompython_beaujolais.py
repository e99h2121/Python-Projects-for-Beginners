from __future__ import print_function

import random
import os
import tweepy

try:
    input = raw_input
except NameError:
    pass


def getStatus():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break

    word = '\n'.join(lines)
    
    l_phrase = []
    l_phrase.append(f"これまでで一番強くかつ攻撃的な{word}")
    l_phrase.append(f"ここ数年で一番出来が良い{word}")
    l_phrase.append(f"10年に1度の{word}")
    l_phrase.append(f"近年まれにみるワインの出来で過去10年間でトップクラスな{word}")
    l_phrase.append(f"10年に1度の{word}当たり年")
    l_phrase.append(f"1000年代最後の新酒ワインは近年にない{word}")
    l_phrase.append(f"今世紀最後の新酒ワインは色鮮やか、甘みがある{word}")
    l_phrase.append(f"ここ10年で最高の{word}")
    l_phrase.append(f"過去10年で最高と言われた01年を上回る{word}")
    l_phrase.append(f"1995年以来の{word}")
    l_phrase.append(f"100年に1度の出来、近年にない良い{word}")
    l_phrase.append(f"香りが強く中々の{word}")
    l_phrase.append(f"ここ数年で最高、タフな03年とはまた違い、本来の軽さを備え、これぞ{word}『ザ・ヌーボー』")
    l_phrase.append(f"今も語り継がれる76年や05年に近い{word}")
    l_phrase.append(f"柔らかく果実味が豊かで上質な{word}")
    l_phrase.append(f"豊かな果実味と程よい酸味が調和した{word}")
    l_phrase.append(f"過去最高と言われた05年に匹敵する50年に１度の{word}")
    l_phrase.append(f"2009年と同等の{word}")
    l_phrase.append(f"今年は天候が良かった為、昨年並みの仕上がり。爽やかでバランスが良い{word}")
    l_phrase.append(f"100年に1度の出来とされた03年を超す21世紀最高の{word}")
    l_phrase.append(f"出来が良く、豊満で絹のように滑らかな{word}")
    l_phrase.append(f"{word}史上最悪の不作")
    l_phrase.append(f"糖度と酸度のバランスが良く、軽やかでフルーティーな仕上がりの{word}")
    l_phrase.append(f"みずみずしさが感じられる素晴らしい品質の{word}")
    l_phrase.append(f"2009年の50年に一度のできを超える味わいの{word}")
    l_phrase.append(f"エレガントで味わい深く、とてもバランスがよい{word}")
    l_phrase.append(f"今世紀で最高の{word}")
    l_phrase.append(f"エレガントで酸味と果実味のバランスがとれた上品な{word}")
    l_phrase.append(f"豊満で朗らか、絹のようにしなやか。しかもフレッシュで輝かしい{word}")
    l_phrase.append(f"理想的な条件の元、素晴らしいヴィンテージへの期待高まる{word}")
    l_phrase.append(f"生産者のテクニックが重要な{word}")
    l_phrase.append(f"凝縮した果実味と上品な酸味が味わえる{word}")
    l_phrase.append(f"極めて早い成熟と乾燥した夏による、究極のミレジム（ヴィンテージ）{word}")

    phrase = random.choice(l_phrase)
    return phrase


def tweetthis(type):
    if type == "text":
        print("Enter your tweet " + user.name)
        tweet = getStatus()
        try:
            api.update_status(tweet)
        except Exception as e:
            print(e)
            return
    elif type == "pic":
        print("Enter pic path " + user.name)
        pic = os.path.abspath(input())
        print("Enter status " + user.name)
        title = getStatus()
        try:
            api.update_with_media(pic, status=title)
        except Exception as e:
            print(e)
            return

    print("\n\nDONE!!")

def initialize():
    global api, auth, user
    ck = "consumer key"  # consumer key
    cks = "consumer key secret"  # consumer key SECRET
    at = "access token"  # access token
    ats = "access token secret"  # access token SECRET

    auth = tweepy.OAuthHandler(ck, cks)
    auth.set_access_token(at, ats)

    api = tweepy.API(auth)
    user = api.me()


def main():
    doit = int(input("\n1. text\n2. picture\n"))
    initialize()
    if doit == 1:
        tweetthis("text")
    elif doit == 2:
        tweetthis("pic")
    else:
        print("OK, Let's try again!")
        main()

main()
