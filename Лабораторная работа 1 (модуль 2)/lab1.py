# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Capybara:
    def __init__(self, age: float, weight: float):
        """
        Создание и подготовка к работе объекта "Капибара"

        :param age: возраст капибары
        :param weight: вес капибары

        Примеры:
        >>> capybara = Capybara(5, 40)  # инициализация экземпляра класса
        """
        if not isinstance(age, (int, float)):
            raise TypeError("Возраст капибары должен быть типа int или float")
        if age <= 0:
            raise ValueError("Возраст капибары должен быть положительным числом")
        self.age = age

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес капибары должен быть int или float")
        if weight < 0:
            raise ValueError("Вес капибары не может быть отрицательным числом")
        self.weight = weight

    def buy_tangerines_for_capybara(self, bought_tangerines: int) -> None:
        """
        Покупка мандаринов для капибары

        :param bought_tangerines: количество купленных мандаринов
        :return: количество купленных мандаринов

        Примеры:
        >>> capybara = Capybara(5, 40)
        >>> capybara.buy_tangerines_for_capybara(15)
        """
        ...

    def feed_capybara_tangerines(self, estimate_tangerines: int) -> None:
        """
        Функция, которая показывает, сколькими мандаринами накормили капибару
        :param estimate_tangerines: Количество мандаринов, которые съела капибара
        :return: Сколько мандаринов съела капибара
        :raise ValueError: Если количество мандаринов отрицательно, то вызываем ошибку
        :raise ValueError: Если количество съеденных мандаринов превышает количество купленных,
        то возвращается ошибка.

        Примеры:
        >>> capybara = Capybara(5, 40)
        >>> capybara.feed_capybara_tangerines(7)
        """
        ...

    def capybara_babies(self, babies: int) -> None:
        """
        Сколько капибарят родила капибара
        :param babies: Количество детенышей капибары
        :raise ValueError: Если количество детенышей превышает 8, то вызываем ошибку

        Примеры:
        >>> capybara = Capybara(5, 40)
        >>> capybara.capybara_babies(3)
        """
        if not isinstance(babies, int):
            raise TypeError("Количество детенышей должно быть типа int")
        if babies > 8:
            raise ValueError("Количество детенышей капибары не превышает 8")
        ...




if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


class Social_media_account:
    def __init__(self, followers: int, following: int):
        """
        Создание и подготовка к работе объекта "Аккаунт в социальной сети"

        :param followers: подписчики
        :param following: подписки

        Примеры:
        >>> social_media_account = Social_media_account(1000, 500)  # инициализация экземпляра класса
        """
        if not isinstance(followers, (int)):
            raise TypeError("Количество подписчиков должно быть типа int")
        if followers < 0:
            raise ValueError("Количество подписчиков должно быть положительным числом")
        self.followers = followers

        if not isinstance(following, int):
            raise TypeError("Количество подписок должно быть int")
        if following < 0:
            raise ValueError("Количество подписок не может быть отрицательным числом")
        self.following = following

    def unfollow(self, unfollows: int) -> None:
        """
        Сколько человек отписалось от аккаунта

        :param unfollows: количество отписок
        :raise ValueError: Если количество отписок превышает количество подписчиков, то вызываем ошибку


        Примеры:
        >>> social_media_account = Social_media_account(1000, 500)
        >>> social_media_account.unfollow(38)
        """
        if unfollows > 1000:
            raise ValueError("Количество отписок не может быть больше числа подписчиков")
        ...

    def likes(self, posts_likes: int) -> None:
        """
        Функция, которая показывает, сколько лайков собрали посты в аккаунте за сутки
        :param posts_likes: количество лайков
        :return: Сколько лайков собрали посты в аккаунте

        Примеры:
        >>> social_media_account = social_media_account(1000, 500)
        >>> social_media_account.likes(250)
        """
        ...



if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


class Book_shop:
    def __init__(self, books: int, clients_a_day: int):
        """
        Создание и подготовка к работе объекта "Книжный магазин"

        :param books: количество книг в магазине
        :param clients_a_day: количество посетителей магазина за день

        Примеры:
        >>> book_shop = Book_shop(5000, 300)  # инициализация экземпляра класса
        """
        if not isinstance(books, (int)):
            raise TypeError("Количество книг должно быть типа int")
        if books < 0:
            raise ValueError("Количество книг должно быть положительным числом")
        self.books = books

        if not isinstance(clients_a_day, (int)):
            raise TypeError("Количество посетителей должно быть типа int")
        if clients_a_day < 0:
            raise ValueError("Количество клиентов не может быть отрицательным числом")
        self.clients_a_day = clients_a_day

    def sold_books(self, sold_books_in_a_day: int) -> None:
        """
        Сколько книг продано за день

        :param sold_books_in_a_day: количество проданных книг
        :raise ValueError: Если количество проданных книг превышает количество книг в магазине, то вызываем ошибку


        Примеры:
        >>> book_shop = Book_shop(5000, 300)
        >>> book_shop.sold_books(17)
        """
        if sold_books_in_a_day > 5000:
            raise ValueError("Количество проданных книг не может быть больше числа книг в магазине")
        ...

    def book_purchase(self, purchased_books: int) -> None:
        """
        сколько книг закупили в магазин для продажи
        :param purchased_books: количество закупленных книг
        :return: на сколько книг пополнился ассортимент

        Примеры:
        >>> book_shop = Book_shop(5000, 300)
        >>> book_shop.book_purchase(383)
        """
        ...
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
