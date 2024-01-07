student_data={}
def add_student(id,name,age,grade):
    student_data[id]={'name':name,
                      'age':age,
                      'grade':grade}

def get_student(id):
    print(student_data.get(id,"Student Not Found"))
    
def delete_student(id):
    if id in student_data:
        del student_data[id]
        print("Data Deleted Sucessfully")
    else:
        print(f"Student with ID : {id} doesn't exist ")
def update_student(id):
    if id in student_data:
        print("Current Student Data")
        print(student_data[id])
        name=input("Enter update name of the student")
        age=input("Enter update age of the student")
        grade=input("Enter update grade of the student")
        if name:
            student_data[id]['name']=name
        if age:
            student_data[id]['age']=age
        if grade:
            student_data[id]['grade']=grade
        print("Student data updated")
    else:
        print("Id doesnot exist")
            
    
    
    
    
    
    
    
while True:
    print("Student Management System")
    print("1 - Add Student ")
    print("2 - Retrieve Student")
    print("3 - Delete Student")
    print("4 - Update Student")
    print("5- Exit")
    choice = input("Enter the choice between (1-5)")
    if choice=='1':
        id_bahar_wali=input('Enter student Id')
        name_bahar_wala=input('Enter student Name')
        age_bahar_wali=input('Enter student Age')
        grade_bahar_wali=input('Enter student Grade')
        add_student(id_bahar_wali,name_bahar_wala,age_bahar_wali,grade_bahar_wali)
    elif  choice=='2':
        id=input("Enter the id of the Student  to retrieve data")
        get_student(id)
    elif choice =='3':
                id=input("Enter the id of the Student  to delete data")
                delete_student(id)
    elif choice =='4':
                id=input("Enter the id of the Student  to delete data")
                update_student(id)
    elif choice == '5':
        print('Thank for using this system')
        break
    else:
        print('Invalid Choice ! Please Enter valid choice between (1-3) again ')



        
        
        

        



crud
create
read
update
delete



'''print(f"Student {name} added successfully")
id_bahar_wali=input('Enter student Id')
name_bahar_wala=input('Enter student Id')
age_bahar_wali=input('Enter student Id')
grade_bahar_wali=input('Enter student Id')
add_student(id_bahar_wali,name_bahar_wala,age_bahar_wali,grade_bahar_wali)
'''