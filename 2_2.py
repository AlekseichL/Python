l = list(input('Введите значения элемента списка ').split())
print(l)
j = 0
for i in range(int(len(l)/2)):
  l[j], l[j+1] = l[j+1], l[j]
  j += 2
print(l)

