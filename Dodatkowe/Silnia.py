
def factorial(n):
    if n == 1:
        result = 1

    elif n>1:
        result = n*factorial(n-1)
        n -= 1
    return result


if __name__ == "__main__":
    n = int(input("Enter your number:\n"))
    print(factorial(n))
