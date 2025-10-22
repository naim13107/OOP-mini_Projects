class StudentDatabase:
    __student_list = []
    
    @classmethod
    def add_student(cls, student_obj):
        cls.__student_list.append(student_obj)
    
    @classmethod
    def get_all_students(cls):
        return cls.__student_list
    
    @classmethod
    def find_student(cls, student_id):
        for student in cls.__student_list:
            if student._Student__student_id == student_id:  
                return student
        return None 

class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.__is_enrolled:
            raise Exception("Student is already enrolled.")
        self.__is_enrolled = True

    def drop_student(self):
        if not self.__is_enrolled:
            raise Exception("Student is not enrolled, can't be dropped.")
        self.__is_enrolled = False

    def view_student_info(self):
        print(f"ID: {self.__student_id}, Name: {self.__name}, "
              f"Department: {self.__department}, Enrolled: {self.__is_enrolled}")

def menu():
    while True:
        print("\n----- Student Management System -----")
        print("1.View All Students")
        print("2.Enroll Student")
        print("3.Drop Student")
        print("4.Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            students = StudentDatabase.get_all_students()
            if not students:
                print("No students available.")
            else:
                print("\n--- Student List ---")
                for student in students:
                    student.view_student_info()

        elif choice == "2":
            try:
                sid = input("Enter student ID to enroll: ")
                student = StudentDatabase.find_student(sid)
                if student is None:
                    raise Exception("Invalid student ID.")
                student.enroll_student()
                print("Student enrolled successfully.")
            except Exception as e:
                print("Error:", e)

        elif choice == "3":
            try:
                sid = input("Enter student ID to drop: ")
                student = StudentDatabase.find_student(sid)
                if student is None:
                    raise Exception("Invalid student ID.")
                student.drop_student()
                print("Student dropped successfully.")
            except Exception as e:
                print("Error:", e)

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid input, please try again.")


Student("S101", "A", "CSE")
Student("S102", "B", "EEE",True)
Student("S103", "C", "BBA", True)

menu()
