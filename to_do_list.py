import os

# create empty list
to_do_list = []

# clear screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# provide help info
def help():
    clear_screen()
    print("What do you need to do today?")
    print("""
    Enter 'SHOW' to see what's already on the list.
    Enter 'HELP' for a list of commands.
    Enter 'DONE' to stop adding items to your to do list.
    """)

# display current list if user enters SHOW command
def show():
    clear_screen()

    print("Here's your list so far: ")

    index = 1
    for item in to_do_list:
        print("{}. {}".format(index, item))
        index += 1

    print("="*10)

def add_to_list(item):
    show()
    if len(to_do_list):
        position = input("Where should I add {}?\n"
        "Press ENTER to add to the end of the list\n"
        "> ".format(item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        to_do_list.insert(position-1, item)
    else:
        to_do_list.append(item)
    show()

def exit():
    if len(to_do_list) == 0:
        print("You can relax!")
    else:
        print("Here's your list: ")
        for item in to_do_list:
            print(item)

def main():
    # print app instructions
    help()

    while True:
        #ask for new items
        new_item = input("> ")
        # enter the word DONE to quit the app
        if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
            exit()
            break
        elif new_item.upper() == 'HELP':
            help()
            continue
        elif new_item.upper() == 'SHOW':
            show()
            continue
        else:
            add_to_list(new_item)

if __name__=="__main__":
    main()
