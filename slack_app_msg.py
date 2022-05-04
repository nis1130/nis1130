#!/usr/bin/env python3
#-*- cording: utf-8 -*-

from slacker import Slacker
from datetime import *
# slack = Slacker('xoxb-3458070245654-3450120866583-4IhiNBNobOmQe7d2tfHQ35NI') # myslackbot
# slack = Slacker('xoxb-3458070245654-3464737980787-DWxZXsEZw8SEDpUklDXLUaze') # moni-bot
# Send a message to #general channel
# slack.chat.post_message('#monitoring', 'Hello fellow slackers!')


import requests
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
 
myToken = 'xoxb-3458070245654-3488535597200-HRY7rvaCg3NarNMXMMGRLo18s'
def dbgout(message):
    """인자로 받은 문자열을 파이썬 셸과 슬랙으로 동시에 출력한다."""
    print(datetime.now().strftime('[%m/%d %H:%M:%S]'), message)
    strbuf = datetime.now().strftime('[%m/%d %H:%M:%S] ') + message
    post_message(myToken,"#monitoring", strbuf)