'''
Created on 27/03/2014

@author: Beto
sqlite
'''
import sqlite3

createDb = sqlite3.connect(':memory:')

queryCurs = createDb.cursor()

def createTable():
    queryCurs.execute('''CREATE TABLE customer
    (id INTEGER PRIMARY KEY, name TEXT, street TEXT, city TEXT, state TEXT, balance REAL)''')

def addCust(name, street, city, state, balance):
    queryCurs.execute('''INSERT INTO customer (name, street, city, state, balance)
    VALUES (?,?,?,?,?)''',(name, street, city, state, balance))
    
def main():
    createTable()
    
    addCust('Derel Banas','5798 Highway Ave','Verona','PA',145.34)
    addCust('Tito Lucas','234 orlando st.','Boca Raton','FL',32.323)
    addCust('Juanita Lopez','23 Guadalupe Blvd.','Mexico','DF',343.007)
    addCust('Paco Paco','12 Loreto Av.','Tampico','TM', 3.23)
    addCust('Abelardo Tam','123 Insurgentes','Cuernavaca','MR', 12312.02)

    createDb.commit()
    
    queryCurs.execute('SELECT * FROM customer ORDER BY balance')
    
    #add column to table
    queryCurs.execute('ALTER TABLE customer ADD COLUMN email TEXT')
    
    #Add email address to customer
    queryCurs.execute('UPDATE customer SET email="derek@gmail.com" WHERE id = 1')
    
    #Delete email address of a customer
    queryCurs.execute('DELETE FROM customer WHERE id=4')
    
    #Print customers ordered by lowest balancce and with titles
    queryCurs.execute('SELECT * FROM customer ORDER BY balance DESC, name LIMIT 2 OFFSET 2')
    
    
    
    listTitle = ['id','name', 'street', 'city', 'state', 'balance','email']
    k = 0
    
    for i in queryCurs:
      print '\n'
      for j in i:
          print "%-10s :" % (listTitle[k]),
          print j
          if k < 6: k += 1
          else: k = 0
    
if __name__ == '__main__': main()
