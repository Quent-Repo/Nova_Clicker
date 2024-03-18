import pyautogui
from tkinter import *
import keyboard
import time
print(pyautogui.size())
count = 0



app = Tk()
app.title("Nova clicker")
app.geometry("300x300")


def start(the_cli=50,the_int=.0001):
    while True:
        if keyboard.is_pressed("q"):
            pyautogui.click(clicks= the_cli, interval=the_int)
        if keyboard.is_pressed("w"):
            break




def go():
    arg= int(number_clicks_entry.get())
    arg2= float(number_interval_entry.get())
    start(arg,arg2)

#Number of click
number_clicks = Frame(app)
number_clicks.pack()
Label(number_clicks, text="Number of clicks").pack(side="left",padx=5)
number_clicks_entry = Entry(number_clicks)
number_clicks_entry.pack(side="right")



#interval time
number_interval = Frame(app)
number_interval.pack()
Label(number_interval, text="Time interval").pack(side="left",padx=5)
number_interval_entry = Entry(number_interval)
number_interval_entry.pack(side="right")

funer= Button(app, text="Start", command=go, width=10)
funer.pack()

app.mainloop()


'''
while True:
    if keyboard.is_pressed("q"):
        pyautogui.click(clicks= 50, interval=.0001)
        count+=1
    if keyboard.is_pressed("w"):
        break

print(count)
'''
