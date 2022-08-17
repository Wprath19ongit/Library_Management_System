
import sqlite3

conn = sqlite3.connect('library.db')
c = conn.cursor()

c.execute("""CREATE TABLE books(book_name text,author1 text,author2 text,author3 text,book_id text,Availability text)""")

c.execute("""CREATE TABLE client_info(username text, password text, first_name text, last_name text, mis text, branch text, college_email text, mobile_no text,
                book1_id text, date_of_issue1 text, date_of_return1 text, book2_id text, date_of_issue2 text, date_of_return2 text)""")

c.execute("""CREATE TABLE admin_info(username text, password text, first_name text, last_name text, mobile_no text)""")

lib_books =[
    ('Programming with python','Reema Thareja','-','-','1','available'),
    ('Digital Logic Design','Morris Mano','-','-','2','available'),
    ('Engineering Graphics','N.D. Bhatt','-','-','3','available')
    ]

c.executemany("""INSERT INTO books VALUES (?,?,?,?,?,?)""", lib_books)

clients =[
    ('Prath','pass1','Prathamesh','Wani','112003152','computer','wanips20.comp@coep.ac.in','9923496033','-','-','-','-','-','-'),
    ('Aniche','pass2','Anish','Deshpande','112010029','computer','despandeaaps20.comp@coep.ac.in','7038147517','-','-','-','-','-','-'),
    ('Soniye','pass3','Soniya','Bhat','112003159','computer','bhatss20.comp@coep.ac.in','8624959339','-','-','-','-','-','-'),
    ('Aaadi','pass4','Adi','Shendge','112003157','computer','shendgeap20.comp@coep.ac.in','9764581880','-','-','-','-','-','-')
    ]

c.executemany("""INSERT INTO client_info VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", clients)

admins =[
    ('Prath','pass1','Prathamesh','Wani','9923496033'),
    ('Aniche','pass2','Anish','Deshpande','7038147517'),
    ('Soniye','pass3','Soniya','Bhat','8624959339'),
    ('Aaadi','pass4','Adi','Shendge','9764581880')
    ]

c.executemany("""INSERT INTO admin_info VALUES (?,?,?,?,?)""", admins)

conn.commit()
conn.close()
