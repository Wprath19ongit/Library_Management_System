import tkinter
from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox
from viewbooks import *
from addbooks import *
from addmembers import *
from memberdetails import *

window = tkinter.Tk()
# to rename the title of the window
window.title("AdminPage")
root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")
same=True
n=0.25

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text= "COEP Library \n Admin Page", bg = 'black', fg = 'white', font=("Arial",15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


btn1 = Button(root,text="View Books List",bg='black', fg='white', command=viewbooks)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Add Books",bg='black', fg='white', command=addbooks)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="Add Members",bg='black', fg='white', command=addmembers)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="View Member Details",bg='black', fg='white', command = memberdetails)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
root.mainloop()