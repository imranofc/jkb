import time
import pyautogui
import random

time.sleep(5)  # 5 sec rukega, tab tak tu YT comment box me cursor le jaa

for i in range(1, 101):
    pyautogui.typewrite(str(random.randint(1, 90)))  # number type karega
    pyautogui.press("enter")     # enter press karega
    time.sleep(0.4)              # thoda delay, spam na lage