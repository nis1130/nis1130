#!/usr/bin/env python3
#-*- cording: utf-8 -*-

import requests
import monitoring_color

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-3458070245654-3488535597200-ssdwF1Y31ioTc1HmCwDBR71h"
 
post_message(myToken,"#monitoring",monitoring_color.check('/var/log/syslog.1','Fail'))

