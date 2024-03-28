def f(palindrome):
    x = len(palindrome)
    print(x)
    print(palindrome[:-1])
    # tutaj to cos nie tak??? xd
    if palindrome == palindrome[:-1]:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(f("row"))