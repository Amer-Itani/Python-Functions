def factorial(n):
    result = 1
    if n == 0:
        return result
    elif n > 0:
        for i in range(n, 1, -1):
            result *= i
        return result
    else:
        return
