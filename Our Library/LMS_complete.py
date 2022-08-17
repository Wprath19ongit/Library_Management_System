import sqlite3
import datetime

conn = sqlite3.connect('library.db')
c = conn.cursor()

conn2 = sqlite3.connect('client_books.db')
c2 = conn2.cursor()

#---------------------------------------------------------------------------------------------------------------------

def client_login():
    

    mis = input("Enter mis: ")
    # c.execute("SELECT EXISTS(SELECT 1 FROM client_info WHERE mis=? LIMIT 1)", (mis,))
    try:
        c.execute("SELECT * FROM client_info")
    except UnboundLocalError:
        print("wrong username")
        return
    
    record = (c.fetchall())
    for i in record:
        if mis == i[4]:
            y = input("Enter password: ")
            c.execute("SELECT password FROM client_info WHERE mis=?", (mis,))
            z = c.fetchone()
            if y == z[0]:
                print("\nCORRECT PASS\n")
                show_client_options(mis)
                break
            else:
                print("\nWrong pass\n")
                break


#---------------------------------------------------------------------------------------------------------------------
def client_signup():


    c.execute("SELECT * FROM client_info")
    record = (c.fetchall())
    
    username = input('Enter username: ')
    for i in record:
        if username == i[0]:
            print('\nUsername already exists.')
            print('\nEnter another username.\n ')
            break
        elif username=='cancel':
            return

    password = input('Enter password: ')
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')

    mis = input('Enter mis: ')
    for i in record:
        if username in i:
            print('mis already exists.')
            username = input('Enter valid mis: ')
        elif mis=='cancel':
            return

    branch = input('Enter branch: ')
    college_email = input('Enter college mail-id: ')
    mobile_no = input('Enter mobile no: ')
    none = '-'
    # c.execute("SELECT password FROM client_info WHERE mis=?", (mis,))

    confirm = input("confirm sign-up - Y/N")
    if(confirm=='Y' or confirm=='y' or confirm=='Yes' or confirm=='yes' or confirm=='YES'):
        c.execute("INSERT INTO client_info VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(username, password, first_name, last_name, mis, branch, college_email, mobile_no,none,none,none,none,none,none))
        conn.commit()
        c2.execute("CREATE TABLE [{mis}](book_name,author1,author2,author3,book_id,issue_date,return_date)")
        conn2.commit()
    else:
        return

# ----------------------------------------------------------------------------------------------------------------

def admin_login():
    

    username = input("Enter username: ")
    # c.execute("SELECT EXISTS(SELECT 1 FROM client_info WHERE mis=? LIMIT 1)", (mis,))
    # csr1.execute("SELECT * FROM books WHERE book_author LIKE 'Reema%'")
    c.execute("SELECT * FROM admin_info")
    record = (c.fetchall())
    index=0
    for i in record:
        if len(i)>0 and username == i[0]:
            
            print("Name is in the table")
            y = input("Enter password: ")
            c.execute("SELECT password FROM admin_info WHERE username=?", (username,))
            z = c.fetchone()
            if y == z[0]:
                print("CORRECT PASS")
                show_admin_options()
                break
            else:
                print("Wrong pass")
                break
            
        else:
            index+=1
    
    if index>len(record):
        print("Member not in the data")
        return

#------------------------------------------------------------------------------------------------------------------------------------------------------------

def show_client_options(mis):

    while(1):
        print('1. view all books')
        print('2. search book')
        print('3. update info')
        print('4. my book history')
        print('0. Exit')
        choice = input('Enter choice: ')
        if (choice=='1'):
            view_books()
        elif (choice=='0'):
            return
        elif (choice=='2'):
            search_books()
        elif(choice=='3'):
            update_client_info(mis)
        elif(choice=='4'):
            book_history_client(mis)
        else:
            print('Enter valid choice')

#---------------------------------------------------------------------------------------------------------------------

def view_books():
    c.execute("SELECT rowid,* FROM books")
    record = c.fetchall()

    for i in record:
        print('\n'+str(i[0])+')      book:',i[1])
        print('\n\tAuthor1:',i[2])
        print('\n\tAuthor2:',i[3])
        print('\n\tAuthor3:',i[4])
        print('\n\tBook_id:',i[5])
        print('\n\tAvalability status:',i[6])


#---------------------------------------------------------------------------------------------------------------------


def search_books():
    # c.execute("SELECT EXISTS(SELECT 1 FROM client_info WHERE mis=? LIMIT 1)", (mis,))
    bk = input("Enter book you want to search: ")
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
    if(len(result)>0):
        for i in result:
            print('\n'+str(i[0])+')      book:',i[1])
            print('\n\tAuthor1:',i[2])
            print('\n\tAuthor2:',i[3])
            print('\n\tAuthor3:',i[4])
            print('\n\tBook_id:',i[5])
            print('\n\tAvalability status:',i[6])
    else:
        print("No such book in our library.")

#---------------------------------------------------------------------------------------------------------------------


def update_client_info(mis):
    c.execute("SELECT * FROM client_info")
    record = (c.fetchall())
    index=0
    for i in record:
        if mis == i[4]:
            y = input("Enter password: ")
            c.execute("SELECT password FROM client_info WHERE mis=?", (mis,))
            z = c.fetchone()
            if y == z[0]:
                while(1):
                    print('1. update first name')
                    print('2. update last name')
                    print('3. update mobile no')
                    print('4. update branch')
                    print('5. exit')
                    choice = input("Enter Choice: ")
                    if choice=='1':
                        first_name = input('Enter new first name: ')
                        c.execute("UPDATE client_info SET first_name = ? WHERE mis=?",(first_name,mis))
                        conn.commit()
                        return
            
                    elif choice=='2':
                        last_name = input('Enter new last name: ')
                        c.execute("UPDATE client_info SET last_name = ? WHERE mis=?",(last_name,mis))
                        conn.commit()
                        return
            
                    elif choice=='3':
                        number = input('Enter new number: ')
                        c.execute("UPDATE client_info SET number = ? WHERE mis=?",(number,mis))
                        conn.commit()
                        return

                    elif choice=='4':
                        branch = input('Enter new branch: ')
                        c.execute("UPDATE client_info SET branch = ? WHERE mis=?",(branch,mis))
                        conn.commit()
                        return
        
                    elif choice=='5':
                        return
                    else:
                        print("Enter Valid choice...")
                    break
            else:
                print("Wrong pass")
                break


#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------


def show_admin_options():
    while(1):
        print('1. view all books\n')
        print('2. search any book\n')
        print('3. allot book to a client\n')
        print('4. get return from  client\n')
        print('5. add a book\n')
        print('6. remove a book\n')
        print("7. Update book info\n")
        print('8. View all clients\n')
        print("9. Search a client\n")
        print("10. Remove a client\n")
        print("11. Client book history\n")
        print('0. exit\n')
        choice = input('Enter choice: ')
        if (choice=='0'):
            return
        elif (choice=='1'):
            view_books()
        elif (choice=='2'):
            search_books()
        elif(choice=='3'):
            book_allot()
        elif (choice=='4'):
            book_return()
        elif (choice=='5'):
            add_book()
        elif (choice=='6'):
            delete_book()
        elif (choice=='7'):
            update_book_info()
        elif(choice == '8'):
            view_clients()
        elif(choice=='9'):
            search_clients()
        elif (choice=='10'):
            remove_client()
        elif(choice=='11'):
            book_history_admin()
        else:
            print('Enter valid choice')


#---------------------------------------------------------------------------------------------------------------------


def add_book():
    
    book_added = []
    book_name = input("Enter book name: ")
    book_added.append(book_name)
    author1 = input("Enter Author: ")
    book_added.append(author1)
    author2 = input("Enter Author2 if any: ")
    book_added.append(author2)
    author3 = input("Enter Author3 if any: ")
    book_added.append(author3)
    # no repeated id feature is remaining
    c.execute("SELECT book_id FROM books")
    bks = c.fetchall()
    id_list = []
    for i in bks:
        id_list.append(i[0])        
    
    while(1):
        book_id = input("Enter new book-id: ")
        if book_id not in id_list:
            book_added.append(book_id)
            break
        else:
            print("Enter unique id for the book.")
    book_added.append("available")
    book_added = tuple(book_added)
    book = []
    book.append(book_added)
    print(book_added)
    confirm = input("Confirm book add? (Y/N)")
    if(confirm=='Y' or confirm=='y' or confirm=='Yes' or confirm=='yes' or confirm=='YES'):
        c.executemany("INSERT INTO books VALUES(?,?,?,?,?,?)",book)
        conn.commit()
        print("The book is added to the library")
        return
    else: 
        print("The book is not added to the library")
        return

#---------------------------------------------------------------------------------------------------------------------

def delete_book():
    search_books()
    c.execute("SELECT book_id FROM books")
    bks = c.fetchall()
    id_list = []
    for i in bks:
        id_list.append(i[0])        
    
    while(1):
        a = input("Enter book-id: ")
        if a in id_list:
            break
        else:
            print("Enter valid id for the book.")
    
    confirm = input("Confirm book delete? (Y/N)")
    if(confirm=='Y' or confirm=='y' or confirm=='Yes' or confirm=='yes' or confirm=='YES'):
        c.execute("DELETE FROM books WHERE book_id=?",(a))
        conn.commit()
        print("The book is deleted from the library")
        return
    else: 
        print("The book is not deleted from the library")
        return

#---------------------------------------------------------------------------------------------------------------------

def book_allot():
    mis = input("Enter client's mis: ")
    c.execute("SELECT * from client_info WHERE mis=?",[mis])
    client = c.fetchall()
    client[0] = list(client[0])
    search_books() # here search function will allow librarian to see the book_id of the desired book

    book_id = input("Enter book_id: ")
    c.execute("SELECT * from books WHERE book_id=?",[book_id])
    book_info = c.fetchall()
    book_info[0] = list(book_info[0])
    un = 'unavailable'
    print(book_info[0][5])
    if(book_info[0][5] == 'unavailable'):
        print("Book unavailable")
        return
    else :
        if client[0][8] == '-' or client[0][10] !='-':
            client[0][8] = book_info[0][4]
            client[0][9] = datetime.datetime.today()
            client[0][10] ='-'
            c.execute("UPDATE client_info SET book1_id = ? WHERE mis=?",[client[0][8],mis])
            c.execute("UPDATE client_info SET date_of_issue1 = ? WHERE mis=?",[client[0][9],mis])
            c.execute("UPDATE client_info SET date_of_return1 = ? WHERE mis=?",[client[0][10],mis])
            c.execute("UPDATE books SET Availability = ? WHERE book_id=?",[un,book_info[0][4]])
            conn.commit()
            bklist = [book_info[0][0],book_info[0][1],book_info[0][2],book_info[0][3],book_info[0][4],client[0][9],client[0][10]]
            conn2.execute(f"INSERT INTO [{mis}] VALUES (?,?,?,?,?,?,?)",(bklist))
            conn2.commit()
            print("The book has been alloted.")
            return
        elif client[0][11] == '-' or client[0][13]!='-':
            client[0][11] = book_info[0][4]
            client[0][12] = datetime.datetime.today()
            client[0][13] = '-'
            c.execute("UPDATE client_info SET book2_id = ? WHERE mis=?",[client[0][11],mis])
            c.execute("UPDATE client_info SET date_of_issue2 = ? WHERE mis=?",[client[0][12],mis])
            c.execute("UPDATE client_info SET date_of_return2 = ? WHERE mis=?",[client[0][13],mis])
            c.execute("UPDATE books SET Availability = ? WHERE book_id=?",[un,book_info[0][4]])
            conn.commit()
            bklist = [book_info[0][0],book_info[0][1],book_info[0][2],book_info[0][3],book_info[0][4],client[0][12],client[0][13]]
            conn2.execute(f"INSERT INTO [{mis}] (book_name,author1,author2,author3,book_id,issue_date,return_date) VALUES (?,?,?,?,?,?,?)",(bklist))
            conn2.commit()
            print("The book has been alloted.")
            return
        else:
            print("First return previous books") 
            return

# ---------------------------------------------------------------------------------------------------------------

def book_return():
    mis = input("Enter client's mis: ")
    c.execute("SELECT * from client_info WHERE mis=?",[mis])
    client = c.fetchall()
    client[0] = list(client[0])
    
    book_id = input("Enter book_id: ")
    c.execute("SELECT * from books WHERE book_id=?",[book_id])
    book_info = c.fetchall()
    book_info[0] = list(book_info[0])
    
    if (client[0][8] == book_id and client[0][10]=='-'):
        client[0][10] = datetime.datetime.today()
        c.execute("UPDATE client_info SET date_of_return1 = ? WHERE mis=?",(client[0][10],mis))
        c.execute("UPDATE books SET Availability = 'available' WHERE book_id=?",(book_info[0][4]))
        conn.commit()
        print("The book is returned")

        c2.execute(f"SELECT rowid,* FROM [{mis}] WHERE return_date = '-'")
        book_with_client = c2.fetchall()
        for i in book_with_client:
            if i[5] == book_info[0][4]:
                row_id = i[0]
        conn2.execute(f"UPDATE [{mis}] SET return_date = ? WHERE rowid=?",(client[0][10],row_id))
        conn2.commit()
        return
    
    elif (client[0][11] == book_id and client[0][13]=='-'):    
        client[0][13] = datetime.datetime.today()
        c.execute("UPDATE client_info SET date_of_return2 = ? WHERE mis=?",(client[0][13],mis))
        c.execute("UPDATE books SET Availability = 'available' WHERE book_id=?",(book_info[0][4]))
        conn.commit()
        print("The book is returned")
        
        c2.execute(f"SELECT rowid,* FROM [{mis}] WHERE return_date = '-'")
        book_with_client = c2.fetchall()
        for i in book_with_client:
            if i[5] == book_info[0][4]:
                row_id = i[0]
        conn2.execute(f"UPDATE [{mis}] SET return_date = ? WHERE rowid=?",(client[0][10],row_id))
        conn2.commit()
        return


# -------------------------------------------------------------------------------------------------------

def update_book_info():
    i=1
    book_id = input('enter book_id: ')
    c.execute("SELECT * FROM books WHERE book_id = ?",(book_id))
    book = c.fetchall()
    while(i):
        print('1. update book name')
        print('2. update author1')
        print('3. update author2')
        print('4. update author3')
        print('5. update availability')
        print('0. exit')
        choice = input()
        if choice=='1':
            bookname = input('Enter new book name: ')
            c.execute("UPDATE books SET book_name = ? WHERE book_id=?",(bookname,book_id))
            conn.commit()
            return
            
        elif choice=='2':
            author1 = input('Enter new author1: ')
            c.execute("UPDATE books SET author1 = ? WHERE book_id=?",(author1,book_id))
            conn.commit()
            return

        elif choice=='3':
            author2 = input('Enter new author2: ')
            c.execute("UPDATE books SET author2 = ? WHERE book_id=?",(author2,book_id))
            conn.commit()
            return

        elif choice=='4':
            author3 = input('Enter new author3: ')
            c.execute("UPDATE books SET author3 = ? WHERE book_id=?",(author3,book_id))
            conn.commit()
            return

        elif choice=='5':
            avail = input('Toggle availability?: (Y/N)')
            if(avail=='Y' or avail=='y' or avail=='Yes' or avail=='yes' or avail=='YES'):
                if(book[5]== 'available'):
                    c.execute("UPDATE books SET Availability = 'unavailable' WHERE book_id=?",(book_id))
                    conn.commit()
                    print("The book is now unavailable")
                    return
                elif(book[5]=='unavailable'):
                    c.execute("SELECT * FROM client_info")
                    clients = c.fetchall()
                    for i in clients:
                        if(i[8]==book_id or i[11]==book_id):
                            print("Availability cannot be toggled as the client has not yet returned the book.")
                            return
                    c.execute("UPDATE books SET Availability = 'available' WHERE book_id=?",(book_id))
                    conn.commit()
                    print("The book is now available")
        
        elif choice=='0':
            return
        else:
            print("Enter Valid choice...")

#---------------------------------------------------------------------------------------------------------------------

def view_clients():
    c.execute("SELECT rowid,* FROM client_info")
    record = c.fetchall()
    for i in record:
        print('\n'+str(i[0])+')      name:',i[3],i[4])
        print('\n\tmis:',i[5])
        print('\n\tbranch:',i[6])
        print('\n\temail-add:',i[7])
        print('\n\tcontact-no:',i[8])
        print('\n\tbook1_id:',i[9]+', issue-date:',i[10]+', return-date:',i[11])
        print('\n\tbook2_id:',i[12]+', issue-date:',i[13]+', return-date:',i[14])



#---------------------------------------------------------------------------------------------------------------------


def search_clients():

    bk = input("Enter client you want to search: ")
    bk = '%'+bk+'%'
    c.execute("SELECT rowid,* FROM client_info WHERE first_name LIKE ?",[bk])
    result1 = c.fetchall()
    c.execute("SELECT rowid,* FROM client_info WHERE last_name LIKE ?",[bk])
    result2 = c.fetchall()
    c.execute("SELECT rowid,* FROM client_info WHERE mis  LIKE ?",[bk])
    result3 = c.fetchall()
    c.execute("SELECT rowid,* FROM client_info WHERE branch LIKE ?",[bk])
    result4 = c.fetchall()
    c.execute("SELECT rowid,* FROM client_info WHERE college_email LIKE ?",[bk])
    result5 = c.fetchall()
    c.execute("SELECT rowid,* FROM client_info WHERE mobile_no LIKE ?",[bk])
    result6 = c.fetchall()
    result = result1+result2+result3+result4+result5+result6
    result = set(result)
    if(len(result)>0):
        for i in result:
            print('\n'+str(i[0])+')      name:',i[3],i[4])
            print('\n\tmis:',i[5])
            print('\n\tbranch:',i[6])
            print('\n\temail-add:',i[7])
            print('\n\tcontact-no:',i[8])
            print('\n\tbook1:',i[9]+', issue-date:',i[10]+', return-date:',i[11])
            print('\n\tbook2:',i[12]+', issue-date:',i[13]+', return-date:',i[14])
    else:
        print("Client not found.")

#---------------------------------------------------------------------------------------------------------------------

def remove_client():
    
    search_clients()
    c.execute("SELECT mis FROM client_info")
    bks = c.fetchall()
    id_list = []
    for i in bks:
        id_list.append(i[0])        
    
    while(1):
        a = input("Enter mis: ")
        if a in id_list:
            break
        if a == 'cancel':
            return
        else:
            print("Enter valid mis of the client.")
    
    confirm = input("Confirm removal of client? (Y/N)")
    if(confirm=='Y' or confirm=='y' or confirm=='Yes' or confirm=='yes' or confirm=='YES'):
        c.execute("DELETE FROM client_info WHERE mis=?",[a])
        conn.commit()
        print("The client is removed.")
        return
    else: 
        print("The client is still our.")
        return

#---------------------------------------------------------------------------------------------------------------------

def book_history_admin():
    mis = input("Enter mis: ")
    c2.execute(f"SELECT rowid,* FROM [{mis}]")
    record = c2.fetchall()
    if len(record) == 0:
        print('no books borrowed till date.')
    for i in record:
        print('\n'+str(i[0])+')      book:',i[1])
        print('\n\tAuthors:',i[2],i[3],i[4])
        print('\n\tBook_id:',i[5])
        print('\n\tIssue date:',i[6],', Return date:',i[7])
    
#---------------------------------------------------------------------------------------------------------------------

def book_history_client(mis):
    c2.execute(f"SELECT rowid,* FROM [{mis}]")
    record = c2.fetchall()
    if len(record) == 0:
        print('no books borrowed till date.')
    for i in record:
        print('\n'+str(i[0])+')      book:',i[1])
        print('\n\tAuthors:',i[2],i[3],i[4])
        print('\n\tBook_id:',i[5])
        print('\n\tIssue date:',i[6],', Return date:',i[7])

#---------------------------------------------------------------------------------------------------------------------


print("WELCOME TO OUR COMPUTER DEPARTMENT LIBRARY \n\n\n")
while(1):
    print("\t 1. Client log-in\n")
    print("\t 2. Client sign-up\n")
    print("\t 3. Admin log-in\n\n")
    print("\t 0. Exit.")
    choice = input("Please Enter Choice: ")
    if(choice=='1'):
        client_login()
    elif(choice=='2'):
        client_signup()
    elif(choice=='3'):
        admin_login()
    elif(choice=='0'):
        print("Thank you for visiting our library\n")
        break
    else:
        print("Please Enter valid choice\n")

#------------------------------------------------------------------------------------------------------------------------------------------------------------

conn.close()
conn2.close()

#------------------------------------------------------------------------------------------------------------------------------------------------------------