'''
A text contains any number of words. Define a function f(name) that returns the acronym (first letters of all words). Sample result:
f("Internet of Things") returns "IoT"
f("For Your Information") returns "FYI"
f("Python") returns "P"
'''

def f(name):
    acronym= ""
    for word in name:
        print(word)
        acronym += word[0].upper()
    return acronym

print(f("For Your Information"))