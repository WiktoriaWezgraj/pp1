'''
23.	An array contains numbers: -15, 8, -31, 47, -2, 19. Create a program that finds and displays the maximum and minimum number. 
'''

arr = [-15,8,-31,47,-2,19]
max = arr[0]
min = arr[0]
for num in arr:
    if num>max:
        max=num
    elif num<min:
        min=num

print(max,min)