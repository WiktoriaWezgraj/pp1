'''
25.	An array contains values: 15, 8, 31, 47, 2, 19. Create a program that calculates and displays the array and the arithmetic mean of array values. Use the “while” loop statement.
'''

arr = [15, 8, 31, 47, 2, 19]

total_sum = 0
count = 0

# for num in arr
while count<len(arr):
    total_sum += arr[count]
    count += 1

mean = total_sum / count

print(f"Array: {arr} Arithmetic mean: {mean:.1f}")
