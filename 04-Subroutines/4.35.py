def f(number1,number2,operator):
    if operator == "+":
        return number1+number2
    elif operator == "%":
        return number1%number2
    elif operator == "**":
        return number1**number2
    elif operator == "*":
        return number1*number2
    elif operator == "-":
        return number1-number2
    else:
        print("Invalid operation.")

if __name__ == "__main__":
    print(f(2,3, "%")) 
    