import time
from datetime import datetime

def nowFormattedDate():
    #  获取当前时间戳
    now = datetime.now()
    # 格式化为字符串
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time

def nowYear():
    now = datetime.now()
    formatted_time = now.strftime("%Y")
    return formatted_time
def nowMonth():
    now = datetime.now()
    formatted_time = now.strftime("%m")
    return formatted_time

def nowDay():
    now = datetime.now()
    formatted_time = now.strftime("%d")
    return formatted_time

def nowFormattedTime():
    return int(time.time())