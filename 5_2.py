my_f = open("text.txt", "r")
content = my_f.readlines()
print('Количество строк в файле: ',len(content))
my_f = open("text.txt", "r")
i=1
for line in my_f:
    print(f'Количество слов в {i} строке: ',len(line.split()))
    i+=1
my_f.close()

