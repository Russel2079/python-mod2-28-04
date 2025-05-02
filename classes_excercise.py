# Duration: 30 minutes
# Objective 
# This is a short exercise to practice creating classes that follow the 4 OOP principles.
# Part 1 
# Create a Student class that takes the name and age on creation.
# Create 2 objects of your student class and get the age of one of them.
# Part 2
# With your Student class, make modifications for the class to accept the student’s current class (as in a classroom) on creation.
# Then add a method that takes 3 test scores and calculates the student’s average test score.
# Part 3
# Create 3 classes, A bird parent class and then an Owl and Dodo class.
# Make use of the 4 OOP Principles.


# Part 1 
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("John Gold", 16)
student2 = Student("Ian Silva", 17)

print(student2.age)


# Part 2
class Student:
    def __init__(self, name, age, classroom):
        self.name = name
        self.age = age
        self.classroom = classroom

    def average_test_score(self, score1, score2, score3):
        return (score1 + score2 + score3)/3 



student1 = Student("Ian Silva", 17, "Year9")

print(student1.average_test_score(80, 90, 70))


# Part 3

class Bird:
    def __init__(self, species):
        self.species = species
        

    def make_sound(self):
        return "Make some bird sound"   
        

    def __str__(self):
        return f"{self.species} - {self.__class__.__name__}"    


class Owl(Bird):
    def make_sound(self):
        return "Hoot hoot!"

class Dodo(Bird):
    def make_sound(self):
        return "Dodo dodo"


owl = Owl("Owl")   
dodo = Dodo("Dodo") 

print(f"{owl.species}: {owl.make_sound()}")
print(f"{dodo.species}: {dodo.make_sound()}")