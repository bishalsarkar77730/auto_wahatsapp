# import pywhatkit as kit
# kit.sendwhatmsg("+916267512533", "I love studytonight.com!", 15, 25)
import pyautogui
import time
message = 5
while message > 0:
    time.sleep(4)
    pyautogui.typewrite("I miss You")
    time.sleep(2)
    pyautogui.press('enter')
    message = message -1
