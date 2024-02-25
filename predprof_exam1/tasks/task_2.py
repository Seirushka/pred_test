import csv


def insertion_sort(array):
    """
    Сортировка базы данных учеников по оценке за проект методом вставки
    :param array: Исходный массив
    :return: Отсортированный массив по убыванию
    """
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if (float(array[j][-1]) if array[j][-1] != 'None' else 0) > \
                    (float(array[j - 1][-1]) if array[j - 1][-1] != 'None' else 0):
                array[j - 1], array[j] = array[j], array[j - 1]
            else:
                break
    return array


# Открывает файл
with open('../students.csv', encoding='utf-8') as file:
    reader = list(csv.reader(file, delimiter=','))[1:]

    # Сортирует массив
    insertion_sort(reader)

    # Находит первых 3-х победителей из 10 класса
    print('10 класс:')
    count = 1
    for element in reader:
        person, class_ = element[1], element[-2]
        surname, name, patronymic = person.split()
        if '10' in class_:
            if count < 4:
                print(f"{count} место: {name[0]}. {surname}")
                count += 1
            else:
                break
