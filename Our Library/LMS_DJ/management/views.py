from urllib import request, response
from django.http import *
from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
import datetime

from matplotlib.pyplot import get

conn = sqlite3.connect('library.db',  check_same_thread=False)
c = conn.cursor()

conn2 = sqlite3.connect('client_books.db',  check_same_thread=False)
c2 = conn2.cursor()
# Create your views here.

def home(request):
    return render(request, 'LMS.html')

def client_login(request):    
    return render(request,'Client_login.html')

def client_signup(request):    
    return render(request,'Client_signup.html')
    
def admin_login(request):    
    return render(request,'Admin_login.html')



def client_lgn(request):
    if request.method == 'POST':
        c.execute("SELECT * FROM client_info")
        record = (c.fetchall())
    
        username = request.POST["username"]
        for i in record:
            if username in i:
                a = 'Username already exists'
                return render(request,'Client_signup.html', {'msg': a})
            elif username=='cancel':
                return render(request,'LMS.html')
            
        password = request.POST["password"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        mis = request.POST["mis"]
        for i in record:
            if username in i:
                a = 'mis already exists'
                return render(request,'Client_signup.html', {'msg': a})
            elif mis=='cancel':
                return render(request,'LMS.html')

        branch = request.POST["branch"]
        college_email = request.POST["college_email"]
        mobile_no = request.POST["mobile_no"]
        none = '-'

        confirm = request.POST["confirm"]
        if(confirm=='Y' or confirm=='y' or confirm=='Yes' or confirm=='yes' or confirm=='YES'):
            c.execute("INSERT INTO client_info VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(username, password, first_name, last_name, mis, branch, college_email, mobile_no,none,none,none,none,none,none))
            conn.commit()
            c2.execute("CREATE TABLE [{mis}](book_name,author1,author2,author3,book_id,issue_date,return_date)")
            conn2.commit()
            return render(request,'Client_login.html')
        else:
            return render(request,'Client_signup.html')




def client_options(request):
    if request.method == 'POST':
        mis = request.POST["mis"]
        c.execute("SELECT * FROM client_info")
        record = (c.fetchall())
        index=-1
        for i in record:
            if mis == i[4]:
                y = request.POST["pass"]
                c.execute("SELECT password FROM client_info WHERE mis=?", (mis,))
                z = c.fetchone()
                if y == z[0]:
                    return render(request,'client_options.html')
                else:
                    res = 'incorrect password'
                    return render(request, 'Client_login.html',{'res':res})

            else:
                index+=1
    
        if mis not in record[index]:
            res = "Member not in the data"   
            return render(request,'Client_signup.html',{'res':res})
    
def admin_options(request):    
    return render(request,'admin_options.html')

def view_books(request):
    c.execute("SELECT rowid,* FROM books")
    record = c.fetchall()


    for i in record:
        print('\n'+str(i[0])+')      book:',i[1])
        {'a':str(i[0])}
        {'records':record}
        print('\n\tAuthor1:',i[2])
        print('\n\tAuthor2:',i[3])
        print('\n\tAuthor3:',i[4])
        print('\n\tBook_id:',i[5])
        print('\n\tAvalability status:',i[6])
    return render(request, 'view_books.html',{'records':record})

    #Prath
    #my_LMS@coep