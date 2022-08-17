import tkinter
from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox
from login import *
from signup import *

window = tkinter.Tk()
# to rename the title of the window
window.title("COEP_Library")
root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")
same=True
n=0.25

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text= "Welcome to \n COEP Library", bg = 'black', fg = 'white', font=("Arial",15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

Label(login_screen, text="Username").pack()
username_login_entry = Entry(login_screen, textvariable="username")
username_login_entry.pack()
Label(login_screen, text="").pack()
Label(login_screen, text="Password").pack()
password__login_entry = Entry(login_screen, textvariable="password", show= '*')
password__login_entry.pack()
Label(login_screen, text="").pack()

btn1 = Button(root,text="Login Here",bg='black', fg='white', command=login)
btn1.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

btn2 = Button(root,text="Sign Up!",bg='black', fg='white', command = signup)
btn2.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
root.mainloop()