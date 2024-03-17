import pyautogui
import tkinter
import keyboard
import time
print(pyautogui.size())
count = 0
while True:
    if keyboard.is_pressed("q"):
        pyautogui.click(clicks= 20, interval=.0001)
        count+=1
    if keyboard.is_pressed("w"):
        break

print(count)
