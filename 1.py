def f(sentence):

    vowels = 'АЕЁИОУЫЭЮЯаеёиоуыэюя'
    consonants = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩбвгджзйклмнпрстфхцчшщ'

    vowel_count = 0
    consonant_count = 0

    for char in sentence.lower():
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    print(f"Гласных: {vowel_count}")
    print(f"Согласных: {consonant_count}")

sentence = input('Введите предложение: ')
f(sentence)

