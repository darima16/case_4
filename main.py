"""Case-study #4 Анализ текста
Developers:
Zhambaeva D.(80%), Zikova K.(40%)
.

"""

text = input("Введите текст:")
count_sentens = text.count('.') + text.count('?') + text.count('!')
count_words = text.count(' ') + text.count(',')
text = text.lower()
count_syllables = text.count('а') + text.count('о') + text.count('и') \
                  + text.count('е') + text.count('ё') + text.count('э') \
                  + text.count('ы') + text.count('у') + text.count('ю') \
                  + text.count('я')

ASL = count_words / count_sentens
ASW = count_syllables / count_words
FRE = 206.835 - (1.3 * ASL) - (60.1 * ASW)


print('Предложений:', count_sentens)
print ('Слов:',count_words)
print ('Слогов:',count_syllables)
print ('Средняя длина предложения в словах:',ASL)
print ('Средняя длина слова в слогах:',ASW)
print ('Индекс удобочитаемости Флеша:',FRE)
if FRE <= 25:
    print('Текст трудно читается (для выпускников ВУЗов).')
if FRE > 25:
    print('Текст немного трудно читать (для студентов).')
if FRE > 50:
    print('Простой текст (для школьников).')
if FRE > 80:
    print('Текст очень легко читается (для младших школьников).')
