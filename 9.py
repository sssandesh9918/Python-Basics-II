# Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.
def bin(args,l,r,x):
    if r>=l:
        m=int(l+(r-l)/2)
        if args[m]==x:
            return m
        elif args[m]>x:
            return bin(args,l,m-1,x)
        else:
            return bin(args,m+1,r,x)
    else:
        return -1
args=[2,3,4,10,40]
s=bin(args,0,len(args)-1,40)
if s!=-1:
    print("There is given element in the list in index",s)
else:
    print("There is no given element in the list")