# Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.
def is_palindrome(string):
    if string==string[::-1]:
        print("It is palindrome")
    else:
        print("It is not palindrome")
word=input("Enter your word")
is_palindrome(word)