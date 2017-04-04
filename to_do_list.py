# create empty list
to_do_list = []

# print out instructions on how to use the app
print("What do you need to do today?")
print("Enter 'DONE' to stop adding items to your to do list.")
print("Enter 'SHOW' to see what's already on the list or 'HELP' for a list of commands.")

# define the help function
def help():
    print("To exit the app, enter 'DONE'. To view items already on your list, enter 'SHOW'.")

# display current list if user enters SHOW command
def show():
    print("Here's your list so far: ")
    for item in to_do_list:
        print(item)

while True:
    #ask for new items
    new_item = input("> ")
    # enter the word DONE to quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        help()
        continue
    elif new_item == 'SHOW':
        show()
        continue
    # add new item to the list
    else:
        to_do_list.append(new_item)

# show user everything that's on the list
print("Here's your list: ")
for item in to_do_list:
    print(item)
