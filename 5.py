# Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.
tup=('Sandesh','Subedi','23')
li=[]
li.append(tup)
tup1=('Hari','Sharma','23')
li.append(tup1)
tup2=('Shyam','Poudel','23')
li.append(tup2)
print(sorted(li,key=lambda li: li[1]))