import time
from datetime import datetime
import pyautogui


class DateObject:

    def __init__(self):
        time_now = datetime.now()
        self.year = time_now.year
        self.month = time_now.month
        self.day = time_now.day


while True:
    try:
        final_time = DateObject()
        date = input("Input DD/MM/YYYY (Leave empty for today):")
        try:
            obj_date = time.strptime(date, "%d/%m/%Y")
            final_time.day = obj_date.tm_mday
            final_time.year = obj_date.tm_year
            final_time.month = obj_date.tm_mon
        except ValueError:
            print("Input invalid or empty, using today!")
        second = input("Input HH:MM:SS:")
        current_time = time.strptime(second, "%H:%M:%S")
        ms = input("Input ms (Leave empty for 0):")
        if ms == "":
            ms = 0
        ms = int(ms) * 1000
        if ms >= 1000000 or ms < 0:
            ms = 0
        result = datetime(final_time.year, final_time.month, final_time.day, current_time.tm_hour, current_time.tm_min,
                          current_time.tm_sec, ms)
        print(f"Clicking on {result.isoformat(' ')}")
        epoch = result.timestamp()
    except ValueError:
        print("Invalid input, try again!")
    else:
        break

while True:
    remain = epoch - time.time()
    if remain <= 4:
        print(f"Remains less than {round(remain, 2)} seconds!")
        break
    print(f"Until click currently remains less than {round(remain, 2)} seconds.")
    time.sleep(1)
while time.time() < epoch:
    continue
pyautogui.click()
