####tc1.py#######
a=[3]
b=[5]
l1=a+b
print(l1) 
>>>[3,5]

####tc2.py#######
x=['s1']
y=['s2']
z=['s3']
l2=(x+y+z)
print(l2)
>>>['s1','s2','s3']

####tc3.py#######
a=[1]
b=[2]
c=[3]
d=[4]
l3=a+b+c
l4=c+d+[5]
print(l3[0])
>>>1
print(l4[1:])
>>>[4,5]

####tc4.py#######
x=['a']
y=['b']
z=['c']
l5=[3]+[5]
print(l5)
>>>[3,5]
l6=(x+y+z)+['d']+['e']
print(l6)
>>>['a','b','c','d','e']
print(l6[1:])
>>>['b','c','d','e']

####tc5.py#######
w=3
m=[w]
y=0 if w>0 else -1
n=[y]
l7=m+n
print(l7)
>>>[3,0]
