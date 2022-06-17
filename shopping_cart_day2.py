from IPython.display import clear_output

def add_item(cart, item):
    cart.append(item)

def remove_item(cart, item):
    cart.remove(item)

def show_cart(cart):
    if not cart:
        print('You currently have no items in your cart.')
    else:
        for idx, item in enumerate(set(cart)):
            print(f"{idx+1}) {item} [{cart.count(item)}]")
    print("=" * 60)

def clear_cart(cart):
    cart.clear()
    
def display_message():
    return input('Your input was invalid. Please try again. ')

def show_instructions():
    print("""Type 'add' to add an item to your cart.
Type 'remove' to remove an item from your cart.
Type 'clear' to remove all items from your cart.
Type 'quit' to quit the program.""")
    print("=" * 60)

# show_instructions()

# initial state = []
shopping_cart = []
    
while True:
    decision = input("Would you like to continue? Y/N? ").lower()
    
    if decision == 'n':
        break
    elif decision == 'y':
        # always clear the output before rendering anything else
        clear_output()
        
        # display some instructions
        show_instructions()
        
        # show the shopping_cart
        show_cart(shopping_cart)
        
        decision = input("What would you like to do? ").lower()
        
        if decision == 'quit':
            break
        elif decision == 'add':
            item_to_add = input('What item would you like to add? ').lower()
            add_item(shopping_cart, item_to_add)
        elif decision == 'remove':
            try:
                item_to_remove = input('What item would you like to remove? ').lower()
                remove_item(shopping_cart, item_to_remove)
            except ValueError as err:
                input("That item doesn't exist in your cart. Please try again. ")
        elif decision == 'clear':
            confirm = input('Are you sure? This will remove all items from your cart. Y/N? ').lower()
            if confirm == 'y':
                clear_cart(shopping_cart)
            elif confirm == 'n':
                continue
            else:
                display_message()
        else:
            display_message()
    else:
        display_message()