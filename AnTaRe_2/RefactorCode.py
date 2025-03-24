def get_user_book_input():
    """Отримує інформацію про книгу від користувача."""
    title = input("Enter book title: ")
    author = input("Enter book author: ")

    while True:
        try:
            year = int(input("Enter book year: "))
            break
        except ValueError:
            print("Invalid year! Please enter a valid number.")  # Спрощення умов

    return Book(title, author, year)


class Book:
    """Клас для представлення книги."""

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class Library:
    """Клас для управління бібліотекою книг."""

    def __init__(self):
        # Інкапсуляція даних - тепер книги зберігаються у прихованому полі __books
        self.__books = {}

    def add_book(self, book):
        """Додає книгу в бібліотеку."""
        if book.title in self.__books:
            print(f"Book '{book.title}' already exists!")  # Спрощення умов
        else:
            self.__books[book.title] = book
            print(f"Book '{book.title}' added successfully!")

    def remove_book(self, title):
        """Видаляє книгу з бібліотеки."""
        if self.__books.pop(title, None):
            print(f"Book '{title}' removed successfully!")
        else:
            print(f"Book '{title}' not found!")  # Спрощення умов

    def search_book(self, query):
        """Шукає книги за частиною назви."""
        found_books = [book for title, book in self.__books.items() if query.lower() in title.lower()]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print(f"No books found matching '{query}'")  # Спрощення умов

    def display_books(self):
        """Відображає всі книги в бібліотеці."""
        if self.__books:
            print("Books in the library:")
            for book in self.__books.values():
                print(book)
        else:
            print("No books available in the library.")  # Спрощення умов

    # Вилучення дублювання коду - використано окремий метод для перевірки існування книги
    def __book_exists(self, title):
        return title in self.__books

    def update_book(self, old_title, new_title, new_author, new_year):
        """Оновлює інформацію про книгу."""
        if self.__book_exists(old_title):
            self.__books[new_title] = Book(new_title, new_author, new_year)
            del self.__books[old_title]
            print(f"Book '{old_title}' updated successfully!")
        else:
            print(f"Book '{old_title}' not found!")  # Спрощення умов


# Розбиття функцій - Меню винесено в окрему функцію
def show_menu():
    """Відображає меню програми."""
    print("\nLibrary Menu:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Update a book")
    print("6. Exit")


def main():
    """Головна функція для роботи з бібліотекою."""
    library = Library()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            book = get_user_book_input()
            library.add_book(book)
        elif choice == "2":
            title = input("Enter book title to remove: ")
            library.remove_book(title)
        elif choice == "3":
            query = input("Enter search query: ")
            library.search_book(query)
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            old_title = input("Enter the title of the book to update: ")
            new_title = input("Enter new title: ")
            new_author = input("Enter new author: ")
            while True:
                try:
                    new_year = int(input("Enter new year: "))
                    break
                except ValueError:
                    print("Invalid year! Please enter a valid number.")  # Спрощення умов

            library.update_book(old_title, new_title, new_author, new_year)
        elif choice == "6":
            print("Exiting the library system. Goodbye!")  # Спрощення умов
            break
        else:
            print("Invalid choice. Please try again.")  # Спрощення умов


if __name__ == "__main__":
    main()
