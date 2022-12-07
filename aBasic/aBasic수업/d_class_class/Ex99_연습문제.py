#2.
class Person(object):
    def  __init__(self, name):
        self.name = name
    def  language(self):
        pass
class Earthling(Person):
    def  language(self, language):
        return language

class Groot(Person):
    def language(self, language):
        return "I'm Groot!"

name = ['Gachon', 'Dr.Strange', 'Groot']
country = ['Korea', 'USA', 'Galaxy']
language = ['Korean', 'English', 'Groot']
for idx, name in enumerate(name):
    if country[idx].upper() != 'GALAXY':
        person = Earthling(name)
        print(person.language(language[idx]))
    else:
        groot = Groot(name)
        print(groot.language(language[idx]))

#3

def factorial(n):
    if n == 0:
        return 1
    else:
        return ( n * factorial(n-1))

print(factorial(6))


#4.
class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number
    def change_back_number(self, back_number):
        self.back_number = back_number

jinhyun = SoccerPlayer("jinhyun", "MF", 10)
print("현재 선수의 등번호는:",jinhyun.back_number)
jinhyun.change_back_number(5)
print("현재 선수의 등번호는:",jinhyun.back_number)

#5.
class Marvel(object):
    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic
    def __str__(self):
        return "My name is {0} and my weapon is {1}.".format(self.name, self.characteristic)
class Villain(Marvel):
        pass
first_villain = Villain("Thanos", "infinity gauntlet")
print(first_villain)

#6.
class TV(object):
    def __init__(self, size, year, company):
        self.size = size
        self.year = year
        self.company = company
    def describe(self):
        print(self.company + "에서 만든 " + self.year + "년형 " + self.size + "인치" + "TV")
class Laptop(TV):
    def describe(self):
        print(self.company + "에서 만든 " + self.year + "년형 " + self.size + "인치 " + "노트북")


LG_TV = TV("32", "2019", "LG")
LG_TV.describe()
samsung_microwave = Laptop("15" , "2018", "Samsung")
samsung_microwave.describe()

#7.
class Score:
    def __init__(self, student):
        tmp = student.split(",")
        self.name = tmp[0]
        self.midterm = int(tmp[1])
        self.final = int(tmp[2])
        self.assignment = int(tmp[3])
        self.score = None
        self.grade = None

    def total_score(self):
        test_score = ((self.midterm + self.final) / 2) * 0.8
        if self.assignment >= 3:
            assign_score = 20
        elif self.assignment >= 2:
            assign_score = 10
        elif self.assignment >= 1:
            assign_score = 5
        else:
            assign_score = 0
        self.score = test_score + assign_score


    def total_grade(self):
        if self.assignment == 0:
            grade = "F"
        elif self.score >= 90:
            grade = "A"
        elif self.score >= 70:
            grade = "B"
        elif self.score >= 60:
            grade = "C"
        else:
            grade = "F"
        self.grade = grade
        return grade



student_john = Score("john,90,90,0")
aa = student_john.total_score()
bb = student_john.total_grade()
print(aa, bb, student_john.score, student_john.grade)