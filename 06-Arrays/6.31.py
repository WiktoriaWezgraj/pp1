'''
31.	Create a program that displays all unique elements in an array. Sample result:
Array: 2 3 2 5 8 1 9 8
Unique elements: 3 5 1 9
'''

arr1 = [2,3,2,5,8,1,9,8]
arr2 = []
for char in arr1:
    if char%2==1:
        arr2.append(char)
        
print(arr2)