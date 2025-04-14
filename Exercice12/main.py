class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Le livre {book.title} a été ajouté avec succès !")

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print(f"Le livre {book_title} a été supprimé avec succès !")

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrow_books.append(book)
                print(f"Le livre {book_title} a été emprunté avec succès !")
                return
        print(f"Le livre {book_title} n'est pas disponible !")
    
    def return_book(self, book_title):
        for book in self.borrow_books:
            if book.title == book_title:
                self.borrow_books.remove(book)
                self.books.append(book)
                print(f"Le livre {book_title} a été retourné avec succès !")
                return
        print(f"Le livre {book_title} n'a pas été emprunté !")
    
    def available_books(self):
        print("\nListe des livres disponibles :")
        for book in self.books:
            print(f"Titre: {book.title}, Auteur: {book.author}, Année: {book.year}")

    def borrowed_books(self):
        print("\nListe des livres empruntés :")
        for book in self.borrow_books:
            print(f"Titre: {book.title}, Auteur: {book.author}, Année: {book.year}")
