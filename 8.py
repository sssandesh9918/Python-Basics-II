# Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
print(is_prime(2))
print(is_prime(7))
print(is_prime(12))
print(is_prime(13))