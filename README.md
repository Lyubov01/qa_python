# qa_python
# Проект: Тестирование BooksCollector

## Описание
В проекте реализован класс `BooksCollector`, который хранит книги, их жанры и список «Избранное».  
Для проверки его работы написан набор юнит-тестов

## Фикстура
В проекте реализована фикстура в файле  **conftest.py**


## Реализованные тесты

Все тесты находятся в классе **`TestBooksCollector`**.

### 1. `add_new_book`
- `test_add_new_book_add_two_books` — проверяет, что можно добавить 2 книги.  
- `test_add_new_book_various_name` — параметризованный тест: проверка добавления книг с разной длиной названия, а также защита от дублей.

### 2. `set_book_genre`
- `test_set_book_genre_valid_invalid_pairs` — установка жанра для существующей книги, проверка корректной установки жанра.

### 3. `get_books_genre`
- `test_get_book_genre_existing_book` — проверка получения жарка книги по ее имени.
- `test_get_books_genre_return_dict` — проверка, что метод возвращает коректный словарь с книгами.  
- `test_get_books_genre_when_return_empty_dict` — если книг нет, возвращается пустой словарь.

### 4. `get_books_with_specific_genre`
- `test_get_books_with_specific_genre_choice` — фильтрация книг по жанру, проверка правильности результата.

### 5. `get_books_for_children`
- `test_get_books_for_children_control_child` — проверка, что книги с «детским» жанром попадают в список, а с «взрослым» жанром — нет.

### 6. `add_book_in_favorites`
- `test_add_book_in_favorites_added` — добавление книги в список избранного.

### 7. `delete_book_from_favorites`
- `test_delete_book_from_favorites_from_fav` — удаление книги из избранного.

### 8. `get_list_of_favorites_books`
- `test_get_list_of_favorites_books_no_books` — проверка, что при пустом избранном возвращается пустой список.  
- `test_get_list_of_favorites_books_with_books` — проверка, что при добавлении книги она появляется в списке избранного.

---

## Итого
- Покрыты все основные методы класса `BooksCollector`.  
- В тестах есть как позитивные, так и негативные сценарии.  
- Использована параметризация для проверки добавления книг с разной длиной имени
