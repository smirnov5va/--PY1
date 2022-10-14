x = 1
y = -1

# TODO переписать через if-elif-else
if x and y > 0:
    print("Первая четверть")
elif x > 0 and y < 0:
    print("Четвертая четверть")
elif x < 0 and y > 0:
    print("Вторая четверть")
else:
    print("Третья четверть")
