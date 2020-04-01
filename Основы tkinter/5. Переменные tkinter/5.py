from tkinter import *

root = Tk()

var0 = StringVar()
var1 = StringVar()
var2 = StringVar()

ch0 = Checkbutton(
    root, 
    text="Circle",
    variable=var0,
    onvalue="circle",
    offvalue="-"
)

ch1 = Checkbutton(
    root, 
    text="Square",
    variable=var1,
    onvalue="square",
    offvalue="-"
)

ch2 = Checkbutton(
    root, 
    text="Triangle",
    variable=var2,
    onvalue="triangle",
    offvalue="-"
)

lab = Label(
    root
)

def result( event ):
    v0 = var0.get()
    v1 = var1.get()
    v2 = var2.get()
    
    res = v0 + ' ' + v1 + ' ' + v2
    lab["text"] = res

but = Button(
    root,
    text="Получить значения"
)

but.bind("<Button-1>", result)

ch0.deselect()
ch1.deselect()
ch2.deselect()

ch0.pack()
ch1.pack()
ch2.pack()
but.pack()
lab.pack()

root.mainloop()

