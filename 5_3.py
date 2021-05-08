my_f = open("zp.txt", "r")
s=[el.split() for el in my_f]
my_f = open("zp.txt", "r")
n=my_f.readlines()
print('Оклад меньше 20 тыс. имеют сотрудники: ',\
[s[i][0] for i in range(len(n)) if int(s[i][1]) < 20000])
sum=0
for i in range(len(n)):
    sum+=int(s[i][1])
print('Средняя величина дохода сотрудников: ', sum/len(n))
my_f.close()


