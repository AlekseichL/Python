d= {}
f=open('new_6.txt', 'r')
for line in f:
    subject, lecture, practice, lab = line.split()
    l=0
    for x in lecture:
        if x.isdigit():
            l=str(l)+str(x)
    p = 0
    for x in practice:
        if x.isdigit():
            p = str(p) + str(x)
    j = 0
    for x in lecture:
        if x.isdigit():
            j = str(j) + str(x)
    d[subject] = int(l)+ int(p)+ int(j)
print(f'Общее количество часов по предмету - \n{d}')


