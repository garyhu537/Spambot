import random
import pyautogui
import pyperclip

def sendSpamBot():
    with open("cnp.txt","r",encoding='gbk') as fk:
        text = fk.read()
        cnm=text.split('\n')
        for i in range (0,50):
            j=random.randint(0,len(cnm)-1)
            pyperclip.copy(cnm[j])
            pyautogui.hotkey('ctrl','v')
            pyautogui.press('enter')

sendSpamBot()