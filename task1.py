list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел
print(sum(set(list_)))
print(len(set(list_)))
print(round(sum(set(list_)) / len(set(list_)), 5))