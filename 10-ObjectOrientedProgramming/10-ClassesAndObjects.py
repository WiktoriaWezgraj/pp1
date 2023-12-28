def Class_and_object_creation():
    class Book():
        def __init__(self,title,author,pages):
            self.title = title
            self.author = author
            self.pages = pages
            self.current_page = 1
            self.is_open = True
        def open(self):
            self.is_open = True
        def close(self):
            self.is_open = False
        def change_page(self,page):
            self.current_page = page

    class Phone():
        def __init__(self, type, ram, time):
            self.type = type
            self.ram = ram
            self.time = time
            self.is_turn_on = False
        def turn_on(self):
            self.is_turn_on = True 
        def turn_off(self):
            self.is_turn_on = False
        

    phone = Phone("Samsung", 16, 15)

    book = Book("Harry Potter and the Philosopher's Stone","J. K. Rowling",223)

    print(f"My favourite book is {book.title}, ",end="")
    print(f"written by {book.author}. ",end="")
    print(f"This book has {book.pages} pages.")

    book.open()
    book.change_page(15)

    if book.is_open:
        print(f"Reading the book, page {book.current_page}")
    else:
        print("I am going to read the book later.")

    if phone.is_turn_on:
        print(f"Incoming call lasts: {phone.time}")
    else:
        print("There is no incoming call.")


def String_representation_of_object():
    class University():
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return self.name + " is the best!"

    university = University("UEK")
    print(university)



def during_class():
    String_representation_of_object()
    
def main():
    during_class()

if __name__ == "__main__":
    main()

