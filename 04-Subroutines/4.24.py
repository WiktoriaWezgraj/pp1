def check_number():
    num = int(input("Enter a number: "))
    print(f"Number {num} in the range <2,15>: ")
    if num >= 2 and num <=15:
        print("yes")
    else:
        print("no")

check_number()