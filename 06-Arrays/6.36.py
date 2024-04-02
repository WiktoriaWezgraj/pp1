'''
36.	Write a program that counts the number of occurrences of any value from a tuple. Sample result:
Tuple: 50,20,40,50,30,50
Value: 50
Number of occurrences: 3
'''
def get_count(tuple):
    value = int(input("Value:"))
    count = 0
    for char in tuple:
        if char == value:
            count +=1
    return count

print(get_count((50,20,40,50,30,50)))

