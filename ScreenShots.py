import pyautogui
import time

x=1

while x<4:
    pyautogui.screenshot("C:\\Users\\No Tocar!!\\Downloads\\image_" + str(x) + ".png")
    x+=1
    time.sleep(2)

