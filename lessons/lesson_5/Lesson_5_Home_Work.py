# Beginner Python Homework: Introduction to Basics

def print_hello_world():
    """Task 1: Print 'Hello, World!' to the console."""
    print("Hello, World!")

def create_and_print_variables():
    """Task 2: Create two variables, `greeting` with any text and `number` with any number, then print both."""
    greeting = "Hello"
    number = 777
    print(greeting, number)
    return number

def sum_two_numbers():
    """Task 3: Create two variables with numbers and print their sum."""
    a = 776
    b = 1
    print(a + b)

def greet_user():
    """Task 4: Use the input() function to ask the user for their name and greet them."""
    name = input("Please enter your name \n")
    print(f"Hello {name} !")

def create_list():
    """Task 5: Create a list named `fruits` with any three fruits and print the list."""
    fruits = ["apple", "banana", "coconut"]
    print(fruits)
    return fruits


def add_fruit_to_list(fruits):
    """Task 6: Add another fruit to the `fruits` list and print the updated list."""
    fruits.append("strawberry")
    print(fruits)

def print_fruits(fruits):
    """Task 7: Print each fruit in the `fruits` list using a loop."""
    for fruit in fruits:
        print(fruit)

def create_and_print_dictionary():
    """Task 8: Create a dictionary named `person` with keys 'name' and 'age', then print the dictionary."""
    person = {"name": "Alex", "age": 30 }
    print(person)
    return person

def update_age_in_dictionary(person):
    """Task 9: Update the 'age' in the `person` dictionary to a new value and print the updated dictionary."""
    person["age"] = 32
    print(person)


def check_number_greater_than_10(number):
    """Task 10: Check if a number stored in a variable is greater than 10 and print a relevant message."""
    #я тут не понял нужно было ли создать переменную внутри функции или передать ее как аргумент ?
    if number > 10:
        print("Number is greater than 10 !")
    elif number == 10:
        print("Numbers is equal 10 !")
    else:
        print("Number is less than 10 !")

def main():
    # Call each function to execute the tasks
    print_hello_world()
    number = create_and_print_variables()
    sum_two_numbers()
    greet_user()
    fruits = create_list()
    add_fruit_to_list(fruits)
    print_fruits(fruits)
    person = create_and_print_dictionary()
    update_age_in_dictionary(person)
    check_number_greater_than_10(number)

if __name__ == "__main__":
    main()
