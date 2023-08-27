my_name = input('Your name: ')
my_age = input('Your age: ') 

print(f"My name is {my_name} and I'm {my_age} years old")

first_number = int(input('First number: '))
second_number = int(input('Second number: '))
operation = input('Type in the operation: ')

if operation == '/':
    print(first_number / second_number)
elif operation == '*':
    print(first_number * second_number)
elif operation == '+':
    print(first_number + second_number)
elif operation == '-':
    print(first_number - second_number)
else:
    print('The operation is not valid')


bus_capacity = 20
people_inbus = int(input('Enter how many people are in the bus: '))
going_inbus = int(input('Enter how many people want to enter the bus: '))
empty_seats = bus_capacity - people_inbus

if empty_seats >= going_inbus:
    print('There are empty seats')
elif empty_seats < going_inbus:
    print('The bus is full')
