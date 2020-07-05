'''Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?'''
n=int(input("Enter the number of names you want to enter"))
names=[]
for i in range(n):
    name=input("Enter name")
    names.append(name)
    print(id(names))
#After appending too, there is no change in the id of the list.
print(sorted(names))
#After sorting the list, the names in the list is arranged in ascending order.