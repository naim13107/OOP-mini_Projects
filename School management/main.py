from school import School
from person import Student , Teacher
from subject import Subject
from classroom import Classroom

school = School("ABC" , "Dhaka" )

eight = Classroom("Eight")
nine = Classroom("Nine")
ten = Classroom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

rahim = Student("Rahim",eight)
karim = Student ("Karim",nine)
fahim = Student ("Fahim", ten)
hamim = Student ("Hamim",ten)

school.student_admission(rahim)
school.student_admission(fahim)
school.student_admission(hamim)
school.student_admission(karim)

abul=Teacher("Abul Khan")
babul=Teacher("Babul Khan")
kabul=Teacher("Kabul Khan")

bangla = Subject("Bangla",abul)
physics= Subject("Physics",babul)
chemistry = Subject("Chemistry",kabul)
biology = Subject("Biology",kabul)



eight.add_subjects(bangla)
eight.add_subjects(physics)
eight.add_subjects(chemistry)
nine.add_subjects(physics)
nine.add_subjects(chemistry)
nine.add_subjects(biology)
ten.add_subjects(physics)
ten.add_subjects(chemistry)
ten.add_subjects(biology)
ten.add_subjects(bangla)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)

                 

