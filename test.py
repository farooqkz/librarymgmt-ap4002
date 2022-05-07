from book import Book
from library import Library
from os import listdir, chdir

lib = Library(name="AP4002", books=[])

chdir("/home/farooqkz/blib/Math/")
for file in filter(lambda f: f.endswith(".pdf"), listdir(".")):
    lib.add_book(Book.from_file(file))

print(lib.search_book_only_title("A"))
