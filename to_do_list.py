# create empty list
to_do_list = []

# print out instructions on how to use the app
print("What do you need to do today?")
print("Enter 'DONE' to stop adding items to your to do list.")

while True:
    #ask for new items
    new_item = input("> ")
    # enter the word DONE to quit the app
    if new_item == 'DONE':
        break
    # add new item to the list
    else:
        to_do_list.append(new_item)

# show user everything that's on the list
print("Here's your list: ")
for item in to_do_list:
    print(item)
