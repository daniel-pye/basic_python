def collatz(num):

        if num % 2 == 0:
            print(num // 2)
            return num // 2
        elif num % 2 == 1:
            result = 3 * num + 1
            print(result)
            return result

try:
    output = input("Enter the number to Collatz:\n")
    while output != 1:
        output = collatz(int(output))
except ValueError:
    print("Whoops, please type in an integer!")
