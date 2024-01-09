def number_of_letters():
    input_text = "I completely agree with you"
    calculate = lambda word: len(word)
    letters_in_words = map(calculate, input_text.split())
    print("Text:", input_text)
    print("No. of letters in words:", list(letters_in_words))

if __name__ == "__main__":
    number_of_letters()