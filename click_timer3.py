import time
import datetime
import ctypes
import platform
from pynput.mouse import Button, Controller

mouse = Controller()

while True:
    try:
        seconds = input("Zadej (Datum je nepovinný) HH:MM:SS DD/MM/YYYY:\n")
        if len(seconds) == 8:
            obj = time.strptime(seconds, "%H:%M:%S")
            current_time = datetime.date.today()
            year = current_time.year
            mon = current_time.month
            day = current_time.day
        else:
            obj = time.strptime(seconds, "%H:%M:%S %d/%m/%Y")
            year = obj.tm_year
            mon = obj.tm_mon
            day = obj.tm_mday
        miliseconds = input("Zadej ms:")
        if miliseconds == "":
            miliseconds = 0
        else:
            miliseconds = int(miliseconds) * 1000
        epoch = datetime.datetime(year, mon, day, obj.tm_hour, obj.tm_min,
                                  obj.tm_sec, miliseconds).timestamp()
    except ValueError:
        print("Neplatný vstup!")
    else:
        break

while True:
    remain = epoch - time.time()
    if remain <= 4:
        print(f"Zbývájí méně než {'{:.0f}'.format(remain)} sekundy")
        break
    print(f"Zbývá {'{:.0f}'.format(remain)} sekund")
    time.sleep(1)
while time.time() < epoch:
    continue
# if platform.system() == "Windows":
#     ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # left down
#     ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # left up
# else:
mouse.click(Button.left, 1)
print("Kliknuto")
