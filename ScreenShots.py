import pyautogui
import time
import os
import glob

name1="Error 1"
name2="Error 2"

def screenshot():
    time.sleep(5)
    pyautogui.screenshot("C:\\Users\\No Tocar!!\\Downloads\\Capturas\\" + str(name1) + ".png")
    time.sleep(5)
    pyautogui.screenshot("C:\\Users\\No Tocar!!\\Downloads\\Capturas\\" + str(name2) + ".png")

screenshot()

print("ver Archivos")
files = "C:\\Users\\No Tocar!!\\Downloads\\Capturas"
for the_file in os.listdir(files): 
    file_path = os.path.join(files, the_file)
    try: 
        if os.path.isfile(file_path): 
            print(file_path) 
    except Exception as e: 
        print (e)