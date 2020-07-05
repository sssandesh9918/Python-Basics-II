# Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.
tup=[('Sandesh','Subedi','23'),('Shyam','Sharma','24'),('Hari','Poudel',26),('John','Kandel',None)]
li=[]
for a in tup:
    li.append(a[2])
print(li)
sum=0
count=0
for i in range(len(li)):
    if li[i]!=None:
        sum=sum+int(li[i])
        count=count+1
aveg=sum/count
print(aveg)