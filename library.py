from dataclasses import dataclass
from book import Book
from typing import List

@dataclass
class Library:
    name: str
    books: List[Book]

    def __len__(self) -> int:
        return len(self.books)

    def add_book(self, book: Book):
        self.books.append(book)

    def search_book(self, title: str) -> List[Book]:
        books = list()
        for book in self.books:
            if title in book.title:
                books.append(book)

        return books 
    
    def search_book_only_title(self, title: str) -> List[str]:
        return list(map(lambda b: b.title, self.search_book(title)))

    def search_book_by_id(self, id_: int) -> Book:
        return self.books[id_]

    def remove_book(self, title: str) -> bool:
        removed = False
        for book in self.books:
            if title == book.title:
                removed = True
                self.books.remove(book)

        return removed
