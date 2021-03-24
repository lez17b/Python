
def main():
    print("Welcome to the playing with numbers program")
    print("--------------------------------------------")
    print("""
    1) Compute if a number is prime
    2) Count the number of digits in a number that are prime
    3) Quit
    """)
    menu_choice = int(input())
    if menu_choice == 1:
        prime = getValidUserInput()
        flag = isPrime(prime)
        if flag:
            print(" IsPrime({}) = Yes".format(prime))
        else:
            print(" IsPrime({}) = No".format(prime))
    elif menu_choice == 2:
        prime = getValidUserInput()
        total = numPrimeDigits(prime)
        print(total)
    elif menu_choice == 3:
        print("Good Bye!")
    else:
        print("Please run the program again and choose from 1 to 3")


def getValidUserInput():
    number = int(input("Enter in a positive number (>0): "))
    while number < 0:
        number = int(input("Enter in a positive number (>0): "))
    return number


def isPrime(prime):
    flag = True
    for i in range(2, prime // 2):
        if prime % i == 0:
            flag = False
            break

    return flag


def numPrimeDigits(prime):
    total_digits = 0
    for i in range(2, prime + 1):
        if i % prime == 0:
            total_digits += 1

    return total_digits


main()

