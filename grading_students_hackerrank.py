
def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 38:
            rem = grades[i]%10
            if rem<5:
                if (5-rem) < 3:
                    grades[i] += (5-rem)
            if rem>5:
                if (10-rem) < 3:
                    grades[i] += (10-rem)
    return grades

n = int(input())

grades = []

for _ in range(n):
    grades_item = int(input())
    grades.append(grades_item)

result = gradingStudents(grades)

print(result)


