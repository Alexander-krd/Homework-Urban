numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes =[]
not_primes = []
for a in numbers:
    is_prime = True
    if a == 1:
        continue
    else:
        for b in range(2, a-1):
            if a % b == 0:
                is_prime = False
                break
    if is_prime:
        primes.append(a)
    else: not_primes.append(a)
print("Список:", numbers)
print("Простые числа:", primes)
print("Непростые числа:", not_primes)
