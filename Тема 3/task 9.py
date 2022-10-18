salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
need_money = spend - salary
# TODO Оформить решение
for i in range(1, 10):
    i = spend * increase + spend - salary
    spend = spend * increase + spend
    need_money += i
print(round(need_money))
