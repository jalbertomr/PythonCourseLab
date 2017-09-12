'''
Created on 27/03/2014

@author: Beto
Shelve pseudo database
'''
import shelve

def addCust(database):
    customer = {} #dictionary
    
    print "Add a new customer to the database\n"
    
    custNum = raw_input('Enter a customer number: ')
    customer['fisrtName'] = raw_input('Customer First Name: ')
    customer['lastName'] = raw_input('Customer last Name: ')
    customer['streetAdd'] = raw_input('Customer Street Name: ')
    customer['city'] = raw_input('Customer City: ') 
    customer['state'] = raw_input('Customer State: ')
    customer['zip'] = raw_input('Customer Zip Code: ')
    
    database[custNum] = customer
    
    return
    
def main():
    
    database = shelve.open('customers.dat', writeback = True)
    
    lookForCust = 1
    
    while(lookForCust != '0'):
        lookForCust = raw_input("Enter Customer Number ( 0 to Exit ) ")
        if lookForCust == '0':
            break
        else:
            try:
                for i in database[lookForCust]:
                    print i," ", database[lookForCust][i]
            except KeyError:
                print "Customer not in database"
                ans = raw_input("Do you want to add a new Customer?[Y|N]")
                if ans.upper()[0] == 'Y':
                    addCust(database)
            else:
                print "\n"
                    
    print "closing..."                
    database.close()
    print "exit!"

    
if __name__ == '__main__': main()