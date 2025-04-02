from practice_uploading.workshop_6_leos.book import inventory


class Book:
    def __init__(self, title:str, author:str, isbn:str, price:int, stock:int):
        self.title = title
        self.author = author
        self._isbn = isbn
        self.price = price
        self.stock = stock

    def get_book_info(self):
        return f'"{self.title}" by {self.author}, isbn is  {self._isbn}, price is {self.price}, stock is {self.stock}'

    def display_info(self):
        print(self.get_book_info())

    def add_stock(self, amount_to_add):
        if not self.check_amount(amount_to_add):
            print('Please input correct amount')
            return
        self.stock += amount_to_add
        print(f'Stock of "{self.title}" is {self.stock}')

    def sell_book(self, amount_sold):
        if not self.check_amount(amount_sold):
            print('Please input correct amount')
            return
        if self.stock < amount_sold:
            print('Inventory is not enough.')
        else:
            self.stock -= amount_sold
            print(f'current inventory is {self.stock} ')

    # check if input amount is valid
    def check_amount(amount):
        if amount > 0:
            return True
        else:
            return False

book1 = Book("Harry Potter","JK Rowling",'1338878921',30,28)
book1.display_info()
book1.sell_book(26)
book1.sell_book(27)
book1.add_stock(3)
book1.display_info()
print('\n------I am the divider------\n')

class EBook(Book):
    def __init__(self, title, author, isbn, price, stock, file_format:str):
        super().__init__(title, author, isbn, price, stock)
        self.file_format = file_format

    def display_info(self):
        print(f'{super().get_book_info()}, file format is {self.file_format}')

book2 = EBook("The Da Vinci Code", "Dan Brown", '13388789532', 30,30,'PDF')
book2.display_info()
book2.sell_book(26)
book2.add_stock(3)
book2.display_info()
print('\n------I am the divider------\n')

class Inventory:
    def __init__(self, books=[]):
        self.books = books

    def add_book(self, book):
        if not self.check_book(book):
            return
        if book in self.books:
            print('This book is already in the inventory.')
        else:
            self.books.append(book)
            print('This book has been added to the inventory.')

    # Assume that we pass an instance of Book class. We can also use isbn as argument, then use for loop to find book we want to remove.
    def remove_book(self, book):
        if not self.check_book(book):
            return
        if book not in self.books:
            print('Please add the book to the inventory first.')
        else:
            # each book object should be unique
            self.books.remove(book)
            print(f"'{book.title}'( isbn: {book._isbn}) has been removed from inventory.")

    #display all books that matched input title
    def find_book_by_title(self, book_title):
        isfound = False
        found_books = ''
        i = 0
        for book in self.books:
            if book_title == book.title:
                i += 1
                found_books += f'\n\t{i}. {book.get_book_info()}'
                isfound = True
        if isfound:
            print('We have found following books:', end='')
            print(found_books)
        else:
            print("Didn't find book in inventory")

    def display_inventory(self):
        inventory = []
        for book in self.books:
            book = {"Book": book.title, "Inventory": book.stock, "E-Book": self.check_ebook(book)}
            inventory.append(book)
        print(inventory)


    # check if book is an instance of Book class
    @staticmethod
    def check_book(book):
        if isinstance(book, Book):
            return True
        else:
            print('This is not a book')
            return False

    # check if book is an instance of EBook class
    @staticmethod
    def check_ebook(book):
        if isinstance(book, EBook):
            return True
        else:
            return False


inventory1 = Inventory()
inventory1.add_book(book1)
inventory1.add_book(book2)
inventory1.display_inventory()

# test if stock changes are also reflected in inventory
book1.add_stock(20)
inventory1.display_inventory()

# test remove
inventory1.remove_book(book2)
inventory1.display_inventory()
inventory1.remove_book(book2)

print('\n------I am the divider------\n')
inventory1.find_book_by_title('niaiwo') # no such book in inventory
inventory1.find_book_by_title('Harry Potter')