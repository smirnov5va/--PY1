def delete(list_, index=None):
    if index is not None:
        list_1 = list_[:index] + list_[index + 1:]
        return list_1
    elif index is None:
        list_2 = list_[:-1]
        return list_2
    return list_

        # TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
