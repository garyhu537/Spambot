import time
import pyautogui
from random import randint, seed

def spamBot():
    time.sleep(3)
    text = open("Trashtalk.txt")
    lines = text.read().split('\n')
    length = len(lines)
    while True:
        randomNumber = randint(0, length-1)
        pyautogui.typewrite(lines[randomNumber])
        pyautogui.press('enter')

spamBot()