class student:
  def __init__(self,name,age,grade):
    self.name=name
    self.age=age
    self.grade=grade


student1=student("Alice",20,"A")
student2=student("Bob",22,"B")
print(f"student name is {student1.name}, age is {student1.age}, grade is {student1.grade}")
print(f"student name is {student2.name}, age is {student2.age}, grade is {student2.grade}")



