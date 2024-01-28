#1
myDict={
    "Hello":"Bonjour",
    "Bye":"Au revoir",
    "Beautiful":"Belle"
}
def addNew(english,french):
    myDict[english]=french
def delete(english):
    if english in myDict:
        del myDict[english]
def findWord(english):
    return myDict.get(english, f"You don't have {english}")
def replaceWord(english,frenchWord):
    if english in myDict:
        myDict[english] =frenchWord
addNew("Good","Bien")
print(myDict)
delete("Hello")
print(myDict)
print(findWord("Bye"))
replaceWord("Bye","Adieu")
print(myDict)
#2
worker={
    1: {'Name and Lastname':'Piter Brown',
        'Phone':'+45878348745',
        'Working email':'piter.brown@gmail.com',
        'Job title':'Programmer',
        'Office room':10,
        'Skype':'piter.brown'
        },
    2: {'Name and Lastname':'Anna Pink',
        'Phone': '+886938693806',
        'Email':'p.anna@gmail.com',
        'Job title':'Maqnager',
        'Office room':12,
        'Skype':'pink.anna'}
}
def addWorker(name,phone,email,jobTitle,officeroom,skype):
    number=len(worker)+1
    worker[number] = {
        'Name and Lastname': name,
        'Phone': phone,
        'Email': email,
        'Job title':jobTitle,
        'Office room':officeroom,
        'Skype':skype
    }
def delete(number):
    if number in worker:
        del worker[number]
def findWorker(number):
    return worker.get(number,f"Try again")
def replace(number,inform,newinform):
    if number in worker:
        if inform in worker[number]:
            worker[number][inform]=newinform
addWorker("Bob Stet",
          "+325032505",
          "bob.stet@gmail.com",
          "accountant",
          11,
          "bob.stet")
print(worker)
delete(2)
print(worker)
print(findWorker(1))
replace(1,"Working email","brownpiter@gmail.com")
print(worker)
#3
electric={
    "laptop":200,
    "phone":150,
    "tablet":170
}
for key,value in electric.items():
    print(f"{key}:{value}")
def costElectric(key):
    print(f"{key} costs -",electric.get(key))
key=input("Enter name of product:")
costElectric(key)
def newPrice(key,value):
    electric[key]=value
newPrice("laptop",230)
print(electric)
def addElectric(name,cost):
    if isinstance(name,str) and isinstance(cost,(int,float)):
        electric[name]=cost
name=input("Enter new position:")
cost=int(input("Enter price:"))
addElectric(name,cost)
print(electric)
def allCost(costElectric):
    allSum=sum(electric.get(key,0)*amount for key,amount in costElectric.items())
    return allSum
costElectric={"watch":3,"tablet":2}
print(f"All:{allCost(costElectric)}")
def deleteElectric(name):
    if name in electric:
        del electric[name]
name=input("Enter name to delete:")
deleteElectric(name)
print(electric)
#4
d={1:1,2:1,3:2,'test': 1}
def delDuplicat(dict):
    makeSet=set()
    withoutDup={}
    for key, value in dict.items():
        if value not in makeSet:
            makeSet.add(value)
            withoutDup[key]=value
    return withoutDup
print(delDuplicat(d))
print("Hello!")
print("what is your name?")
print("GOOD day!")