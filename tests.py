import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        assert len(collector.get_books_genre()) == 2


    @pytest.mark.parametrize('name, added', [['A', True], ['A'*40, True], ['', False], ['A'*41, False]])
    def test_add_new_book_various_name(self, collector, name, added):
        collector.add_new_book(name)
        assert (name in collector.get_books_genre()) == added

    def test_set_book_genre_valid_invalid_pairs(self, collector):
        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Мультфильмы')
        assert collector.get_book_genre('Колобок')=='Мультфильмы'

    def test_get_book_genre_existing_book(self,collector):
        collector.books_genre["Гарри Поттер"] = "Фантастика"
        result = collector.get_book_genre("Гарри Поттер")
        assert result == "Фантастика"

    def test_get_books_with_specific_genre_choice(self, collector):
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.add_new_book("Книга3")

        collector.set_book_genre("Книга1", "Ужасы")
        collector.set_book_genre("Книга2", "Ужасы")
        collector.set_book_genre("Книга3", "Комедии")

        result = collector.get_books_with_specific_genre("Ужасы")

        assert result == ['Книга1', 'Книга2']

    def test_get_books_genre_return_dict(self, collector):
        collector.add_new_book("Касл")
        collector.set_book_genre("Касл", "Детективы")
        books_diction = collector.get_books_genre()
        assert books_diction == {"Касл": "Детективы"}

    def test_get_books_genre_when_return_empty_dict(self, collector):
        books_diction = collector.get_books_genre()
        assert books_diction == {}

    def test_get_books_for_children_control_child(self, collector):
        collector.add_new_book("Три кота")
        collector.add_new_book("Дом у озера")
        collector.set_book_genre("Три кота", "Мультфильмы")  
        collector.set_book_genre("Дом у озера", "Ужасы")         

        child = collector.get_books_for_children()
        assert "Три кота" in child

    def test_add_book_in_favorites_added(self, collector):
        collector.add_new_book('Книга1')
        collector.add_book_in_favorites("Книга1")
        fan = collector.get_list_of_favorites_books()
        assert "Книга1" in fan

    def test_delete_book_from_favorites_from_fav(self, collector):
        collector.add_new_book("Книга2")
        collector.add_book_in_favorites("Книга2")
        collector.delete_book_from_favorites("Книга2")
        assert "Книга2" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_no_books(self, collector):
        favorites = collector.get_list_of_favorites_books()
        assert favorites == []

    def test_get_list_of_favorites_books_with_books(self, collector):
        collector.add_new_book("Книга3")
        collector.add_book_in_favorites("Книга3")
        fan = collector.get_list_of_favorites_books()
        assert fan == ['Книга3']