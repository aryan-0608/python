class Library:
    def __init__(self):
        self.noBook = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBook = len(self.books)

    def showInfo(self):
        print(f"The library has {self.noBook} books")
        for book in self.books:
            print(book)
l1 = Library()
l1.addBook("Python Programming")
l1.addBook("Data Structures and Algorithms")
l1.addBook("Machine Learning")
l1.showInfo()