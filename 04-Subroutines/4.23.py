def f(sentence, letter):
    count = 0
    for i in sentence:
        if i == letter:
            count += 1  
    print(f"The number of letter '{letter}' is {count}")
  

if __name__ == "__main__":
    f("You never get a second chance to make a first impression", "e")