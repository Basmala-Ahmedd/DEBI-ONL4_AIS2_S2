class Course:
    _id_counter = 1
    
    def __init__(self,name):
        self.course_id = Course._id_counter  
        Course._id_counter += 1
        self.name = name  
        self.enrolled_student = []
    def __repr__(self):
        return f"Course ID : {self.course_id} , Name : {self.name} , Enrolled_Students : {len(self.enrolled_student)}"

    def enroll_student(self,student):
        if student not in self.enrolled_student:
            self.enrolled_student.append(student)
            print("Student Enrolled Successfully!.")
        else:
            print("The Student Already Enrolled!.")
            print("The Student Already!.")
    
    def remove_student(self,student):
        if student in self.enroll_student:
            self.enrolled_student.remove(student)
            print("Student Removed Successfully!.")
        else:
            print("Student Not Found in This Course !.")