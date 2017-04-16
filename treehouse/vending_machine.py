sodas = ["Pepsi", "Cherry Coke", "Coke Zero", "Sprite"]
crisps = ["Pringles", "Doritos"]
chocolate = ["Snickers", "Mars", "M & Ms"]

while True:
    choice = input("Would you like a SODA, some CRISPS or CHOCOLATE?\n").lower()
    try:
        if choice == 'soda':
            snack = sodas.pop()
        elif choice == 'crisps':
            snack = crisps.pop()
        elif choice == 'chocolate':
            snack = chocolate.pop()
        else:
            print("Sorry I didn't understand that...")
            continue
        print("Here's your {}: {}.".format(choice, snack))
    except IndexError:
        print("We're all out of {}, sorry!".format(choice))
