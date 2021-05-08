my_f= open("num.txt", 'r')
f_obj = open("f.txt", 'a')
for line in my_f:
    a=line.split('-')
    if a[0]=='One':
        a[0]='Один'
    if a[0]=='Two':
        a[0]='Два'
    if a[0]=='Three':
        a[0]='Три'
    if a[0]=='Four':
        a[0]='Четыре'
    print(a)
    b=a[0]+'-'+a[1]
    f_obj.write(b)
f_obj.write('\n')
