# Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.
n=int(input("Enter the number of names you want to enter"))
names=[]
for i in range(n):
    name=input("Enter the name")
    names.append(name)
for i in range(len(names)):
    if names[i]=='John':
        print("The list has John in it")
        print(i)
        break
    elif names[i]!='John':
        if i==(len(names)-1):
            print("Not Found")
