import requests
import json
import sys

WEB_HOOK_URL = "https://hooks.slack.com/zzzzzz"
args = sys.argv

try:
    message = args[1]
except: 
    message = input('message:')

requests.post(WEB_HOOK_URL, data=json.dumps({
    # メッセージ内容
    "text" : message
}))
