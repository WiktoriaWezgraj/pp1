first_name = str(input('Enter first person name: '))
first_age = float(input('Enter first person age: '))
second_name = str(input('Enter second person name: '))
second_age = float(input('Enter second person age: '))
if first_age and second_age >= 18 :
    print(f'Both {first_name} and {second_name} are adults')
else:
    print(f'{first_name} and {second_name} are not adults')

