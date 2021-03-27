from __future__ import print_function

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
    status = '\n'.join(lines)
    return status

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
