
class Book: # родительский класс книга
    def __init__(self, title, price, pages):
        self.title = title
        self.price = price
        self.pages = pages

    def average_page_cost(self):
        return self.price / self.pages

    def double_price_if_programming(self):
        if self.title.startswith('Программирование'):
            self.price *= 2


class ProgrammingBook(Book):
    def __init__(self, title, price, pages, language):
        super().__init__(title, price, pages)
        self.language = language


class AnotherBook(Book):
    def __init__(self, title, price, pages, genre):
        super().__init__(title, price, pages)
        self.genre = genre


book1 = ProgrammingBook('Программирование на Python', 100, 300, 'Python')
book2 = AnotherBook('Повесть', 50, 300, 'Роман')

print(book1.average_page_cost())  # вывод средней стоимости одной страницы
book1.double_price_if_programming()  # увеличение цены х2  начинается с "Программирование"
print(book1.price) # вывод цены книги "программирование"
print(book2.average_page_cost())  # вывод средней стоимости одной страницы книги "Повесть"
print(book2.price) # вывод цены книги "Повесть"

