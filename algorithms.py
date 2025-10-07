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

def find_max(numbers):
    maximum = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > maximum:
            maximum = numbers[i]
    return maximum

def linear_search(numbers, target):
    if target in numbers:
        return True
    return False
