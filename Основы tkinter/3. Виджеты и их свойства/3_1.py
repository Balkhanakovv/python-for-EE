from tkinter import *

root = Tk()

groupsRI = ['RI-87', 'RI-88', 'RI-89']
listbox = Listbox(
    root,
    selectmode=SINGLE,
    height=4,
    bd=30
)

for i in groupsRI:
    listbox.insert(END, i)

window1 = Toplevel(
    root,
    bg="lightblue"
)

window1.title("Окно 1")
window1.minsize(width=400, height=200)

button1 = Button(
    window1,
    text="Button 1",
    bd=3   
)

window2 = Toplevel(
    root,
    bg="pink"
)

window2.title("Окно 2")
window2.minsize(width=200, height=400)

entry2 = Entry(
    window2,
    bd=2,
    width=40
)

button2 = Button(
    window2,
    bd=3,
    text="Button 2"
)

listbox.pack()
button1.pack()
entry2.pack()
button2.pack()
root.mainloop()