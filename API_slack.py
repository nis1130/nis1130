#!/usr/bin/env python3
#-*- cording: utf-8 -*-

import requests
import monitoring

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-3458070245654-3488535597200-HRY7rvaCg3NarNMXMMGRLo18"
 
post_message(myToken,"#monitoring",monitoring.check('/var/log/syslog.1','Error'))

