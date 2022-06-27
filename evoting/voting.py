import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from PIL import ImageTk, Image
import os
root = Tk()
root.geometry("1450x800+0+0")
root.title("E-Voting")
bg_color = "#074463"
title = Label(root, text="E-Voting System", bd=12, relief=GROOVE, bg=bg_color, fg="white",
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
my_img = ImageTk.PhotoImage(file='C:\Users\Gayatri Kamtekar\PycharmProjects\evoting\p3.PNG')
l1 = Label(root,image=my_img )
l1.pack()
root.mainloop()
