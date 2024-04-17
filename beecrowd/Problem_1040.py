line = input().split(' ')
a = float(line[0])
b = float(line[1])
c = float(line[2])
d = float(line[3])

average = (2*a + 3*b + 4*c +d)/10
print("Media: " + "{:.1f}".format(average))

if average >= 7:
    print("Aluno aprovado.")
elif average < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exam = float(input())
    print("Nota do exame: " + "{:.1f}".format(exam))
    new_average = (average + exam)/2
    if new_average >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: " + "{:.1f}".format(new_average))