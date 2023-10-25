def calc_final_grades(file):
    javab = {}

    with open(file, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            name = parts[0].lower()
            q_grades = list(map(int, parts[1:7]))
            a_grades = list(map(int, parts[7:11]))
            midterm = int(parts[11])
            final = int(parts[12])

            q_grades.sort()
            q_grades = q_grades[2:]

            a_grades.sort()
            a_grades = a_grades[1:]

            q_avg = sum(q_grades) / len(q_grades)
            a_avg = sum(a_grades) / len(a_grades)

            total = q_avg * 0.25 + a_avg * 0.25 + midterm * 0.25 + final * 0.25

            javab[name] = "Pass" if total >= 60 else "Fail"

    return javab

filename = "C:/New folder/data1.txt"
javab = calc_final_grades(filename)
print(javab)
