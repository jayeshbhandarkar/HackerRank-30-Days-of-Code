def is_prime(n):
    if n < 2:
        return False
        
    if n == 2:
        return True
        
    if n > 2 and n % 2 == 0:
        return False
        
    max_div = int(n ** 0.5)
    for i in range(3, max_div + 1, 2):
        if n % i == 0:
            return False
    return True

T = int(input())

for _ in range(T):
    n = int(input())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")
