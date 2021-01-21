# import pywhatkit as kit
# kit.sendwhatmsg("+91***********", "I love you!", 15, 25)
import pyautogui
import time
message = 5
while message > 0:
    time.sleep(4)
    pyautogui.typewrite("I miss You")
    time.sleep(2)
    pyautogui.press('enter')
    message = message -1
