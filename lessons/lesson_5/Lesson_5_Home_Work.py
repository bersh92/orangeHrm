# Beginner Python Homework: Introduction to Basics

def print_hello_world():
    """Task 1: Print 'Hello, World!' to the console."""
    print('\nHello, World!')

def create_and_print_variables():
    """Task 2: Create two variables, `greeting` with any text and `number` with any number, then print both."""
    print('\ncreate_and_print_variables():')
    number_doc = 256
    def greet(Document):
        return 'Document', number_doc
    greeting = greet("Python Programmer")
    print(greeting)

def sum_two_numbers():
    """Task 3: Create two variables with numbers and print their sum."""
    print('\nSum_two_numbers:')
    variab_1 = 2
    variab_2 = 3
    print(variab_1 + variab_2)


def greet_user():
    """Task 4: Use the input() function to ask the user for their name and greet them.пнглгш"""
    print('\ngreet_user():')
    def greet(name):
        return "Hello, " + name + "!"
    greeting = greet("Python Programmer")
    print(greeting)

def create_list():
    """Task 5: Create a list named `fruits` with any three fruits and print the list."""
    print("\ncreate_list():")
    a_list = ["Apple", "Pear", "Mango"]
    print("Fruits:", a_list)

def add_fruit_to_list(fruits):
    """Task 6: Add another fruit to the `fruits` list and print the updated list."""
    a_list = ["Apple", "Pear", "Mango"]
    a_list.append("Orange")
    print("Updated List Fruits:", a_list)


def print_fruits(fruits):
    """Task 7: Print each fruit in the `fruits` list using a loop."""
    print("For Loop Range(5):")
    for i in range(5): #не понимаю что нужно получить на выходе (с фруктами)
        print(i)


def create_and_print_dictionary():
    """Task 8: Create a dictionary named `person` with keys 'name' and 'age', then print the dictionary."""
    # Your code here
    print("\ncreate_and_print_dictionary():")
    d = {
        'Max' : 23,
        'Viktor': 25,
        'Maria': 32
    }
    print(d)
def update_age_in_dictionary(person):
    """Task 9: Update the 'age' in the `person` dictionary to a new value and print the updated dictionary."""
    print("\nupdate_age_in_dictionary(person):")
    d = {
        'Max': 23,
        'Viktor': 25,
        'Maria': 32
    }
    print(d)
    d['Anna'] = 18
    print (d)


def check_number_greater_than_10():
    """Task 10: Check if a number stored in a variable is greater than 10 and print a relevant message."""
    print("\nnumber_greater_than_10()")
    number = 15
    if number > 10:
        print("Relevant message")
    else:
        print("Number is 10 or less")

def main():
    # Call each function to execute the tasks
    print_hello_world()
    create_and_print_variables()
    sum_two_numbers()
    greet_user()
    fruits = create_list()
    add_fruit_to_list(fruits)
    print_fruits(fruits)
    person = create_and_print_dictionary()
    update_age_in_dictionary(person)
    check_number_greater_than_10()

if __name__ == "__main__":
    main()
