import pyautogui
from tkinter import *
import keyboard
import time
print(pyautogui.size())
count = 0



app = Tk()
app.title("Nova clicker")
app.geometry("300x300")
app.maxsize(300,300)

def start(the_cli=50,the_int=.0001,tog="e",hld="q",en="w"):
    while True:
        if keyboard.is_pressed(hld):
            pyautogui.click(clicks= the_cli, interval=the_int)

        if keyboard.is_pressed(tog):
            while 1:
                pyautogui.click(clicks= the_cli, interval=the_int)
                print(On_Or_Off)


        if keyboard.is_pressed(en):
            break




def go():
    arg= int(number_clicks_entry.get())
    arg2= float(number_interval_entry.get())
    toggle = toggle_key_entry.get()
    hold = hold_key_entry.get()
    end = end_key_entry.get()
    start(arg,arg2,toggle,hold,end)

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


toggle_key = Frame(app)
toggle_key.pack()
Label(toggle_key , text="toggle").pack(side="left",padx=5)
toggle_key_entry = Entry(toggle_key)
toggle_key_entry.pack(side="right")



end_key = Frame(app)
end_key.pack()
Label(end_key , text="End").pack(side="left",padx=5)
end_key_entry = Entry(end_key)
end_key_entry.pack(side="right")


funer= Button(app, text="Start", command=go, width=10)
funer.pack()

hold_key = Frame(app)
hold_key.pack()
Label(hold_key, text="hold").pack(side="left",padx=5)
hold_key_entry = Entry(hold_key)
hold_key_entry.pack(side="right")

timer_key = Frame(app)
timer_key.pack()
Label(timer_key, text="Time").pack(side="right",padx=5)
timer_key_entry = Entry(timer_key)
timer_key_entry.pack(side="right")

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
