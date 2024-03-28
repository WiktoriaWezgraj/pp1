def f(n1,n2,n3):
    if n1 != n2 and n2 != n3 and n1 != n3:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(f(1,2,3))
    print(f(1,2,2))
    print(f(1,1,2))
    print(f(1,2,1))