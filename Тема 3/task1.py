src = not False and True or False and not True

# TODO расписать упрощение выражения
# not False = True, Следовательно первая часть выражения True and True = True
# not True = False, Следовательно вторая часть выражения False and False = False
# Итоговый результат будет True or False = True


result = True  # TODO подставить результат выражения

print(src == result)
