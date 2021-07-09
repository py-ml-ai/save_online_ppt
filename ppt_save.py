import pyautogui
import keyboard
import time
import numpy as np
from PIL import Image
print("Hi folk, make a folder named 'pdf' in your D drive otherwise this will not work")
n = int(input("Enter the number of ScreenShots to be Taken"))
pdf_name = input("Enter pdf name")
print("Press the key S when you want to start capturing")
imlist = []
while True:
    if keyboard.read_key() == "s":
        for i in range(n):
            pyautogui.press("right")
            time.sleep(0.4)
            image = pyautogui.screenshot()
            image = np.array(image)
            im = Image.fromarray(image)
            imlist.append(im)
            print("You pressed Right")
        imlist[0].save("D:\pdf\\"+ str(pdf_name) + ".pdf",save_all=True, append_images=imlist[0:])
        break  

