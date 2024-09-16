grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
alf_students = sorted(students)

len_1 = len(grades[0])
sum_1 = sum(grades[0])
slot_1 = sum_1 / len_1
grades[0] = slot_1

len_2 = len(grades[1])
sum_2 = sum(grades[1])
slot_2 = sum_2 / len_2
grades[1] = slot_2

len_3 = len(grades[2])
sum_3 = sum(grades[2])
slot_3 = sum_3 / len_3
grades[2] = slot_3

len_4 = len(grades[3])
sum_4 = sum(grades[3])
slot_4 = sum_4 / len_4
grades[3] = slot_4

len_5 = len(grades[4])
sum_5 = sum(grades[4])
slot_5 = sum_5 / len_5
grades[4] = slot_5

dictionary = dict(zip(alf_students, grades))
print(dictionary)
