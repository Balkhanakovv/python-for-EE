from tkinter import *

def color( event ):
    var = scale.get()

    if var == 1:
        frame.configure(bg="red")
    elif var == 2:
        frame.configure(bg="green")
    else:
        frame.configure(bg="blue")

root =Tk()

frame = Frame(
    root,
    width=250,
    height=250
)

var = IntVar()
scale = Scale(
    root,
    orient=HORIZONTAL,
    from_=1,
    to=3,
    tickinterval=1
)
scale.bind("<Button-1>", color)

frame.pack()
scale.pack()
root.mainloop()
