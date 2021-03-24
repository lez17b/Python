water = 400
milk = 540
coffee_beans = 120
dispensable_cups = 9
money = 550
Coffee_Machine = [water,
                  milk,
                  coffee_beans,
                  dispensable_cups,
                  money]
Espresso = [250, 0, 16, 1, 4]
Latte = [350, 75, 20, 1, 7]
Cappuccino = [200, 100, 12, 1, 6]


def remaining(coffee_machine):
    print("The coffee machine has: ")
    print(Coffee_Machine[0], " of water")
    print(Coffee_Machine[1], " of milk")
    print(Coffee_Machine[2], " of coffee beans")
    print(Coffee_Machine[3], " of disposable cups")
    print(Coffee_Machine[4], " of money")
    print('')


def buy(coffee_machine):
    typeC = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
    if typeC == 1:
        
        if coffee_machine[0] >= 250 and coffee_machine[2] >= 16 and coffee_machine[3] >= 1:
            print('I have enough resources, making you a coffee!')
            coffee_machine[0] = coffee_machine[0] - 250
            coffee_machine[1] = coffee_machine[1] - 0
            coffee_machine[2] = Coffee_Machine[2] - 16
            coffee_machine[3] = coffee_machine[3] - 1
            coffee_machine[4] = coffee_machine[4] + 4
        elif  coffee_machine[0] < 250:
            print('Sorry, not enough water!')
        elif coffee_machine[2] < 16:
            print('Sorry, not enough coffee beans!')
        elif coffee_machine[3] < 1:
            print('Sorry, not enough cups!')
    elif typeC == 2:
        
        if coffee_machine[0] >= 350 and coffee_machine[1] >=75 and coffee_machine[2] >= 20 and coffee_machine[3] >= 1:
            print('I have enough resources, making you a coffee!')
            coffee_machine[0] = coffee_machine[0] - 350
            coffee_machine[1] = coffee_machine[1] - 75
            coffee_machine[2] = coffee_machine[2] - 20
            coffee_machine[3] = coffee_machine[3] - 1
            coffee_machine[4] = coffee_machine[4] + 7
        elif  coffee_machine[0] < 350:
            print('Sorry, not enough water!')
        elif coffee_machine[2] < 20:
            print('Sorry, not enough coffee beans!')
        elif coffee_machine[1] < 75:
            print('Sorry, not enough milk!')   
        elif coffee_machine[3] < 1:
            print('Sorry, not enough cups!')
    elif typeC == 3:
        
        if coffee_machine[0] >= 200 and coffee_machine[1] >=100 and coffee_machine[2] >= 12 and coffee_machine[3] >= 1:
            print('I have enough resources, making you a coffee!')
            coffee_machine[0] = coffee_machine[0] - 200
            coffee_machine[1] = coffee_machine[1] - 100
            coffee_machine[2] = coffee_machine[2] - 12
            coffee_machine[3] = coffee_machine[3] - 1
            coffee_machine[4] = coffee_machine[4] + 6
        elif  coffee_machine[0] < 200:
            print('Sorry, not enough water!')
        elif coffee_machine[2] < 12:
            print('Sorry, not enough coffee beans!')
        elif coffee_machine[1] < 100:
            print('Sorry, not enough milk!')   
        elif coffee_machine[3] < 1:
            print('Sorry, not enough cups!')


def fill(coffee_machine):
    amount_water = int(input("Write how many ml of water do you want to add:"))
    amount_milk = int(input("Write how many ml of milk do you want to add:"))
    amount_coffee = int(input("Write how many grams of coffee beans do you want to add:"))
    amount_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
    amounts = [amount_water, amount_milk, amount_coffee, amount_cups]
    i = 0
    for i in range(0, 4):
        Coffee_Machine[i] = Coffee_Machine[i] + amounts[i]
    print('')
    print('')
    print("The coffee machine has:")
    print(coffee_machine[0], "of water")
    print(coffee_machine[1], "of milk")
    print(coffee_machine[2], "of coffee beans")
    print(coffee_machine[3], "of disposable cups")
    print(coffee_machine[4], "of money")


def take(coffee_machine):
    print("I gave you", "$", 550)
    Coffee_Machine[4] = Coffee_Machine[4] - Coffee_Machine[4]
    print("")
    print("The coffee machine has:")
    print(coffee_machine[0], "of water")
    print(coffee_machine[1], "of milk")
    print(coffee_machine[2], "of coffee beans")
    print(coffee_machine[3], "of disposable cups")
    print(coffee_machine[4], "of money")


Option = ''
while Option != 'exit':
    print("Write action (buy, fill, take, remaining, exit):")
    Option = input()

    if Option == 'buy':
        buy(Coffee_Machine)
    elif Option == 'fill':
        fill(Coffee_Machine)
    elif Option == 'take':
        take(Coffee_Machine)
    elif Option == 'remaining':
        remaining(Coffee_Machine)
