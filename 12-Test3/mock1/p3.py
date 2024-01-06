'''''
(p3.py) The uid array contains user IDs in one of the popular websites. Identifiers should be unique. Create a function f(uid) that returns true if all ids are unique. Otherwise, the function returns false. Example:

f(["john5","ann123","JOHN5","xxx","abc333","a10"]) 🡪 True
f(["abc123","ann","abc123","a10"]) 🡪 False
f(["bob2","bob2"]) 🡪 False
f(["bob2","BOB2"]) 🡪 True
'''''

def f(uid):
    for i in range(len(uid)):
        for j in range (i+1, len(uid)):
            if uid[i] == uid[j]:
                return False
    return True

if __name__ == "__main__":
    print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
    print(f(["abc123","ann","abc123","a10"]))