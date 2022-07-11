import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


names = contacts_list.pop(0)
# Задание 1------------------------------------------------------------------------------------------
# поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно

pattern = r"(\w+)\s?(.*)?"
for value in contacts_list:
    result = re.sub(pattern, r"\2", value[0])
    # print(result)
    if result != '':
        value[0] = re.sub(pattern, r"\1", value[0])
        value[1] = result


    result2 = re.sub(pattern, r"\2", value[1])
    # print(result2)
    if result2 != '':
        value[1] = re.sub(pattern, r"\1", value[1])
        value[2] = result2



# Задание 2-----------------------------------------------------------------------------------------
# привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;


pattern = r"(\+7|8)(\s*\(|\W?)(\d{3})\)?\W?(\d{3})\W?(\d{2})\W?(\d{2})"
for value in contacts_list:
    result = re.sub(pattern, r"+7(\3)\4-\5-\6", value[5])
    value[5] = result

pattern = r"\s*?\W?доб\.?\W?(\d{4})\W?"
for value in contacts_list:
    result = re.sub(pattern, r" доб.\1", value[5])


# Задание 3-----------------------------------------------------------------------------------------
# объединить все дублирующиеся записи о человеке в одну.

index_two = 1
delete_index = []
new_contact_list = []

for value in contacts_list:
    for value2 in range(index_two,len(contacts_list)):
        if value[0] == contacts_list[value2][0] and value[1] == contacts_list[value2][1]:
            for i in range(3,7):
                if value[i] == "":
                    value[i] = contacts_list[value2][i]
            delete_index.append(value2)
    index_two += 1

for index in range(len(contacts_list)):
    if index not in delete_index:
        new_contact_list.append(contacts_list[index])






# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_contact_list)