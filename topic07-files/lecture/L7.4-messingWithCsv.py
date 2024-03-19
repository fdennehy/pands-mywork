# Messing with CSV
# This is a program to demonstrate storing data in csv format
# Author: FInbar Dennehy

import csv

mydict =[{'first': 'Andrew', 'last': 'Beatty', 'age':'2'},
         {'first': 'joe', 'last': 'Bloggs', 'age':'22'},
         {'first': 'Mary', 'last': 'mc', 'age':'2222'} 
        ] 
    
# field names 
fields = ['first', 'last', 'age'] 
    
# name of csv file 
FILENAME = "data.csv"
    
# writing to csv file 
with open(FILENAME, 'w', newline='') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
        
    # writing headers (field names) 
    writer.writeheader() 
    for dictrow in mydict:
        print(dictrow)
        writer.writerow(dictrow) 