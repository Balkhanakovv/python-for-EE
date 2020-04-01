def but1_event(event):
    frame.configure(width=100, height=100)

def but2_event(event):
    frame.configure(width=200, height=200)

def but3_event(event):
    frame.configure(width=300, height=300)


from tkinter import *
root = Tk()

frame = Frame(
    root,
    bg="lightblue",
    width=100,
    height=100
)

but1 = Button(
    root,
    text="100x100"
)
but1.bind("<Button-1>", but1_event)

but2 = Button(
    root,
    text="200x200"
)
but2.bind("<Button-1>", but2_event)

but3 = Button(
    root,
    text="300x300"
)
but3.bind("<Button-1>", but3_event)

frame.pack()
but1.pack()
but2.pack()
but3.pack()
root.mainloop()