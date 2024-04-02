'''
24.	An array contains values: 15, 8, 31, 47, 2, 19. 
Create a program that calculates and displays the array and the arithmetic mean of array values. Use the “for” loop statement.
'''

arr = [15, 8, 31, 47, 2, 19]

count = 0
sum = 0

for char in arr:
    sum+=char
    count+=1

mean = sum/count
print(mean)