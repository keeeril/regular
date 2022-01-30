import re
from pprint import pprint
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

for contact in range(1, len(contacts_list)):
  # print(contact)
  i = contacts_list[contact]
  # print(i)
  name_pattern = r"'(\w*[А-Яа-я]+)'?,?\s?'?([А-Я][а-я]+)'?,?\s?'?(\w+)?'"
  name = re.findall(name_pattern, str(i))
  # print(name)
  phone_pattern = r"(\+7|8)?\s?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d+)(\s?\(?(доб.)\s?(\d+)\)?)?"

  i[0] = name[0][0]
  i[1] = name[0][1]
  i[2] = name[0][2]
  i[5] = re.sub(phone_pattern, r"+7(\2)\3\4\5 \7\8", i[5])

  if len(i) > 7:
    del i[7:]


new_contacts = [contacts_list[0]]
for i in contacts_list:
  last_name = i[0]
  first_name = i[1]
  for ii in range(1, len(contacts_list)):
    c2 = contacts_list[ii]
    if last_name == c2[0] and first_name == c2[1]:
      index = 2
      while index <= 6:
        if i[index] == '':
          i[index] = c2[index]
        index += 1
  if i not in new_contacts:
    new_contacts.append(i)
# print(correct_contacts)

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_contacts)
  print('Ready!')
