'''
22.	Create a program that computes the second power of each array element. Sample result:
Array: 8 2 5 1 9
2nd power: 64 4 25 1 81
'''

arr = [8,2,5,1,9]
squared_arr = [char**2 for char in arr]
print(squared_arr)

