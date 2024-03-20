def popular_words(text, words):
    # Розбиваємо текст на слова за пробілами та переводимо всі слова в нижній регістр
    word_list = text.lower().split()

    # Ініціалізуємо словник для зберігання кількості зустрічей кожного слова
    word_count = {}

    # Перебираємо слова, які потрібно знайти
    for word in words:
        # Визначаємо кількість зустрічей слова у тексті та додаємо у словник
        word_count[word] = word_list.count(word)

    return word_count


# Тестуємо функцію
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')