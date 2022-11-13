from random import randint
def get_unique_list_numbers() -> list[int]:
    start = -10
    stop = 10
    count_ = 15
    return set([randint(start, stop) for i in range(count_)])  # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
