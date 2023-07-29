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
