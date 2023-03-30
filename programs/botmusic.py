from fileinput import close
import os
import pyautogui
import webbrowser
import time
#print(pyautogui.size())
#pyautogui.moveTo(200, 200)
#print(pyautogui.position())
#pyautogui.click(144, 1397)
#pyautogui.typewrite("Instagram")
#pyautogui.press('enter')
destination = "H:\\My Drive\\new"
location = "C:\\Users\\Blaze Pro\\Documents\\notes\\download.txt"

def create():
    webbrowser.open_new_tab('https://free-mp3-download.net')
    time.sleep(3)
    pyautogui.click(510, 537)
    lines = songs()
    for i in lines:
        pyautogui.typewrite(i)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.click(x=2155, y=898)
        pyautogui.click(x=1825, y=894)
        time.sleep(15)
        pyautogui.scroll(-800)
        pyautogui.click(1020, 842, 1,3)
        pyautogui.click(1256, 993)
        time.sleep(20)
        for item in os.listdir(destination):
            while item.endswith('.opdownload'):
                print(item)
                time.sleep(1)
        pyautogui. hotkey('ctrl', 'w')
        webbrowser.open('https://free-mp3-download.net')
        time.sleep(3)
        pyautogui.click(510, 537)   
    print("I have done downloading all the files!!!")

def songs():
    with open(location) as fobj:
        data = fobj.read()
        lines = data.split("\n")
        #print(lines)
    return lines
    

create()