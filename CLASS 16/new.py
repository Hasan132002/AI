import pandas as pd

# Check if the Excel file exists, and create it if not
excel_file_path = 'student_data.xlsx'
try:
    student_data = pd.read_excel(excel_file_path, index_col=0).to_dict(orient='index')
except FileNotFoundError:
    student_data = {}

def save_to_excel():
    pd.DataFrame.from_dict(student_data, orient='index').to_excel(excel_file_path, index_label='ID')

def add_student(id, name, age, grade):
    student_data[id] = {'name': name, 'age': age, 'grade': grade}
    save_to_excel()
    print(f"Student with ID {id} added successfully!")

def get_student(id):
    print(student_data.get(id, "Student Not Found"))

def delete_student(id):
    if id in student_data:
        del student_data[id]
        save_to_excel()
        print(f"Student with ID {id} deleted successfully!")
    else:
        print("Student Not Found")

def update_student(id):
    if id in student_data:
        print("Current Student Data:")
        print(student_data[id])
        name = input("Enter updated student Name (Press Enter to keep current): ")
        age = input("Enter updated student Age (Press Enter to keep current): ")
        grade = input("Enter updated student Grade (Press Enter to keep current): ")
        if name:
            student_data[id]['name'] = name
        if age:
            student_data[id]['age'] = age
        if grade:
            student_data[id]['grade'] = grade
        save_to_excel()
        print(f"Student with ID {id} updated successfully!")
    else:
        print("Student Not Found")

def display_all_students():
    print("\nAll Students Data:")
    for id, data in student_data.items():
        print(f"ID: {id}, Name: {data['name']}, Age: {data['age']}, Grade: {data['grade']}")

def ai_analysis():
    grades = [float(data['grade']) for data in student_data.values() if str(data['grade']).replace('.', '').isdigit()]
    if grades:
        average_grade = sum(grades) / len(grades)
        print(f"\nAI Analysis: Average Grade of All Students: {average_grade:.2f}")
    else:
        print("\nAI Analysis: No valid student grades available for analysis.")

def retrieve_all_students():
    display_all_students()

def delete_all_students():
    global student_data
    student_data = {}
    save_to_excel()
    print("All Students deleted successfully!")

def update_all_students():
    for id in student_data.keys():
        update_student(id)

while True:
    print("\nStudent Management System")
    print("1 - Add Student")
    print("2 - Retrieve Student")
    print("3 - Update Student")
    print("4 - Delete Student")
    print("5 - Display All Students")
    print("6 - AI Analysis")
    print("7 - Retrieve All Students from Excel")
    print("8 - Delete All Students from Excel")
    print("9 - Update All Students from Excel")
    print("10 - Exit")
    choice = input("Enter your choice (1-10): ")

    if choice == '1':
        id = input('Enter student Id: ')
        name = input('Enter student Name: ')
        age = input('Enter student Age: ')
        grade = input('Enter student Grade: ')
        add_student(id, name, age, grade)
    elif choice == '2':
        id = input("Enter the id of the Student to retrieve data: ")
        get_student(id)
    elif choice == '3':
        id = input("Enter the id of the Student to update data: ")
        update_student(id)
    elif choice == '4':
        id = input("Enter the id of the Student to delete: ")
        delete_student(id)
    elif choice == '5':
        display_all_students()
    elif choice == '6':
        ai_analysis()
    elif choice == '7':
        retrieve_all_students()
    elif choice == '8':
        delete_all_students()
    elif choice == '9':
        update_all_students()
    elif choice == '10':
        print('Thank you for using this system!')
        break
    else:
        print('Invalid Choice! Please enter a valid choice (1-10).')
