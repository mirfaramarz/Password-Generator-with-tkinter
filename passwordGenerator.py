from tkinter import *
import random , string


LETTERS = string.ascii_letters
NUMBERS = string.digits  
PUNCTUATION = string.punctuation  

chars = LETTERS + NUMBERS + PUNCTUATION

root = Tk()

root.geometry("200x200")
heading = Label(root, text="Password Generator").pack()
footer = Label(root, text="Coded by Faramarz").pack(side=BOTTOM)


pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()



pass_str = StringVar()

def passwordGenerator():
    password = ''
    for pwd in range(pass_len.get()):
        password +=  random.choice(chars)
    pass_str.set(password)


button = Button(root, text="Click", command=passwordGenerator).pack()
passwordField = Entry(root , textvariable = pass_str).pack()



root.mainloop()

