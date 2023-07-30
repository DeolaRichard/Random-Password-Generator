import math


# fibonacci numbers module

def fib(n):  # write fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
        print()


def fib2(n):  # return fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
        return result


# using for else in loops
nums = [11, 13, 19, 18, 6, 9]

for num in nums:
    if num % 5 == 0:
        print(num)
        break  # to jump out of the loop
else:
    print("Not Found")

# To find if a number is prime or not
nums = int(input("Write a number to check: "))  # accept input from user
for i in range(2, nums):
    if nums % i == 0:  # check if the number is divisible by each number in iteration
        print("Not a Prime Number")
        break
else:
    print("Is a Prime Number")


# A more efficient way to solve this


def is_prime(num):
    if num < 2:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    # Only need to check up to the square root of the number
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True


num = int(input("Write a number to check: "))
if is_prime(num):
    print("Is a Prime Number")
else:
    print("Not a Prime Number")
