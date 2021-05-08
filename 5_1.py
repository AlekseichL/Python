f_obj = open("new_f.txt", 'a')
while True:
    a=input('Введите данные: ')
    if a=='':
        f_obj.close()
        break
    else:
        f_obj.write(a+'\n')

