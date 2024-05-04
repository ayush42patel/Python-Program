from tkinter import *
import tkinter
#
r=tkinter.Tk()
r.title("Counting Seconds")
b=tkinter.Button(r,text="Stop", width=25, command=r.destroy,height=5,font=10,activebackground="red",activeforeground="blue")
b.pack()
r.mainloop()
#
master=Tk()
w=Canvas(master,width=20,height=60)
w.pack()
canvas_height=20
canvas_width=200
y=int(canvas_height/2)
w.create_line(0,y,canvas_width,y)
mainloop()
#
master = Tk()
var1 = IntVar()
Checkbutton(master, text='male',activebackground="Red",font=20,variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female',activebackground="Red",font=20,variable=var2).grid(row=1, sticky=W)
mainloop()
#
master = Tk()
Label(master,bd=20,bg="Red",highlightcolor="red",width=5,height=5,text='First Name').grid(row=0)
Label(master,bd=20,bg="Red",highlightcolor="red",width=5,height=5,text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()
#
root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
redbutton = Button(frame,text='Red',highlightcolor="red",width=10,height=5,fg ='red')
redbutton.pack( side = LEFT)
greenbutton = Button(frame,text='green',highlightcolor="green",width=10,height=5,fg='green')
greenbutton.pack( side = LEFT )
bluebutton = Button(frame,text='Blue',highlightcolor="blue",width=10,height=5,fg ='blue')
bluebutton.pack( side = LEFT )
blackbutton = Button(bottomframe, text ='Brown',highlightcolor="brown",width=10,height=5,fg ='brown')
blackbutton.pack( side = BOTTOM)
root.mainloop()
#
