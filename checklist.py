checklist = list()

checklist.append("Hello")
print(checklist)
checklist.append("World")
print(checklist)

def create(item):
    checklist.append(item)
#print(checklist[0])

def read(index):
    return checklist[int(index)]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(int(index))

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    completed_item = checklist[index]
    checklist.insert(int(index), "√ " + completed_item)
    checklist.remove(completed_item)

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):
#Creates new list item by appending
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
#Reads list item
    elif function_code == "R":
        item_index = user_input("Index Number?")
        print(read(item_index))
#Lists all items in checklist
    elif function_code == "P":
        list_all_items()
#Updates item in checklist[index]. Returns list
    elif function_code == "U":
        list_all_items()
        item_index = user_input("Update which item #?")
        item_change = user_input("Update to what?")
        update(int(item_index), item_change)
        list_all_items()
#Marks item in checklist[index] as √ . Returns list
###To-fix. Above function NOT done correctly.
    elif function_code == "M":
        list_all_items()
        item_index = int(user_input("Which do you want to mark completed?"))
        mark_completed(item_index)
        list_all_items()
#Removes/destroys item in checklist[index]. Returns list
    elif function_code == "D":
        list_all_items()
        item_index = user_input("What item # do you want to destroy?")
        destroy(item_index)
        list_all_items()
#Quit function
    elif function_code == "Q":
        return False
    else:
        print("Unknown Option")
    return True

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))

    #select("C")

    list_all_items()

    #select("R")

    list_all_items()

test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, U to Update item, P to display list, D to Destroy an item, M to mark completed, and Q to quit\n")
    running = select(selection.upper())


"""
def my_fun_function(say_this):
    print(say_this)

my_fun_function("Hello World")

print(checklist())


print("Hello World")

checklist = list()
"""
