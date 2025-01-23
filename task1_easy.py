import re

# Ввод текста
text = open("file1.txt", "r")

# Регулярное выражение для извлечения слов
words = re.findall(r'\b[a-zA-Zа-яА-ЯёЁ]+\b', text)

# Множество для хранения уникальных слов длиной 1, 2 или 3
unique_words = set()

# Проходим по всем словам
for word in words:
    # Приводим слово к нижнему регистру и проверяем длину
    if 1 <= len(word) <= 3:
        unique_words.add(word.lower())  # добавляем слово в множество (уникальные слова)

# Сортируем множество слов в алфавитном порядке
sorted_words = sorted(unique_words)

# Выводим результаты
print(len(sorted_words))
for word in sorted_words:
    print(word)
