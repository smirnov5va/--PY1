list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# TODO Оформить решение
max_index = 0
for i in range(len(list_numbers)):
    max_element = list_numbers[max_index]
    current_ = list_numbers[i]
    if current_ > max_element:
        max_index = i

list_numbers[max_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_index]
print(list_numbers)