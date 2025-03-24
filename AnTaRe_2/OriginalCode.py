class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully!")

    def remove_book(self, title):
        found = False
        for i, book in enumerate(self.books):
            if book.title == title:
                del self.books[i]
                print(f"Book '{title}' removed successfully!")
                found = True
                break
        if not found:
            print(f"Book '{title}' not found!")

    def search_book(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print(f"No books found with title containing '{title}'")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)

    def update_book(self, old_title, new_title, new_author, new_year):
        found = False
        for book in self.books:
            if book.title == old_title:
                book.title = new_title
                book.author = new_author
                book.year = new_year
                print(f"Book '{old_title}' updated successfully!")
                found = True
                break
        if not found:
            print(f"Book '{old_title}' not found!")


def show_menu():
    print("\nLibrary Menu:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Update a book")
    print("6. Exit")


def main():
    library = Library()

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            year = int(input("Enter the year of publication: "))
            book = Book(title, author, year)
            library.add_book(book)

        elif choice == '2':
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)

        elif choice == '3':
            title = input("Enter part or full title to search: ")
            library.search_book(title)

        elif choice == '4':
            library.display_books()

        elif choice == '5':
            old_title = input("Enter the title of the book to update: ")
            new_title = input("Enter the new title: ")
            new_author = input("Enter the new author: ")
            new_year = int(input("Enter the new year of publication: "))
            library.update_book(old_title, new_title, new_author, new_year)

        elif choice == '6':
            print("Exiting the library system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
