import pytest
from RefactorCode import Book, Library


@pytest.fixture
def sample_library():
    lib = Library()
    lib.add_book(Book("1984", "George Orwell", 1949))
    lib.add_book(Book("Brave New World", "Aldous Huxley", 1932))
    return lib


# Тести для класу Book
def test_book_creation():
    book = Book("Test Title", "Test Author", 2020)
    assert book.title == "Test Title"
    assert book.author == "Test Author"
    assert book.year == 2020


def test_book_str():
    book = Book("Dune", "Frank Herbert", 1965)
    assert str(book) == "Title: Dune, Author: Frank Herbert, Year: 1965"


# Тести для класу Library
def test_add_book(sample_library):
    book = Book("Fahrenheit 451", "Ray Bradbury", 1953)
    sample_library.add_book(book)
    assert "Fahrenheit 451" in sample_library._Library__books


def test_add_duplicate_book(sample_library, capsys):
    book = Book("1984", "George Orwell", 1949)
    sample_library.add_book(book)
    captured = capsys.readouterr()
    assert "Book '1984' already exists!" in captured.out


def test_remove_book(sample_library):
    sample_library.remove_book("1984")
    assert "1984" not in sample_library._Library__books


def test_remove_nonexistent_book(sample_library, capsys):
    sample_library.remove_book("Nonexistent Book")
    captured = capsys.readouterr()
    assert "Book 'Nonexistent Book' not found!" in captured.out


def test_search_existing_book(sample_library, capsys):
    sample_library.search_book("1984")
    captured = capsys.readouterr()
    assert "Title: 1984, Author: George Orwell, Year: 1949" in captured.out


def test_search_nonexistent_book(sample_library, capsys):
    sample_library.search_book("Random Book")
    captured = capsys.readouterr()
    assert "No books found matching 'Random Book'" in captured.out


def test_display_books(sample_library, capsys):
    sample_library.display_books()
    captured = capsys.readouterr()
    assert "Books in the library:" in captured.out
    assert "1984" in captured.out
    assert "Brave New World" in captured.out


def test_display_empty_library(capsys):
    lib = Library()
    lib.display_books()
    captured = capsys.readouterr()
    assert "No books available in the library." in captured.out


def test_update_existing_book(sample_library):
    sample_library.update_book("1984", "Nineteen Eighty-Four", "George Orwell", 1949)
    assert "Nineteen Eighty-Four" in sample_library._Library__books
    assert "1984" not in sample_library._Library__books


def test_update_nonexistent_book(sample_library, capsys):
    sample_library.update_book("Unknown Book", "New Title", "New Author", 2000)
    captured = capsys.readouterr()
    assert "Book 'Unknown Book' not found!" in captured.out


# Додаткові негативні тести
@pytest.mark.parametrize("title,author,year", [
    ("", "Author", 2000),
    ("Title", "", 2000),
    ("Title", "Author", -1),
])
def test_invalid_book_creation(title, author, year):
    book = Book(title, author, year)
    assert book.title == title
    assert book.author == author
    assert book.year == year


@pytest.mark.parametrize("query,expected", [
    ("1984", "Title: 1984, Author: George Orwell, Year: 1949"),
    ("Brave", "Title: Brave New World, Author: Aldous Huxley, Year: 1932"),
    ("Nonexistent", "No books found matching 'Nonexistent'"),
])
def test_search_various_books(sample_library, capsys, query, expected):
    sample_library.search_book(query)
    captured = capsys.readouterr()
    assert expected in captured.out
