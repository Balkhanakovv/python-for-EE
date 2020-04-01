from tkinter import * 

def colorR():
    frame.config(bg="Red")

def colorG():
    frame.config(bg="Green")

def colorB():
    frame.config(bg="Blue") 

def square():
    frame.config(height=500, width=500) 

def rectangle():
    frame.config(height=400, width=700)

root = Tk()   

m = Menu(root) 
root.config(menu=m)  

frame = Frame(root,
    width=300,
    height=100,
    bg="Black"
)
frame.pack()

colorMenu = Menu(m) 
m.add_cascade(label="Color", menu=colorMenu)
colorMenu.add_command(label="Red", command=colorR)
colorMenu.add_command(label="Green", command=colorG)
colorMenu.add_command(label="Blue", command=colorB)

sizeMenu = Menu(m) 
m.add_cascade(label="Size", menu=sizeMenu)
sizeMenu.add_command(label="500x500", command=square)
sizeMenu.add_command(label="700x400", command=rectangle)

root.mainloop()  