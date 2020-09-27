from tkinter import *

root = Tk()

mylabel = Label(root,text = "Hey there! How are you?").grid(row = 0, column = 1)
mylabel1 = Label(root,text = "I'm doing good too.").grid(row = 1, column = 1)
mylabel2 = Label(root, text = "Ankur").grid(row = 2, column = 2)


root.mainloop()