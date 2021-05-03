#а) итератор, генерирующий целые числа, начиная с указанного
from itertools import count

for el in count(3):
    if el > 10:
        break
    print(el)

print(' ') #для разделения частей задания (чтобы не сливались)

# б) итератор, повторяющий элементы некоторого списка, определенного заранее
from itertools import cycle

с = 0
my_list=[i for i in range(2, 13, 2)]
print(my_list)
for el in cycle(my_list):
    if с > 11:
        break
    print(el)
    с += 1
