def frame_size(event):
    frame.configure( width=entry1.get(), height=entry2.get())


from tkinter import *

root = Tk()

frame = Frame(
    root,
    bg="cyan",
    width=100,
    height=100
)
frame.pack()

entry1 = Entry(
    root,
    width=15
)
entry1.bind("<space>", frame_size)
entry1.pack()

entry2 = Entry(
    root,
    width=15
)
entry2.bind("<space>", frame_size)
entry2.pack()

root.mainloop()
