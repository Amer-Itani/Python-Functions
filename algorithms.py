# O(1) + O(n) * O(1) => O(n)
def factorial(n):
    #O(1)
    result = 1

    if n == 0:
        return result
    elif n > 0:
        #O(n) n being the number of iterations from 1 to n.
        for i in range(n, 1, -1):
            #O(1)
            result *= i
        return result
    return
# O(1) + O(n) * O(1) => O(n)
def find_max(numbers):
    #O(1)
    maximum = numbers[0]

    #O(n) n being the length of the list numbers.
    for i in range(1, len(numbers)):
        #O(1)
        if numbers[i] > maximum:
            maximum = numbers[i]
    return maximum
#O(n) * O(1) + O(1) => O(n)
def linear_search(numbers, target):
    #O(n) n being the length of the list numbers.
    if target in numbers:
        #O(1)
        return True
    return False
#O(1) + O(2 ^ n) => O(2 ^ n)
def recursive_fibonacci(n):
    #O(1)
    if n == 0 or n == 1:
        return n
    elif n > 1:
        #O(2 ^ n) n being the position of the fibonacci sequence number.
        return fibonacci(n - 2) + fibonacci(n - 1)
    return
#O(1) + O(n) * O(1) => O(n)
def iterative_fibonacci(n):
    #O(1)
    first_number = 0
    second_number = 1
    result = 0

    if n == 0 or n == 1:
        return n
    elif n > 1:
        #O(n) n being the position of the fibonacci sequence number.
        for i in range(n-1):
            #O(1)
            third_number = first_number + second_number
            first_number = second_number
            second_number = third_number
        result = third_number
        return result
    return
#O(1)
logged_in = False
#O(1)
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

