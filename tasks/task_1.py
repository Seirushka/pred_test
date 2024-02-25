import csv
# Открываеть файл
with open('../students.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter=','))[1:]

    count_class = {}
    sum_class = {}

    for id_, name, titleProject_id, class_, score in reader:
        # Узнает оценку Владимира за проект
        if 'Хадаров Владимир' in name:
            print(f"Ты получил: {score}, за проект - {titleProject_id}")

        # Считает средние значения по классам (None принимает за 0)
        if score != 'None':
            sum_class[class_] = sum_class.get(class_, 0) + int(score)
        count_class[class_] = count_class.get(class_, 0) + 1

# Заменяет None на средние значения по классам
    for element in reader:
        if element[-1] == 'None':
            element[-1] = round(sum_class[element[-2]] / count_class[element[-2]], 3)

# Запишем новую версию файла
with open('students_new.csv', 'w', encoding='utf8', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])
    writer.writerows(reader)
