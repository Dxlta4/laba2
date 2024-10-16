print(Пример лямбда функции)

def book_list(books, func):
    for book in books:
        print(func(book))

books = ['The Witcher','Lords Of The Rings','Metro:2033']
book_list(books, lambda book: book.upper() + ' - read')

