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
num = int(input("Write a number to check: "))  # accept input from user
for i in range(2, num):
    if num % i == 0:  # check if the number is divisible by each number in iteration
        print("Not a Prime Number")
        break
else:
    print("Is a Prime Number")
