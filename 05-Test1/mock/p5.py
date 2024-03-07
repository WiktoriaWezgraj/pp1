def f(binary_number):
    for digit in binary_number:
        if digit not in ['0','1']:
            return False
    return True

if __name__ == "__main__":
    print(f("10001101"))
    print(f("10001a101"))