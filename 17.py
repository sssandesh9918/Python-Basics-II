# Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.
num1=float(input("Enter one number"))
num2=float(input("Enter another number"))
operator=input("Enter the operator you want to operate with")
if operator=='+':
    print('%s+%s='%(num1,num2),(num1+num2))
elif operator=='-':
    print('%s-%s='%(num1,num2),(num1-num2))
elif operator=='*':
    print('%s*%s='%(num1,num2),(num1*num2))
elif operator=='%':
    print('{}%{}='.format(num1,num2),(num1%num2))
elif operator=='/':
    try:
        print('{}/{}='.format(num1,num2),(num1/num2))
    except:
        num2=0
        print("Cannot divide by zero")