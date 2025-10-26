from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    def test_add_new_book_incorrect_add_book_unsuccessful_add(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби и что делать, если ваш кот хочет вас убить')

        assert len(collector.books_genre) == 0
        
    
    @pytest.mark.parametrize('name, genre', 
                             [['Гордость и предубеждение', 'Фантастика'],
                              ['Игра престолов', 'Ужасы'],
                              ['Зеленая миля', 'Детективы'],
                              ['Ван Хельсинг', 'Мультфильмы'],
                              ['Остаться в живых', 'Комедии']])  
    def test_set_book_genre_correct_genre_success(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre
        
        
    def test_set_book_genre_incorrect_genre_unsuccess(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Мелодрама')

        assert collector.get_book_genre('Гордость и предубеждение') == ''
        
    
    def test_get_book_genre_whithout_genre_adding(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')

        assert collector.get_book_genre('Гордость и предубеждение') == ''
        
    
    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы'])    
    def test_get_books_with_specific_genre(self, genre):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', genre)
        
        assert len(collector.get_books_with_specific_genre(genre)) == 1
        
      
    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Ужасы')
        
        assert collector.get_books_genre() == collector.books_genre
        
        
    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        
        assert len(collector.get_books_for_children()) == 1
        
        
    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        collector.add_book_in_favorites('Гордость и предубеждение')
        
        assert len(collector.favorites) == 1
        
        
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        collector.add_book_in_favorites('Гордость и предубеждение')
        collector.delete_book_from_favorites('Гордость и предубеждение')
        
        assert len(collector.favorites) == 0
        
        
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        collector.add_book_in_favorites('Гордость и предубеждение')
        
        assert collector.favorites == collector.get_list_of_favorites_books()