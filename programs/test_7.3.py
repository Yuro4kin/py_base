


# 3. Напишите программу определения слова палиндрома
# (это слова, которые одинаково читаются в обоих направлениях,
# например, анна, abba и т.п.) Слово вводится с клавиатуры
# msgPal1 = "Anna"
# msgPal2 = "abba"
# msgPal = msgPal1.
word1 = input("Введите слово: ")
wordLower = word1.lower()
word2 = wordLower[::-1]            #  берем срез - все буквы наоборот записываются

result = wordLower > word2
res    = wordLower == word2

if(res): print("Слово Палиндрома: "+wordLower)
else:  print("Слово не Палиндрома: "+wordLower)

                                # литералы
                                # большая и маленькая буквы

    


