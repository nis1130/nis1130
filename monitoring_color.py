#!/usr/bin/env python3
#-*- cording: utf-8 -*-

from mylog import get_log_data
from time import sleep
import os
import sys
import datetime


def check(file_name, search_word):
    ret= ""
    if os.path.exists(file_name):
        ret = ret + "모니터링 시작 : " + file_name + "\n"
        ret = ret + "대상 : " + search_word + "\n"

    else:
        ret = ret + "찾으려는 파일이 없습니다. : " + file_name
    
    index = 0
    while os.path.exists(file_name):
        fp = open(file_name)
        file_data = fp.read()
        index = file_data.find(search_word, index)
        fp.close()

        if index >= 0:
            alert_msg=alert(search_word)
            (data, count) = get_log_data(file_data, search_word, index, 2, 2)
            ret += data
            ret += alert_msg
            return ret
            
        else:
            sys.stdout.write('...')
            sys.stdout.flush()

            index =len(file_data)
            sleep(5)
             
def alert(search_word):
    alert_text = ""
    now = datetime.datetime.now()
    if search_word == "Fail":
        alert_text =  '\n' + str(now) + " 심각한 문제가 발생했습니다."
    elif search_word == "exited":
        alert_text = '\n' + str(now) + " 문제가 발생했습니다."
    return alert_text

    
