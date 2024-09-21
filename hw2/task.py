# Создание пустого списка для хранения участников спора
participants = []

# Заполнение данных для 3-х участников
for i in range(3):
    print (f"Введите информацию об участнике {i + 1}:")
    name = input("Наименование: ")
    status = input("Статус: ")
    inn = input ("ИНН: ")

    # Создание словаря с информацией об участнике и добавление его в списки
    participants_info = {"name": name, "status": status, "inn": inn}
    participants.append(participants_info)

# Вывод полученных данных на консоль
print ("Участники спора:")
for participants in participants:
    print(participants)
