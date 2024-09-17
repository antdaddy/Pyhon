import pickle

class Book: # родительский класс книга
    def __init__(self, title, price, pages):
        self.title = title
        self.price = price
        self.pages = pages

    def average_page_cost(self):
        try:
            return self.price / self.pages
        except ZeroDivisionError:
            print("Ошибка: количество страниц не может быть нулевым")
            return 0

    def double_price_if_programming(self):
        if self.title.lower().startswith('программирование'):
            self.price *= 2

class CustomException(Exception):
    pass

try:
    title = input("Введите название книги: ")
    price = float(input("Введите цену книги: "))
    pages = int(input("Введите количество страниц: "))

    book = Book(title, price, pages)

    average_page_cost = book.average_page_cost()
    print(f"Средняя стоимость одной страницы: {average_page_cost:.2f}")

    book.double_price_if_programming()
    print(f"Цена книги после увеличения: {book.price:.2f}")

    with open('book_data.pickle', 'wb') as file:
        pickle.dump(book, file)
        print("Данные книги сохранены в файл")

    with open('book_data.pickle', 'rb') as file:
        loaded_book = pickle.load(file)
        print(f"Данные книги из файла: {loaded_book.title}, Цена: {loaded_book.price}, Страницы: {loaded_book.pages}")

    raise CustomException("Это пользовательское исключение")

except ValueError:
    print("Ошибка: введены некорректные данные")
except FileNotFoundError:
    print("Ошибка: файл не найден")
except pickle.PickleError:
    print("Ошибка при чтении/записи файла")
except CustomException as e:
    print(f"Пользовательское исключение: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
