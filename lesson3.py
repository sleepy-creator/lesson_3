file = open('text.txt', 'r', encoding='UTF-8')
text = file.read()
# 1) Очистка текста от знаков препинания;
print("Задача №1")
text_new = text.replace(',''.''?''!''-''<<''>>'';''('')','')
print(text_new,'')
# 3) Приведение текста к нижнему регистру
print("Задача №3")
text_lower = text_new.lower()
print(text_lower,'')
# 2) Формировка list со словами
print("Задача №2")
words = text_lower.split()
print(words,'')
# 3) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
print("Задача №3")
text_dict = {}
for a in range (len(words)):
    many = 0
    word = words[a]
    for i in range(len(words)):
        if word == words[i]:
            many = many + 1
    text_dict[word] = many
print(text_dict)
# 4) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
print("Задача №4")
sort_list=list(text_dict.items())
sort_list.sort(key = lambda i: i[1], reverse=True)
print('5 наиболее встречающихся: ', sort_list[0:5])
text_set = set(words)
print('Количество разных слов в тексте: ', len(text_set), 'слов')
