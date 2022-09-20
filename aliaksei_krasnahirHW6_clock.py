import datetime
import time
import os


while True:
    current_sys_time = datetime.datetime.now().time()
    print("%s:%s:%s" % (current_sys_time.hour, current_sys_time.minute, current_sys_time.second))
    time.sleep(0.2)
    os.system('clear')