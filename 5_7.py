import json
d1={}
d2={}
f=open('new_7.txt', 'r')
for line in f:
    firm, f_sobs, B, R = line.split()
    pr=int(B)-int(R)
    d1[firm]=pr
s=0
n=0
for i in d1.values():
    if i > 0:
        s+=i
        n+=1
d2["average_profit"]=s/n
l=[d1, d2]
print(l)
with open("my_file.json", "w") as write_f:
    json.dump(l, write_f)
