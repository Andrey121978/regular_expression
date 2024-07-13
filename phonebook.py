from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

def name_satandard(contact_list):
  contact_list_update = []
  contact_list[0] = " ".join(contact_list[:3])
  contact_list_update += (contact_list[0].split(' ')[:3])
  contact_list_update += contact_list[3:7]
  #print(contact_list_update)
  return contact_list_update

def name_unic(contact_list):
  flag = 0
  contact_list_unic = []
  contact_list_unic.append(contact_list[0])
  for i in range(1, len(contact_list)):
    flag = 0
    for j in range(1, len(contact_list_unic)):
      if contact_list[i][0] == contact_list_unic[j][0] and contact_list[i][1] == contact_list_unic[j][1]:
        for k in range(2, len(contact_list[i])):
          if contact_list[i][k] != contact_list_unic[j][k]:
            contact_list_unic[j][k] += contact_list[i][k]
        flag = 1
    if flag == 0:
      contact_list_unic.append(contact_list[i])
  return contact_list_unic


with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)



#pprint(contacts_list)
contacts_list_standard = []
# TODO 1: выполните пункты 1-3 ДЗ

for contact in contacts_list:
  contacts_list_standard.append(name_satandard(contact))


contacts_list_unic = name_unic(contacts_list_standard)

pattern = r"(\+7|8)\s*\(*(\d{3})\)*\s*\-*(\d{3})\-*(\d{2})\-*(\d{2})"
pattern1 = r"\(*(\w+)\.\s*(\d+)\)*"
substr = r"+7(\2)\3-\4-\5"
substr1 = r"\1.\2"
for contact in contacts_list_unic:
    result = re.sub(pattern, substr, contact[5])
    if result:
      contact[5] = result
    result1 = re.sub(pattern1, substr1, contact[5])
    if result1:
      contact[5] = result1


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list_unic)