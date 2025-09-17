
students = dict()
n = int(input("how many student are there :"))
for i in range(n):
    sname = input("Enter name of student : ")
    marks = []
    for j in range(5):
        mark = float(input("Enter marks : "))
        marks.append(mark)
        students[sname] = marks

        print("created dictionary of student is",students)

        name = input("Enter name of student")

        if name in students.keys():
            print(students[name])
        else:
            print("no student found with this name")
       