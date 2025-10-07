def factorial(n):
    result = 1
    if n == 0:
        return result
    elif n > 0:
        for i in range(n, 1, -1):
            result *= i
        return result
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

def recursive_fibonacci(n):
    if n == 0 or n == 1:
        return n
    elif n > 1:
        return fibonacci(n - 2) + fibonacci(n - 1)
    return

def iterative_fibonacci(n):
    first_number = 0
    second_number = 1
    result = 0

    if n == 0 or n == 1:
        return n
    elif n > 1:
        for i in range(n-1):
            third_number = first_number + second_number
            first_number = second_number
            second_number = third_number
        result = third_number
        return result
    return