# Напишите программу для печати всех уникальных значений в словарях.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "}, {" VIII": " S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

dictionaries = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
                {"VII": " S005 "}, {" V ": " S009 "}, {" VIII": " S007 "}]

lst = set()
for i in dictionaries:
    for v in i.values():
        lst.add(v.strip())
print(lst)
