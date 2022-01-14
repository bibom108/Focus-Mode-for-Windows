import os
import time
from datetime import datetime
import psutil
from tkinter import *


def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


def kill_by_process_name_shell(name):
    for name in names:
        if checkIfProcessRunning(name) == True:
            os.system("taskkill /f /im " + name)


start_time = 300
end_time = 1140
names = ["Garena.exe", "steam.exe"]
while (1):
    now = datetime.now()
    current_time = int(now.strftime("%H")) * 60 + int(now.strftime("%M"))
    if current_time > start_time and current_time < end_time:
        kill_by_process_name_shell(names)
    else:
        break
    time.sleep(5)