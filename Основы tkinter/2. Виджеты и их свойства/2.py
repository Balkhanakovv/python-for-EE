from tkinter import *

root = Tk()

lab1 = Label(    
    root, 
    text="Ваш адрес:", 
    bg="yellow", 
    font="Arial 14"
)

ent = Entry(
    root,
    width=25,
    bd=3
)

lab2 = Label(
    root,
    text="Комментарий:",
    font="Arial 14"
)

tex = Text(
    root,
    width=30,
    height=10,
    bd=1
)

but = Button(
    root, 
    text="Отправить",
    font="Arial 14",
    bg="lightblue"
)

lab1.pack()
ent.pack()
lab2.pack()
tex.pack()
but.pack()
root.mainloop()