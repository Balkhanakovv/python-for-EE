from tkinter import *

class butt_class:
    def __init__(self):
        self.but = Button(root, text="Print")
        self.but.bind("<Button-1>", self.func)
        self.but.pack()

    def func(self, event):
        print("Hello World!!!")

root = Tk()

but = butt_class()
root.mainloop()
