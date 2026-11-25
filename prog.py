'''import keyword
print(keyword.kwlist)

a=None
print(a)

a=10
print(bool(a))

a=1.0
print(bool(a))

print(int())
print(float())

a=10+8j
print(complex(a))'''

'''a=6j
print(a)'''

'''a="happy father's day"
print(a)
print(a[-10])

a=10,20,30
print(a,type(a))

a={10,20,30,40}
print(a,type(a))

a={'a':10,'b':20}
print(a,type(a))

a={'a':[10,20,30],'b':30}
print(a['a'][1])'''

'''a="Hello"
print(a[2:3:1])

a="Hello"
print(a[2:3+1:1])'''

'''a="Hello"
print(a[-3:-2+1:1])'''

'''a="Good Morning"
print(a[7:10+1:1])
print(a[-5:-2+1:1])'''

'''a="Good Morning"
print(a[10:7-1:-1])
print(a[-2:-5-1:-1])'''

'''a="Good Morning"
print(a[10:7:-1])'''

'''a="Good Morning"
print(a[::-1])'''

'''a="Good Morning"
'odm'
print(a[1:5+1:2])
'mng'
print(a[5:11+1:3])
print(a[5::3])
print(a[-7::3])'''

'''a="Good Morning"
'nr'
print(a[10:4-1:-3])

a="Good Morning"
print(a[-2:-8-1:-3])'''

'''a=input("Enter:")
print(a)'''

'''a=int(input("Enter:"))
print(type(a))'''

'''a=eval(input("Enter:"))
print(a,type(a))'''

'''a=float(input("Enter:"))
print(a,type(a))'''

'''a=int(input("Enter:"))
if(a%2==0):
    print("Even")
else:
    print("Odd")'''

'''l=eval(input("Enter list:"))

if len(l)==5:
    print("Yes")
else:
    print("No")'''

'''print(chr(65))
print(ord('a'))
print(chr(97))
print(ord('A'))
print(chr(ord('A')+32))'''

'''ch=input("Enter:")
if "A"<=ch<="Z":
    print("Uppercase")
elif "a"<=ch<="z":
    print("Lowercase")
else:
    print("Not an Alphabet")'''

'''un=input("Enter username:")
if un=="harshitha_kv__":
    print("Correct username")
    pw=input("Enter password:")
    if pw=="harshitha":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")'''

'''i=1
while i<=100:
    print(i)
    i+=1'''

'''i=0
while i<=50:
    print(i)
    i+=2'''

'''a=10
if a>0:
    print("Positive Number")'''

'''n=int(input("Enter a number:"))
rev=0
while n>0:
    id=n%10
    n=n//10
    rev=rev*10+id
    print(rev)'''

'''for i in range(1,11):
    print(i)'''

'''for i in range(1,51):
    if i%2==0:
        print(i,"even")'''

'''l=[10,20,30]
for i in l:
    print(i)'''

'''s=input("Enter a string:")
output=""
for i in s:
    if"A"<=i<="Z":
        output+=chr(ord(i)+32)
    elif "a"<=i<="z":
        output+=chr(ord(i)-32)
    else:
        output+=i
print(output)'''

'''s=input("Enter a string:")
reverse=""
for i in s:
    reverse=i+reverse
print(reverse)'''

'''for i in range(1,6):
    for j in range(1,6):
        print('*',end="")
    print()'''

'''for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('*',end="")
        else:
            print(' ',end="")
    print()'''

'''for i in range(1,6):
    for j in range(1,6):
        if i>j:
            print('*',end="")
        else:
            print(' ',end="")
    print()'''

'''for i in range(1,6):
    for j in range(1,6):
        if i<j:
            print('*',end="")
        else:
            print(' ',end="")
    print()'''

'''a=10,20,30
print(a,type(a))'''

'''a="happy birthday"
'htr'
print(a[10:8-1:-1])'''

'''a="happy birthday"
print(a[-4:-7:-1])'''

# with argument and with return type
'''def convert(s,output):
    output=' '
    for i in s:
        if "a"<=i<="z":
            output+=chr(ord(i)-32)
        else:
            output+=i
    return output
print(convert(input("Enter a string:"),' '))'''

#with argument and without return type
'''def convert(s,output):
    output=' '
    for i in s:
        if "a"<=i<="z":
            output+=chr(ord(i)-32)
        else:
            output+=i
    print(output)
convert(input("Enter a string:"),' ')'''

#without argument and without return type
'''def convert():
    s=input("Enter a string:")
    output=' '
    for i in s:
        if "a"<=i<="z":
            output+=chr(ord(i)-32)
        else:
            output+=i
    print(output)
convert()'''

#without argument and with return type
'''def convert():
    s=input("Enter a string:")
    output=' '
    for i in s:
        if "a"<=i<="z":
            output+=chr(ord(i)-32)
        else:
            output+=i
    return output
print(convert())'''

#OOPs
'''class college:
    cname="gpln"
    cloc="hoodi"
s1=college()
print(s1.cname, s1.cloc)
print(college.cname)
print(college.cloc)
college.cloc="k r puram"
print("changing loc wtrsp obj")
s1.cloc="hoodi"
print(s1.cloc)
print(college.cloc)'''

'''class college:
    cname="GPLN"
    cloc="Hoodi"

s1=college()
s1.sname="Harshitha"
s1.phno=1234567890

s2=college()
s2.sname="Deeksha"
s2.sphno=9876543210

s1.cloc="K R Puram"
print("After changing ")
print(s1.cloc)
print(s2.cloc)'''

#constructor
'''class college:
    def __init__(self,name,phno,usn):
        self.name=name
        self.phno=phno
        self.usn=usn

    def display(self):
        print("Name:",self.name)
        print("Phno:",self.phno)
        print("Usn:",self.usn)

s1=college('Harshitha',1234567890,'cd015')
s2=college('Deeksha',9876543210,'cd014')
s1.display()
s2.display()'''

'''class college:
    def __init__(self,name,phno,usn):
        self.name=name
        self.phno=phno
        self.usn=usn

s1=college('Harshitha',1234567890,'cd015')
s2=college('Deeksha',9876543210,'cd014')
print(s1.name)
print(s2.name)'''

'''class college:
    cname="GPLN"
    cloc="Hoodi"

    @classmethod
    def disp(cls):
        print("cls.cname:",cls.cname)
        print("cls.cloc:",cls.cloc)

    def __init__(self,name,phno,usn):
        self.name=name
        self.phno=phno
        self.usn=usn

    def display(self):
        print("Name:",self.name)
        print("Phno:",self.phno)
        print("Usn:",self.usn)

    def change_name(self,newname):
        self.name=newname

    def change_phno(self,newphno):
        self.phno=newphno

s1=college('Harshitha',1234567890,'cd015')
s2=college('Deeksha',9876543210,'cd014')
s1.display()
s2.display()

s1.change_name("Sandhya")
s1.display()
s2.change_phno(5647382910)
s2.display()'''

'''a=10,20,30
print(a,type(a))'''

