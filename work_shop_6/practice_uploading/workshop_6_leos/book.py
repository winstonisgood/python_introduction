class book:
   def __init__(self,title,author,isbn,price,stock):
       self.title=title
       self.author=author
       self.isbn=isbn
       self.price=price
       self.stock=stock
   def display_info(self):
       print(f" '{self.title}' by {self.author} ,isbn is  {self.isbn}  ,price is  {self.price}, stock is {self.stock}")
   def add_stock(self,add_number):
       self.stock += add_number
       print(f"current stock is {self.stock}")
   def sell_book(self,sold_number):
       self.stock -= sold_number
       print(f"current stock is {self.stock}")

my_book = book("Harry Potter","JK Rowling",1338878921,30,5000)
my_book.display_info()
my_book.add_stock(300)
my_book.sell_book(50)

class ebook(book):
    def __init__(self,title,author,isbn,price,stock,file_format):
        super().__init__(title,author,isbn,price,stock)
        self.file_format=file_format

my_ebook = ebook("Harry Potter","JK Rowling",1338878921,30,5000,"EPUB")

class inventory:
    def __init__(self):
      self.books=[]
    def add_book(self,book):
      self.books.append(book)
    def remove_book(self,title):
       for book in self.books:
          if book.title == title:
              self.books.remove(book)
              
    def find_book(self,title):
        for book in self.books:
          if book.title == title:
              print(f"{title} is found in inventory")
    
    def display_inventory(self):
        if not self.books:
            print("No books in inventory.")
        else:
            print("Inventory:")
            for book in self.books:
                print(book.display_info())
    
inventory=inventory()
    
book1 = book("To Kill a Mockingbird", "Harper Lee", 28177378,50,1000)
book2 = ebook("Digital Fortress", "Dan Brown", 3567777, 45,2000, "PDF")

inventory.add_book(book1)
inventory.add_book(book2)
inventory.display_inventory()

inventory.remove_book("To Kill a Mockingbird")
inventory.display_inventory()
inventory.find_book("Digital Fortress")
    