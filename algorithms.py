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

logged_in = False

while True:
    choice = int(input("Enter your choice number: "))

    if choice == 5:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == "root" and password == "pass":
            logged_in = True
        else:
            logged_in = False

    if logged_in:
        if choice == 1:
            number = int(input("Enter a number for factorial: "))
            print(factorial(number))

        elif choice == 2:
            max_list = list(map(int, input("Enter your list to find the maximum in it: ").split()))
            print(find_max(max_list))

        elif choice == 3:
            search_list = list(map(int, input("Enter your list to find a target in it: ").split()))
            t = int(input("Enter your target to be searched for in the list: "))
            print(linear_search(search_list, t))

        elif choice == 4:
            n = int(input("Enter your number to return the number in that position in the fibonacci sequence: "))
            print(iterative_fibonacci(n))

        elif choice == 6:
            print("Program ended.")
            break

