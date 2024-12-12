"""Create a dictionary storing data on one University of Warsaw student. 
The dictionary should contain at least 5 different pieces of information about this student 
(you can choose the information yourself, e.g. first name, faculty, id, etc). (1p) 
Next: 
add to the dictionary using a method another key:value pair which should contain 
information about the final grade of the programming class (1p). 
Finally, display all the information about the student using loops (1p)
"""
student = {"first_name":"Ania", "last_name":"Kowalska", "age":24, "faculty":"Wydział Lingwistyki Stosowanej",
            "student_id":"345875"}

student.update({"grade":4.5})

for k, v in student.items():
    label = k.replace("_", " ").capitalize()
    print(f"{label}: {v}")