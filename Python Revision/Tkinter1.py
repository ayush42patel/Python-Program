import tkinter as t
from tkinter import messagebox
from tkinter import *
# Making windows
root=t.Tk()

#changing title of window appearing
root.title("Hello Tkinter")

# Size of window (width , height)
root.geometry('300x200')

#Making Buttons
b=Button(root,text="Press Me!!")
b.pack()

# Making labels
# message=t.Label(text="Hello World!",foreground="white",background="black")
# message.pack()
root.mainloop()