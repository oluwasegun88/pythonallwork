students = dict()
n = int(input("Enter number of students :"))
for i in range(n):
        sname = input("Enter names of student :")
        marks= []
        for j in range(2):
           mark = float(input("Enter marks :"))
           marks.append(mark)
        students[sname] = marks
        subject = []
        for j in range(2):
            subject = input("Enter subject")
print("Dictionary of student created :")
print(students)

