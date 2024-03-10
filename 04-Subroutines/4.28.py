def f(binary_number):
    for digit in binary_number:
        if digit not in ['1','0']:
            return False
        return True

if __name__ == "__main__":       
    print(f("101101"))
    print(f("1311a10101"))