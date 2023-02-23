import os
import pathlib
import datetime

def createLogs(logs):
    namelog = f"{datetime.date.today()}.log"
    exist = False
    os.system(f"echo \'[{datetime.date.today()}] {logs}\' >> logs/{namelog}")
    exist = True
    if pathlib.Path(f"logs/{namelog}").is_file():
        exist = True
    else:
        exist = False
        if exist == False:
            os.system(f"touch logs/{namelog}")