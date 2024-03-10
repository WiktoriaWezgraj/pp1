from mymath import generate_number
from mykeyboard import read_number
num1 = read_number()
num2 = generate_number()
print("Generated number:", num2)
if num1 == num2:
    print('You won the game!')
else:
    print('You lost the game!')