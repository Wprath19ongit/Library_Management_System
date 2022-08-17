import email
from unicodedata import name
from isbntools.app import *
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import sqlite3

# addbook(), addmem(), openviewmember(), openbookview(), opennewwindow()

from matplotlib.pyplot import show

conn = sqlite3.connect('library.db')
c = conn.cursor()

root = Tk()
root.geometry("600x500")

def addbook():
    def takeallinput():
        book = bookname.get("1.0", "end-1c")
        author_name = authorname.get("1.0", "end-1c")
        get_isbn = isbn_from_words(book)
        isbnno.insert(END,get_isbn)
        isbn_number = isbnno.get("1.0", "end-1c")
        print(get_isbn)
        c.execute("INSERT INTO books VALUES(?,?,?,?,?,?)",(book,author_name,"","",isbn_number,"Available"))
        messagebox.showinfo("Add Book", "Book added Successfully")
        newWindow.destroy()
        
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)
    titleFrame1 = Frame(newWindow,bg="#FFBB00",bd=5, height=50,width=100)
    titleFrame1.place(relx=0.2,rely=0.1,relwidth=0.6)
    titleLabel = Label(titleFrame1, text="Add Book", bg = 'black', fg = 'white', font=("Arial",15))
    titleLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    headFrame1 = Frame(newWindow,bd=1,width=100,height=25)
    headFrame1.place(relx=0.2,rely=0.3,relwidth=0.6)
    Frame2 = Frame(newWindow,bd=1, height=25,width=100)
    Frame2.place(relx=0.2,rely=0.4,relwidth=0.6)
    Frame3 = Frame(newWindow,bd=1,width=100, height=30)
    Frame3.place(relx=0.2,rely=0.5,relwidth=0.6)
    Frame4 = Frame(newWindow,bd=1, height=25)
    Frame4.place(relx=0.2,rely=0.6,relwidth=0.6)
    
    # sets the title of the
    # Toplevel widget
    newWindow.title("ADD BOOK")
 
    # sets the geometry of toplevel
    newWindow.geometry("500x500")
    newWindow.minsize(width=400,height=400)
    # A Label widget to show in toplevel
    NameLabel = Label(headFrame1, text="Bookname: ", fg = 'black', font=("Arial",15))
    
    bookname = Text(headFrame1, height = 2,
                width = 20,
                )
    bookname.place(relx=0,rely=0, relwidth=1, relheight=1)
    authorLabel = Label(Frame2, text="Author Name: ", fg = 'black', font=("Arial",15))
    
    authorname = Text(Frame2, height = 2,
                width = 20,
                )
    authorname.place(relx=0,rely=0, relwidth=1, relheight=1)

    isbn_num = Label(Frame3, text="ISBN Number: ", fg = 'black', font=("Arial",15))
    
    isbnno = Text(Frame3, height = 2,
                width = 20,
                )
    isbnno.place(relx=0,rely=0, relwidth=1, relheight=1)

    Butt = Button(Frame4, height = 2,
                 width = 20,
                 text ="Add",
                 command=takeallinput) ###add function
    Butt.place(relx=0,rely=0, relwidth=1, relheight=1)
    NameLabel.pack(side=LEFT)
    bookname.pack(side=RIGHT)
    authorLabel.pack(side=LEFT)
    authorname.pack(side=RIGHT)
    isbn_num.pack(side=LEFT)
    isbnno.pack(side=RIGHT)
    Butt.pack()
    
def addmem():
    def takeallinput():
        name = memname.get("1.0", "end-1c")
        lname = memlname.get("1.0", "end-1c")
        em = eaddress.get("1.0", "end-1c")
        miss = mis.get("1.0", "end-1c")
        bran = branch.get("1.0", "end-1c")
        c.execute("INSERT INTO client_info VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(miss,"1234",name,lname,miss,bran,em,"","","","","","",""))
        messagebox.showinfo("Add Member", "Member added Successfully \n Username: {} \n Password: {}".format(miss,"1234"))
        newWindow.destroy()            
             
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)
    titleFrame1 = Frame(newWindow,bg="#FFBB00",bd=5, height=50,width=100)
    titleFrame1.place(relx=0.2,rely=0.1,relwidth=0.6)
    titleLabel = Label(titleFrame1, text="Add Member", bg = 'black', fg = 'white', font=("Arial",15))
    titleLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    headFrame1 = Frame(newWindow,bd=1,width=100,height=25)
    headFrame1.place(relx=0.2,rely=0.3,relwidth=0.6)
    Frame2 = Frame(newWindow,bd=1, height=25,width=100)
    Frame2.place(relx=0.2,rely=0.4,relwidth=0.6)
    Frame3 = Frame(newWindow,bd=1,width=100, height=30)
    Frame3.place(relx=0.2,rely=0.5,relwidth=0.6)
    Frame4 = Frame(newWindow,bd=1, height=25)
    Frame4.place(relx=0.2,rely=0.6,relwidth=0.6)
    Frame5 = Frame(newWindow,bd=1, height=25)
    Frame5.place(relx=0.2,rely=0.7,relwidth=0.6)
    Frame6 = Frame(newWindow,bd=1, height=25)
    Frame6.place(relx=0.2,rely=0.8,relwidth=0.6)
    
    # sets the title of the
    # Toplevel widget
    newWindow.title("ADD MEMBER")
 
    # sets the geometry of toplevel
    newWindow.geometry("500x500")
    newWindow.minsize(width=400,height=400)
    # A Label widget to show in toplevel
    NameLabel = Label(headFrame1, text="First Name: ", fg = 'black', font=("Arial",15))
    
    memname = Text(headFrame1, height = 2,
                width = 20,
                )
    memname.place(relx=0,rely=0, relwidth=1, relheight=1)
    memllabel = Label(Frame2, text="Last Name: ", fg = 'black', font=("Arial",15))
    
    memlname = Text(Frame2, height = 2,
                width = 20,
                )
    memlname.place(relx=0,rely=0, relwidth=1, relheight=1)

    email = Label(Frame3, text="EMail: ", fg = 'black', font=("Arial",15))
    
    eaddress = Text(Frame3, height = 2,
                width = 20,
                )
    eaddress.place(relx=0,rely=0, relwidth=1, relheight=1)

    mis_no = Label(Frame4, text="MIS Number: ", fg = 'black', font=("Arial",15))
    
    mis = Text(Frame4, height = 2,
                width = 20,
                )
    mis.place(relx=0,rely=0, relwidth=1, relheight=1)

    branch_name = Label(Frame5, text="Branch: ", fg = 'black', font=("Arial",15))
    
    branch = Text(Frame5, height = 2,
                width = 20,
                )
    branch.place(relx=0,rely=0, relwidth=1, relheight=1)

    Butt = Button(Frame6, height = 2,
                 width = 20,
                 text ="Add",
                 command=takeallinput) ###add function
    Butt.place(relx=0,rely=0, relwidth=1, relheight=1)
    NameLabel.pack(side=LEFT)
    memname.pack(side=RIGHT)
    memllabel.pack(side=LEFT)
    memlname.pack(side=RIGHT)
    email.pack(side=LEFT)
    eaddress.pack(side=RIGHT)
    mis_no.pack(side=LEFT)
    mis.pack(side=RIGHT)
    branch_name.pack(side=LEFT)
    branch.pack(side=RIGHT)
    Butt.pack()





def openviewmember():
    def takeinput():
        INPUT = inputtxt.get("1.0", "end-1c")
        c.execute("SELECT EXISTS(SELECT 1 FROM client_info WHERE mis=? LIMIT 1)", (INPUT,))
        record = c.fetchone()
        if record[0] == 1:
            print("Name is in the table")
            c.execute("SELECT * FROM client_info WHERE mis=?",(INPUT,))
            entry = c.fetchone()
            NameLabel.config(text = entry[2])
            lNameLabel.config(text = entry[3])
            misLabel.config(text = entry[4])
            branchLabel.config(text = entry[5])

             
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)
    headFrame1 = Frame(newWindow,bd=5)
    headFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    Frame2 = Frame(newWindow,bd=5, bg="white" , height=100)
    Frame2.place(relx=0.2,rely=0.3,relwidth=0.6,relheight=0.6)
    # sets the title of the
    # Toplevel widget
    newWindow.title("MEMBER DETAILS")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
    newWindow.minsize(width=400,height=400)
    # A Label widget to show in toplevel
    inputtxt = Text(headFrame1, height = 2,
                width = 20,
                )
    inputtxt.place(relx=0,rely=0, relwidth=1, relheight=1)
    Display = Button(headFrame1, height = 2,
                 width = 5,
                 text ="View",
                 command=takeinput) ###add function
    Display.place(relx=0,rely=0, relwidth=1, relheight=1)
    NameLabel = Label(Frame2, text="", bg = 'white', fg = 'black', font=("Arial",15))
    NameLabel.place(relx=0.28,rely=0.3, relwidth=1, relheight=1)
    lNameLabel = Label(Frame2, text="", bg = 'white', fg = 'black', font=("Arial",15))
    lNameLabel.place(relx=0.28,rely=0.4, relwidth=1, relheight=1)
    misLabel = Label(Frame2, text="", bg = 'white', fg = 'black', font=("Arial",15))
    misLabel.place(relx=0.28,rely=0.5, relwidth=1, relheight=1)
    branchLabel = Label(Frame2, text="", bg = 'white', fg = 'black', font=("Arial",15))
    branchLabel.place(relx=0.28,rely=0.6, relwidth=1, relheight=1)
    inputtxt.pack(side=LEFT)
    Display.pack(side=RIGHT)
    NameLabel.pack()
    lNameLabel.pack()
    misLabel.pack()
    branchLabel.pack()

def openbookview():
    def show():
        bk = inputtxt2.get("1.0", "end-1c")
        bk = '%'+bk+'%'
        
        c.execute("SELECT rowid,* FROM books WHERE book_name LIKE ?",[bk])
        result1 = c.fetchall()
        c.execute("SELECT rowid,* FROM books WHERE author1 LIKE ?",[bk])
        result2 = c.fetchall()
        c.execute("SELECT rowid,* FROM books WHERE author2 LIKE ?",[bk])
        result3 = c.fetchall()
        c.execute("SELECT rowid,* FROM books WHERE author3 LIKE ?",[bk])
        result4 = c.fetchall()
        c.execute("SELECT rowid,* FROM books WHERE book_id LIKE ?",[bk])
        result5 = c.fetchall()
        result = result1+result2+result3+result4+result5
        result = set(result)
        if check[0] == 1:
            NameLabel.config(text = entry[1])
            authorNameLabel.config(text = entry[0])
            bookidLabel.config(text = entry[4])
            availLabel.config(text = entry[5])


             
    # Toplevel object which will
    # be treated as a new window
    newWindow2 = Toplevel(root)
    headFrame1 = Frame(newWindow2,bd=5)
    headFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    Frame2 = Frame(newWindow2,bd=5, bg="white" , height=100)
    Frame2.place(relx=0.2,rely=0.3,relwidth=0.6,relheight=0.6)
    # sets the title of the
    # Toplevel widget
    newWindow2.title("BOOK DETAILS")
 
    # sets the geometry of toplevel
    newWindow2.geometry("200x200")
    newWindow2.minsize(width=400,height=400)
    # A Label widget to show in toplevel
    inputtxt2 = Text(headFrame1, height = 2,
                width = 20,
                )
    inputtxt2.place(relx=0,rely=0, relwidth=1, relheight=1)
    Display = Button(headFrame1, height = 2,
                 width = 5,
                 text ="View",
                 command=show) ###add function
    Display.place(relx=0,rely=0, relwidth=1, relheight=1)
    NameLabel = Label(Frame2, text="", bg = 'white', fg = 'black', font=("Arial",15))
    NameLabel.place(relx=0.28,rely=0.3, relwidth=1, relheight=1)
    authorNameLabel = Label(Frame2, text="", bg = 'white', fg = 'black', font=("Arial",15))
    authorNameLabel.place(relx=0.28,rely=0.4, relwidth=1, relheight=1)
    bookidLabel = Label(Frame2, text="", bg = 'white', fg = 'black', font=("Arial",15))
    bookidLabel.place(relx=0.28,rely=0.5, relwidth=1, relheight=1)
    availLabel = Label(Frame2, text="", bg = 'white', fg = 'black', font=("Arial",15))
    availLabel.place(relx=0.28,rely=0.6, relwidth=1, relheight=1)
    inputtxt2.pack(side=LEFT)
    Display.pack(side=RIGHT)
    NameLabel.pack()
    authorNameLabel.pack()
    bookidLabel.pack()
    availLabel.pack()




def admin_options():

    root.title("Library")
    root.minsize(width=400,height=400)

    same=True
    n=0.25

# Adding a background image
#background_image =Image.open("lib.jpeg")
#[imageSizeWidth, imageSizeHeight] = background_image.size

#newImageSizeWidth = int(imageSizeWidth*n)
#if same:
 #   newImageSizeHeight = int(imageSizeHeight*n) 
#else:
#    newImageSizeHeight = int(imageSizeHeight/n) 
    
#background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
#img = Image.PhotoImage(background_image)
    Canvas1 = Canvas(root)
#Canvas1.create_image(300,340,image = img)      
#Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Admin Page", bg = 'black', fg = 'white', font=("Arial",15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    btn1 = Button(root,text="View Books List",bg='black', fg='white', command=openbookview) #add function
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Add Books",bg='black', fg='white', command=addbook)  #add function
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
    btn3 = Button(root,text="Add Members",bg='black', fg='white', command=addmem) #add function
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
    btn4 = Button(root,text="View Member Details",bg='black', fg='white', command=openviewmember) #add function
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    root.mainloop()

def client_options():

    root.title("Library")
    root.minsize(width=400,height=400)

    same=True
    n=0.25

# Adding a background image
#background_image =Image.open("lib.jpeg")
#[imageSizeWidth, imageSizeHeight] = background_image.size

#newImageSizeWidth = int(imageSizeWidth*n)
#if same:
 #   newImageSizeHeight = int(imageSizeHeight*n) 
#else:
#    newImageSizeHeight = int(imageSizeHeight/n) 
    
#background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
#img = Image.PhotoImage(background_image)
    Canvas1 = Canvas(root)
#Canvas1.create_image(300,340,image = img)      
#Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Admin Page", bg = 'black', fg = 'white', font=("Arial",15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    btn1 = Button(root,text="Search a book",bg='black', fg='white', command=openbookview) #add function
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="view all books",bg='black', fg='white', command=addbook)  #add function
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
    btn3 = Button(root,text="update info",bg='black', fg='white', command=addmem) #add function
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
    btn4 = Button(root,text="my book history",bg='black', fg='white', command=openviewmember) #add function
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    root.mainloop()

