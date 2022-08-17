import tkinter
from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox
from personal_info import *
from books_searched import *
from book_requests import *

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
headingLabel = Label(headingFrame1, text= "COEP Library \n Member Page", bg = 'black', fg = 'white', font=("Arial",15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


btn1 = Button(root,text="Personal Information",bg='black', fg='white', command=personal_info)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Books Searched",bg='black', fg='white', command=books_searched)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="Book Requests",bg='black', fg='white', command=book_requests)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

root.mainloop()