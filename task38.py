def count_vowels(word):
    """Функция для подсчета гласных букв в слове"""
    vowels = 'аеёиоуыэюя'  # список гласных букв
    count = 0
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    return count


def check_rhythm(poem):
    """Функция для проверки ритма стихотворения"""
    words = poem.split()  # разбиваем стихотворение на слова
    syllables = []  # список количества слогов в каждой фразе
    for word in words:
        syllables.append(count_vowels(word))
    if len(set(syllables)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"


poem = input("Введите стихотворение: ")
print(check_rhythm(poem))