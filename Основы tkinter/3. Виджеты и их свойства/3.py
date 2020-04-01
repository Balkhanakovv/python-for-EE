from tkinter import *

root = Tk()

frame1 = Frame(
    root,
    bd=20,
    bg="lightgreen"
)

frame2 = Frame(
    root,
    bd=20,
    bg="green"
)


frame3 = Frame(
    root
)

ent = Entry(
    frame2,
    width=20
)

scale1 = Scale(
    frame1,
    orient=HORIZONTAL,
    length=300,
    from_=0,
    to=100,
    tickinterval=10,
    resolution=1
)

text = Text(
    frame3,
    width=36,
    height=3,
    font='14'
)

scr = Scrollbar(frame3, command=text.yview)
text.configure(yscrollcommand=scr.set)   
text.grid(row=0,column=0) 
scr.grid(row=0,column=1)

frame1.pack()
frame2.pack()
frame3.pack()
ent.pack()
scale1.pack()
root.mainloop() 