# 9. Write a Python function that takes a number as a parameter and check the number is prime or not.
def check_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for i in range(2,n):
            if(n % i==0):
                return False
        return True

given_num=int(input("Enter a number:"))
print(check_prime(given_num))