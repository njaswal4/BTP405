def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def getPrimeNumbers(n):
    return [num for num in range(2, n + 1) if is_prime(num)]

# Example->
n = 15
result = getPrimeNumbers(n)
print(f"Prime numbers between 2 and {n}: {result}")
