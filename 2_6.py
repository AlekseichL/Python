m = int(input('Введите количество добавляемых позиций  :'))
n=1
j=1
while j<=m:
    globals()['k' + str(j)]=(n, {"название": input('Введите название товара  :'), "цена": int(input('Введите цену товара  :')),"количество": int(input('Введите количество товара  :')), "eд": 'шт.'})
    print(globals()['k' + str(j)])
    n+=1
    j+=1
print(' ') #для того чтобы записи не сливались
pr =[globals()['k' + str(i)][1]["название"] for i in range(1, m+1) ]
print("Название:", pr)
pr =[globals()['k' + str(i)][1]["цена"] for i in range(1, m+1) ]
print("цена:", pr)
pr =[globals()['k' + str(i)][1]["количество"] for i in range(1, m+1) ]
print("количество:", pr)
print('“ед”: [“шт.”]')  #решил не мудрить, а просто напечатать так, потому что данная часть не изменяется
