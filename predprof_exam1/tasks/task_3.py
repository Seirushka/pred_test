import csv

# Открываеть файл
with open('../students.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter=','))[1:]

    # Ввод id проекта
    project_id = input()

    # Поиск проектов пока пользователь не введет "СТОП"
    while project_id != 'СТОП':
        for id_, student, titleProject_id, class_, score in reader:
            if project_id == titleProject_id:
                surname, name, patronymic = student.split()
                print(f"Проект № {titleProject_id} делал: {name[0]}. {surname}")
                break
        else:
            print('Ничего не найдено')
        project_id = input()
