from tkinter import *

root = Tk()

lab1 = Label(
    root,
    text="Сколько штук?"
)

var=IntVar()
var.set(0)

rad0 = Radiobutton(
    root,
    text="0-10",
    variable=var,
    value=0
)

rad1 = Radiobutton(
    root,
    text="11-20",
    variable=var,
    value=1
)

rad2 = Radiobutton(
    root,
    text="21-30",
    variable=var,
    value=2
)

rad3 = Radiobutton(
    root,
    text="31-40",
    variable=var,
    value=3
)

lab2 = Label(
    root,
    text="Какого цвета?"
)

c0 = IntVar()
c1 = IntVar()
c2 = IntVar()
c3 = IntVar()

ch0 = Checkbutton(
    root,
    text="RED",
    bg="red",
    variable=c0,
    onvalue=1,
    offvalue=0
)

ch1 = Checkbutton(
    root,
    text="BLUE",
    bg="blue",
    variable=c1,
    onvalue=1,
    offvalue=0
)

ch2 = Checkbutton(
    root,
    text="GREEN",
    bg="green",
    variable=c2,
    onvalue=1,
    offvalue=0
)

ch3 = Checkbutton(
    root,
    text="YELLOW",
    bg="yellow",
    variable=c3,
    onvalue=1,
    offvalue=0
)

lab1.pack()
rad0.pack()
rad1.pack()
rad2.pack()
rad3.pack()
lab2.pack()
ch0.pack()
ch1.pack()
ch2.pack()
ch3.pack()
root.mainloop()