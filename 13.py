# Write a function to write a comma-separated value (CSV) file. It
# should accept a filename and a list of tuples as parameters. The
# tuples should have a name, address, and age. The file should create
# a header row followed by a row for each tuple. If the following list of
# tuples was passed in:
# [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
# it should write the following in the file:
# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21
import csv
def func(filename,*args):
    with open("%s.csv"%(filename),'a',newline='\n') as file:
        writer=csv.writer(file)
        writer.writerow([*args])
filename=input("Enter file name")
with open("%s.csv"%(filename),'a',newline='\n') as file:
        writer=csv.writer(file)
        writer.writerow(['Name','Address','Age'])
n=int(input("Enter the number of data you want to enter"))
for i in range(n):
    name=input("Enter name")
    address=input("Enter address")
    age=input("Enter age")
    func(filename,name,address,age)