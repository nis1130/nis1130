def printlog(logfile, search_word, pre_rowcount, next_rowcount):
    log_text = ''
    
    f= open(logfile)
    logdata=f.read()
    f.close()
    index = logdata.find(search_word)
    if index >= 0:
        (data, count)= get_log_data(logdata, search_word, index, pre_rowcount,next_rowcount)
        log_text += ("-"*70)+("\n"*2)+"log file : "+ logfile +"\n"
        log_text += "Find word : "+ search_word +("\n"*2)+("-"*70)
        log_text += logfile
        log_text += data
        log_text += "\n" + "추출한 로그 갯수 : " + str(count)
        
    else:
        log_text += +"검색한 로그가 없습니다."
    return log_text
        

def get_log_data(logdata, search_word,start_index, pre_rowcount, next_rowcount):
    count = 0
    ret = ''
    while start_index >= 0:
    
        enter_index = max(0,logdata.rfind("\n",0,start_index))

        for i in range(0,pre_rowcount):
            enter_index = max(0,logdata.rfind("\n",0,enter_index))
        enter_index2 = logdata.find("\n",start_index,len(logdata))
        for i in range(0,next_rowcount):
            next_end_index2=logdata.find("\n",enter_index2 + 1,len(logdata))
            if next_end_index2 == -1:
                next_end_index2= enter_index2
                break
            else: 
                enter_index2 = next_end_index2
        ret = ret+logdata[enter_index : enter_index2]
        ret = ret+"\n"+("-"*100)
        start_index = logdata.find(search_word, enter_index2 + 1)
        count += 1 
    
    return ret,count
