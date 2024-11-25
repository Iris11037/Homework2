def is_prime(func):
    def wrapper(*args):
        fun = func(*args)
        for i in range(2, fun):
            if fun % i == 0:
                return (f"Число {fun} Составное")
        return f"Число {fun} Простое"
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)