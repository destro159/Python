a=10
b=20
c=40
if(a>b&a>c):
    print("a is greatest:",a)
elif(b>c):
    print("b is greatest:",b)
else:
    print("c is greatest",c)

tup1 =('a','b','c')
if 'a' in tup1:
    print("value a is present in tup1:")

l1 =['a','b','c']
if l1[1]=='b':
    l1[1]='g'
    print("l1:",l1)

d1 ={'k1':10 ,'k2':20,'k3':30}
if d1['k2']==20:
    d1['k3'] =d1['k3']+100
    print(d1)