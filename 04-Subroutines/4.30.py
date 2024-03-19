def f(number):
    sum = 0
    for digit in number:
        if digit%2==0 and number%2==0:
           sum +=digit
        if digit%2==1 and number%2==1:
            sum+=digit
    return sum
    
if __name__ == "__main__":
    f("3124")