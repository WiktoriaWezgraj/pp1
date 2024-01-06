class University():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name + " is the best!"

university = University("UEK")
print(university)
