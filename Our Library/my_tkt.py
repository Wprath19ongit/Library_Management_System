import tkinter as tk
import tkinter.font as tkFont
import sqlite3
import datetime

conn = sqlite3.connect('library.db')
c = conn.cursor()

conn2 = sqlite3.connect('client_books.db')
c2 = conn2.cursor()


class App:
    def __init__(self, root):
        #setting title
        root.title("LMS_Coep")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_486=tk.Label(root)
        GLabel_486["bg"] = "#ffd700"
        ft = tkFont.Font(family='Times',size=18)
        GLabel_486["font"] = ft
        GLabel_486["fg"] = "#cc0000"
        GLabel_486["justify"] = "center"
        GLabel_486["text"] = "LIBRARY MANAGEMENT SYSTEM"
        GLabel_486.place(x=110,y=60,width=385,height=70)

        GButton_261=tk.Button(root)
        GButton_261["bg"] = "#060000"
        GButton_261["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=10)
        GButton_261["font"] = ft
        GButton_261["fg"] = "#5fb878"
        GButton_261["justify"] = "center"
        GButton_261["text"] = "Admin Login"
        GButton_261.place(x=230,y=270,width=132,height=45)
        GButton_261["command"] = self.admin_login

        GButton_438=tk.Button(root)
        GButton_438["bg"] = "#100101"
        GButton_438["cursor"] = "spider"
        ft = tkFont.Font(family='Times',size=10)
        GButton_438["font"] = ft
        GButton_438["fg"] = "#5fb878"
        GButton_438["justify"] = "center"
        GButton_438["text"] = "Client login"
        GButton_438.place(x=230,y=150,width=132,height=45)
        GButton_438["command"] = self.client_login

        GButton_67=tk.Button(root)
        GButton_67["bg"] = "#070000"
        GButton_67["cursor"] = "spider"
        ft = tkFont.Font(family='Times',size=10)
        GButton_67["font"] = ft
        GButton_67["fg"] = "#33bc2c"
        GButton_67["justify"] = "center"
        GButton_67["text"] = "Client Sign-up"
        GButton_67.place(x=230,y=210,width=132,height=46)
        GButton_67["command"] = self.client_signup

        GButton_551=tk.Button(root)
        GButton_551["bg"] = "#cc0000"
        GButton_67["cursor"] = "spider"
        ft = tkFont.Font(family='Times',size=18)
        GButton_551["font"] = ft
        GButton_551["fg"] = "#393d49"
        GButton_551["justify"] = "center"
        GButton_551["text"] = "EXIT"
        GButton_551.place(x=250,y=350,width=90,height=25)
        GButton_551["command"] = self.exit

    def admin_login(self):
        print("command")


    def client_login(self):
        def __init__(self, root):
        #setting title
            root.title("login")
        #setting window size
            width=600
            height=500
            screenwidth = root.winfo_screenwidth()
            screenheight = root.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            root.geometry(alignstr)
            root.resizable(width=False, height=False)

            GLineEdit_544=tk.Entry(root)
            GLineEdit_544["bg"] = "#ffffff"
            GLineEdit_544["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times',size=10)
            GLineEdit_544["font"] = ft
            GLineEdit_544["fg"] = "#333333"
            GLineEdit_544["justify"] = "center"
            GLineEdit_544["text"] = "mis"
            GLineEdit_544.place(x=170,y=130,width=230,height=25)

            GLineEdit_951=tk.Entry(root)
            GLineEdit_951["bg"] = "#ffffff"
            GLineEdit_951["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times',size=10)
            GLineEdit_951["font"] = ft
            GLineEdit_951["fg"] = "#333333"
            GLineEdit_951["justify"] = "center"
            GLineEdit_951["text"] = "password"
            GLineEdit_951.place(x=170,y=190,width=230,height=25)

            GLabel_108=tk.Label(root)
            GLabel_108["bg"] = "#de3737"
            ft = tkFont.Font(family='Times',size=14)
            GLabel_108["font"] = ft
            GLabel_108["fg"] = "#333333"
            GLabel_108["justify"] = "center"
            GLabel_108["text"] = "Client Login"
            GLabel_108.place(x=190,y=60,width=174,height=30)

            GButton_493=tk.Button(root)
            GButton_493["bg"] = "#fad400"
            ft = tkFont.Font(family='Times',size=13)
            GButton_493["font"] = ft
            GButton_493["fg"] = "#ff8c00"
            GButton_493["justify"] = "center"
            GButton_493["text"] = "Login"
            GButton_493.place(x=320,y=260,width=70,height=25)
            GButton_493["command"] = self.GButton_493_command

    def GButton_493_command(self):
        print("command")





        mis = GLineEdit_544.entry(root)
        # c.execute("SELECT EXISTS(SELECT 1 FROM client_info WHERE mis=? LIMIT 1)", (mis,))
        c.execute("SELECT * FROM client_info")
        record = (c.fetchall())
        index=0
        for i in record:
            if mis == i[4]:
            
                print("Name is in the table")
                y = input("Enter password: ")
                c.execute("SELECT password FROM client_info WHERE mis=?", (mis,))
                z = c.fetchone()
                if y == z[0]:
                    print("CORRECT PASS")
                    show_client_options()
                    break
                else:
                    print("Wrong pass")
                    break
            
            else:
                index+=1
    
        if mis not in record[index]:
            print("Member not in the data")


    def client_signup(self):
        print("command")


    def exit(self):
        return

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
