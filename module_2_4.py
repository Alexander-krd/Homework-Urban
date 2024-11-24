numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes =[2, 3, 5, 7, 11, 13]
not_primes = [4, 6, 8, 9, 10, 12, 14, 15]
def number(num):
    n= num
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    return "True" if count ==2 else "False"
print(number(5))