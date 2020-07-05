#Write an if statement to determine whether a variable holding a year
#is a leap year.
year=int(input("Enter your year"))
if (year%4)==0 and (year%100)!=0:
    print("It is leap year")
elif (year%400==0):
    print("It is leap year")
else:
    print("It is not leap year")