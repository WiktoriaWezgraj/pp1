class Ebook():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.is_open = True

    def open(self):
        self.is_open =  True

    def close(self):
        self.is_open = False

    def change_page(self, pages_read):
        self.pages_read = pages_read
        if self.is_open == True:
            print(f"I am reading a book. I've read {pages_read} pages.")
        else:
            print("You didn't open a book.")

    def show_status(self):
        if self.is_open == True:
            print("Book is opened.")
        else:
            print("Book is closed.")


ebook = Ebook("Why we sleep", "Matthew Walker", 350)
ebook.open()
ebook.show_status()
ebook.change_page(89)
ebook.close()
ebook.show_status()
ebook.change_page(7)