#Для определения являются ли переданные слова анаграммами, мы можем воспользоваться подходом с сортировкой букв в словах и
# и сравнением отсортированных слов. Сложность алгоритма будет O(n * m * log m), где n - количество слов,
# m - средняя длина слова.
def are_anagrams(words):
    sorted_words = [''.join(sorted(w)) for w in words]
    return len(set(sorted_words)) == 1
words = ["listen", "silent", "enlist"]
print(are_anagrams(words))
