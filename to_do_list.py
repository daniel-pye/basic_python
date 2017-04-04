# create empty list
to_do_list = []

# provide help info
def help():
    print("What do you need to do today?")
    print("""
    Enter 'SHOW' to see what's already on the list.
    Enter 'HELP' for a list of commands.
    Enter 'DONE' to stop adding items to your to do list.
    """)

# display current list if user enters SHOW command
def show():
    print("Here's your list so far: ")
    for item in to_do_list:
        print(item)

def add_to_list(new_item):
    # add new item to the list
    to_do_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(to_do_list)))

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
        if new_item == 'DONE':
            exit()
            break
        elif new_item == 'HELP':
            help()
            continue
        elif new_item == 'SHOW':
            show()
            continue
        add_to_list(new_item)

if__name__=="__main__":
    main()
