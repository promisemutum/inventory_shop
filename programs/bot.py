import pyautogui
import time
import webbrowser
import random
import string
#print(pyautogui.size())
#pyautogui.moveTo(200, 200)
#print(pyautogui.position())
#pyautogui.click(144, 1397)
#pyautogui.typewrite("Instagram")
#pyautogui.press('enter')
location = "C:\\Users\\Blaze Pro\\Documents\\notes\\mails.txt"
def create():
    webbrowser.open_new_tab('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
    time.sleep(3)
    result = random_string("First: ")
    pyautogui.typewrite(result)
    pyautogui.press('enter')
    result = random_string("Last: ")
    pyautogui.typewrite(result)
    pyautogui.press('enter')
    result = random_string("Mail: ")
    pyautogui.typewrite(result)
    pyautogui.press('enter')
    result = random_string("Password: ")
    pyautogui.typewrite(result)
    pyautogui.press('enter')
    pyautogui.typewrite(result)


def random_string(word):
    letters = string.ascii_lowercase
    result = ''.join(random.choice(letters) for i in range(8))
    result = result.capitalize()
    with open(location,'a') as file:
        file.write(word+str(result)+"\n")
    return result

create()