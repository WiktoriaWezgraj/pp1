'''''
 Assume that a valid variable name in a computer program consists of one to five characters. The first character of a variable name must be a lowercase or uppercase letter or an underscore. The remaining characters in the variable name can be uppercase or lowercase letters, digits or the underscore character. Create a function f(vname) that returns true if the variable name vname is valid. Otherwise, the function returns false. Example:

f("abc") 🡪 True
f("Abc") 🡪 True
f("aBC") 🡪 True
f("_ab_c") 🡪 True
f("abcdef") 🡪 False
f("8abc") 🡪 False
f("_aB8_") 🡪 True
f("_4x") 🡪 True
'''''

def f(vname):
    if 1 <= len(vname) <= 5:
        ...
