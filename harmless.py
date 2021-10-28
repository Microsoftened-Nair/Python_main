import os
from tkinter import *
import webbrowser
import time

def yes1():
    def yes2():
        new2 = Tk()
        label1 = Label(new2, text="You have made our earth proud")
        label1.pack()
        time.sleep(4)
        for i in range(3):
            label1.configure(text=range(4))
            time.sleep(1)
        os.system("shutdown /s /t 1")
        new2.mainloop()


    def no2():
        webbrowser.open("https://www.netflix.com/in/title/70281562#:~:text=2013%20%7C%2016%2B%20%7C%207%20Seasons,Goor%2CMichael%20Schur")
        time.sleep(3)
        for i in range(3):
            time.sleep(1)
        os.system("shutdown /s /t 1")

    new = Tk()
    label = Label(new, text="Do you watch Brooklyn 99 on Netflix?")
    label.pack()
    y = Button(new, text="Yes", command=yes2)
    y.pack()
    n = Button(new, text="No", command=no2)
    n.pack()
    new.mainloop()

def no1():
    new = Tk()
    label1 = Label(new, text="You should sometimes")
    label1.pack()
    time.sleep(3)
    for i in range(3):
        label.configure(text=range(4))
        time.sleep(1)
    os.system("shutdown /s /t 1")
    new.mainloop()


root = Tk()
label = Label(root, text="Do you watch Netflix?")
label.pack()
y = Button(text="Yes", command=yes1)
y.pack()
n = Button(text="No", command=no1)
n.pack()

root.mainloop()
