
import sqlite3

conn = sqlite3.connect('library.db')
c = conn.cursor()

c.execute("SELECT rowid,* FROM books")
data=(c.fetchall())
print('the books in our library-\n')
for i in data:
    print('\n'+str(i[0])+')      book:',i[1])
    print('\n\tAuthor1:',i[2])
    print('\n\tAuthor2:',i[3])
    print('\n\tAuthor3:',i[4])
    print('\n\tBook_id:',i[5])
    print('\n\tAvalability status:',i[6])

print('\n\n\n')
c.execute("SELECT rowid,* FROM client_info")
data=(c.fetchall())
print('the clients of our library-')
for i in data:
    print('\n'+str(i[0])+')      firstname:',i[3])
    print('\n\tlastname:',i[4])
    print('\n\tmis:',i[5])
    print('\n\tbranch:',i[6])
    print('\n\temail-add:',i[7])
    print('\n\tcontact-no:',i[8])
    print('\n\tbook1:',i[9]+', issue-date:',i[10]+', return-date:',i[11])
    print('\n\tbook1:',i[12]+', issue-date:',i[13]+', return-date:',i[14])
    
print('\n\n\n')
c.execute("SELECT rowid,* FROM admin_info")
data=(c.fetchall())
print('the admins of our library-')
for i in data:
    print('\n'+str(i[0])+')      firstname:',i[3])
    print('\n\tlastname:',i[4])
    print('\n\tcontact-no:',i[5])

conn.close()