def CAlculator():
    a = int(input("a : "))

    b = int(input("b : "))

    number = a + b 
    
    print(number)


CAlculator()


def Name():
    Name = "ahmed"
    print(Name)

Name()

def age():
    age = 20
    print(age)

age()

def gpa():
    gpa = 4
    print(gpa)
 
gpa()

def your():
    age = int(input("enter your age :"))
    print(age)

    Name = input("enter your name :" )
    print(Name)
your()

def calculator():
    ax = int(input("ax : "))
    
    bx = int(input("bx : "))
    
    numbar = ax * bx
    
    print(numbar)
calculator()

def Calculator():
    aa = int(input("aa : "))
    
    bb = int(input("bb : "))
    
    number = aa / bb
    print(number)
Calculator()

def mm():
    x = 10
    z = 20
    print(x == z)
mm()


def nn():
    A = "asdfghjkqwer"
    print(A)

    print(A[5])
    print(A[0])
    print(A[-2])
nn()


# list
def list():
    h = [1 , 2, 3, 4]
    print(h)

# list mix 
    b = ["ai", 2, 3, 4,]
    print(b)

    gpa = input("gpa : ")

    print(gpa)
    
    Name = input("Name :")
    
    print(Name)
    
    g = [gpa,Name ]

    print(g)

    a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    a.append(10)
    print(a)
    k = ["aa", 123, 17 , "alzawea alhamra"]

    k.remove("alzawea alhamra")
    k.append("aa@gmail.com")
    k[2] = 4
    print(k)

# update 
    
    a [1] = 20
    print(a)
    a.pop

list()

def tuple():
    tup =('hallo', 'world',8,'j',True)
    print(tup[0])
    print(tup[3])

tuple()

def ll():
    s1 = set("set date")
    print(s1)
ll()

def dictionary():
    d = {}

#{key : value}

    D = {1:'aa', 2:'nn',3:'mm' }
    print(D.get(1))
    D.keys()
    print(D)
    print(D.keys())

#ex 2
    d =  {"Name":'ahmed', "age": 20, id:111111111 }
    print(d)
    d.keys()
    print(d.keys())

    print(d.get("Name"))

    print(d.get("age"))

    print(d.get(id))

dictionary()

# if 
def iFtest():
    num = 7
    if num == 7:
        print("the number 7")

    temperature = int(input("enter the temperature: "))
    if temperature > 30:
        print("it hot outside")
    else : 
        print("it not hot outside")




iFtest()


def lol():
    furuits = ["apple","banana","cherry"]
    print(furuits[0])
    print(furuits[1])
    print(furuits[2])
    for x in "banana":
        print(x)
#break (stop)

    fruits = ["apple","banana","cherry"]
    for x in fruits:
        print(x)
        if x =="banana":
            break
               #start,end,step
    for j in range(0,11,1):
        print(j)

    for b in range(11,0,-1):
        print(b)
lol()
def ooo():
#while loop
  
    i = 0
    while i < 6:
        i += 1
        print(i)
ooo()

def ttt():
    i = 0
    while i > 10:
        i+=1
        if i == 3:
            continue
    print(i)
ttt()

