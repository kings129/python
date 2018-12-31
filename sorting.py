from operator import itemgetter, attrgetter
'''
Sorting HOW TO
https://docs.python.org/3/howto/sorting.html
'''

a = [5, 2, 3, 1, 4]
print(sorted(a))

# list.sort() modify list in-place.
a.sort()
print(a)

# list.sort() is only defined for lists. In contrast, sorted()
# function accept any iterable.
dict = {2: 'B', 1: 'A', 3: 'C', 4: 'D'}
print(sorted(dict))

# Key functions
# Both list.sort() and sorted() have a key parameter to specify a function
# to be called on each list element prior to making comparisions.
s = 'This is a test string from Qiang'
print(sorted(s.split(), key=str.lower))

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
s = sorted(student_tuples, key=lambda student: student[2])  # sort by age
print(s)


# python __str__ VS __repr__
# https://dbader.org/blog/python-repr-vs-str
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
s = sorted(student_objects, key=lambda student: student.age)
print(s)

# Operator module functions
# The key-function patterns show above are very common, so Python provides
# convenience functions to make accessor functions easier and faster.
print(sorted(student_tuples, key=itemgetter(2)))
print(sorted(student_objects, key=attrgetter('age')))

# The operator allow mutiple levels of sorting!
print(sorted(student_tuples, key=itemgetter(1, 2)))  # Grade then age
print(sorted(student_objects, key=attrgetter('grade', 'age')))

# Ascendign and Descending
# Both list.sort() and sorted() accept a reverse parameter with a boolean value.
print(sorted(student_tuples, key=itemgetter(2), reverse=True))
print(sorted(student_objects, key=attrgetter('age'), reverse=True))

# The sort routines are guaranteed to use __lt__() when making comparision between
# two objects, So it is easy to add a standard sort order to a class by defining an
# __lt__() method:
Student.__lt__ = lambda self, other: self.age < other.age
print('provide __lt__')
print(sorted(student_objects))
