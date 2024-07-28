# Students Grade sorting using Selection sort

def StudentsGradeSort(grades):
    for i in range(0,len(grades)):
        minimum = i
        for j in range(i+1 , len(grades)):
            if grades[j] < grades[minimum]:
                minimum = j
        grades[i],grades[minimum] = grades[minimum],grades[i]
    return grades

studentsgrade = [85,92,78,64,89,99,73,88]
print(StudentsGradeSort(studentsgrade))