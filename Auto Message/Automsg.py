
import pyautogui as pt

import time

limit = input("Enter Limit")

i = 0
time.sleep(5)
while i<int(limit):
    pt.typewrite("hii copycat")
    time.sleep(0.5)
    pt.press("enter")
    i+=1