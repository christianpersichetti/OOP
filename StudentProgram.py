import StudentClass as sc


student_ID = input(
    "Student ID:",
)
student_name = input(
    "Student Name:",
)
student_dob = input(
    "Date Of Birth(mm/dd/yyyy):",
)
student_class = input(
    "Classification(F, S, Jr, Sr):",
)


student1 = sc.Student(student_ID, student_name, student_dob, student_class)

student1.calc_age()

student1.calc_register()

print(f"Student age is: {student1.get_age()}")
print(f"Student can register between{student1.get_registration()}")
