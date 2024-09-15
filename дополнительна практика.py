#Напишите программу, которая составляет словарь, используя grades и students,
#где ключом будет имя ученика, а значением - его средний балл.

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades_a_1 = sum(grades[0])
grades_b_1 = len(grades[0])
grades_1 = grades_a_1 / grades_b_1
grades_a_2 = sum(grades[1])
grades_b_2 = len(grades[1])
grades_2 = grades_a_2/grades_b_2
grades_a_3 = sum(grades[2])
grades_b_3 = len(grades[2])
grades_3 = grades_a_3/grades_b_3
grades_a_4 = sum(grades[3])
grades_b_4 = len(grades[3])
grades_4 = grades_a_4/grades_b_4
grades_a_5 = sum(grades[4])
grades_b_5 = len(grades[4])
grades_5 = grades_a_5/grades_b_5
grades_list_ = grades_1, grades_2, grades_3, grades_4, grades_5
students_list_ = list(students)
students_alphabetically = sorted(students)
dictionary = dict(zip(students_alphabetically, grades_list_))
print(dictionary)
#print(type(dictionary))
#{'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}