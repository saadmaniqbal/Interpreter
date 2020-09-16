##### tc11.py #####
a=40
b=400
m=4000 if b<a else 4
l1=[m]
l2=l1+l1+l1
print(l2[2]) #the index will always be given as len(list)-1
>>>4

##### tc12.py #####
x="a"
y="b"
z="z" if x==y else "c"
l1=[z]+["z"]

w="w" if x<y else "d"
l2=l1+[w]
print(l2)
>>>["c","z","w"]

##### tc13.py #####
a1=30
b1=50
c1=55

m1=22 if a1==30 else 0
l1=([a1]+[b1]+[c1])+[m1] 
print(l1[1:])
>>>[50,55,22]

b1=40
n1=34 if b1>45 else 0
l2=[n1]+l1
print(l2)
>>>[0,30,50,55,22]
print(l2[3])
>>>55

##### tc14.py (advanced) #####
a=40
l1=["50"]
#error <-(print this in .out file)
l2=[a]+l1 
l3=l1+(["300"]+["21"])
print(l3)
>>>["50","300","21"]
#error <-(print this in .out file)
l4=l3+[a]

##### tc15.py (advance- maximum 1 or 0 final test will be like this) #####
l1=[4]
l1=l1+[7]
l1=l1+[7]
l1=l1+[9]
l1=l1+[10]
print(l1)
>>>[4,7,7,9,10]
print(l1[2]) 
>>>7
l2=l1+l1+l1
print(l2[1:])
>>>[7, 7, 9, 10, 4, 7, 7, 9, 10, 4, 7, 7, 9, 10]
