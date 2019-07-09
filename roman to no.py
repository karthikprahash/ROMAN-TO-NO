# ROMAN-TO-NO
dic={"I":1,"V":5,"X":10}
i=input()
if i=='IV':
    print('4')
elif i=='IX':
    print('9')
else:
    i=list(i)
    s=0
    for item in i:
        s=s+dic[item]
    print(s)
