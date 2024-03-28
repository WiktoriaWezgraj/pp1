'''
12.	Create a program that calculates and displays the number of even values in the array. Use the ‘for’ loop statement.
'''

def f(arr):
    even = 0
    for num in arr:
        if num % 2 == 0:
            even += 1

    print("Number of even values in the array:", even)

print(f([34,3,17,4,5,6]))
