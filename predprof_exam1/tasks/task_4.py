import csv
from random import choice, shuffle


def generate_login(person):
    """
    Генерирует логин пользователя
    :param person: ФИО пользователя
    :return: Логин вида: "Соколов_ИИ"
    """
    surname, name, patronymic = person.split()
    return f"{surname}_{name[0]}{patronymic[0]}"


def generate_password():
    """
    Генерирует случайный пароль из заглавных, строчных буквы английского алфавита и цифр
    :return: Пароль длиной в 8 симфолов
    """
    alphabet1 = 'qwertyuiopasdfghjklzxcvbnm'
    alphabet2 = alphabet1.upper()
    alphabet3 = '0123456789'
    all_alphabet = alphabet1 + alphabet2 + alphabet3

    password = [choice(alphabet1), choice(alphabet2), choice(alphabet3)]
    password += [choice(all_alphabet) for _ in range(5)]
    shuffle(password)
    return ''.join(password)


# Список для обновленной базы данных
new_data = []

# Открывает файл
with open('../students.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter=','))[1:]

    # Добаляет в каждую строку файла логин и пароль в конце
    for line in reader:
        line.append(generate_login(line[1]))
        line.append(generate_password())
        new_data.append(line)

# Создает новый файл с обновленной базой данных
with open('students_password.csv', 'w', newline='', encoding='utf8') as file:
    file = csv.writer(file, delimiter=',')
    file.writerow(['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password'])
    file.writerows(new_data)
