import csv


def generate_hash_id(person):
    """
    Генерирует хэш ученика на основе его ФИО
    :param person: ФИО ученика
    :return: Хэш ученика
    """
    alphabet = ''.join(sorted('йцукенгшщзхъфывапролджэячсмитьбю'))
    alphabet = alphabet[:6] + 'ё' + alphabet[6:]
    alphabet += alphabet.upper() + ' '

    hash_alphabet = {letter: number for number, letter in enumerate(alphabet, 1)}

    p = 67
    p_row = 1
    m = 10 ** 9 + 9

    hash_value = 0
    for element in person:
        hash_value = (hash_value + hash_alphabet[element] * p_row) % m
        p_row = (p_row * p) % m

    return int(hash_value)


# Список для обновленной базы данных
new_data = []

# Открывает файл
with open('../students.csv', encoding='utf-8') as file:
    reader = list(csv.reader(file, delimiter=','))[1:]

    # Генерирует хэш учеников и добавляет обновленные строки в новую базу данных
    for line in reader:
        hash_id = generate_hash_id(line[1])

        line = line[1:]
        new_line = [str(hash_id)] + line
        new_data.append(new_line)

# Создает новый файл с обновленной базой данных
with open('students_with_hash.csv', 'w', newline='', encoding='utf-8') as file:
    file = csv.writer(file, delimiter=',')
    file.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])
    file.writerows(new_data)
