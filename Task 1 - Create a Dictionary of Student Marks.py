student_list = {"Alice": 85,"Jivan": 92,"Kent": 78,"Rahul": 96}
student_name = input("Enter the student's name: ")
if student_name in student_list:
    marks = student_list[student_name]
    print(f"{student_name}'s marks: {marks}")
else:
    print(f"Sorry, {student_name} not found.")