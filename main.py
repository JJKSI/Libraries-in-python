import pandas as pd
import xlsxwriter

s='phone directory'
print(s.center(50))

l={
           'darsh': 1212121212,
           'vandan': 1212121,
           'jenny': 121212,
           'aaa': 11212,
           'bbb': 212,
           'ccc': 12,
           'ddd': 1,

   }


df=pd.DataFrame(data=l,index=[1])
df.to_excel('l.xlsx')



for i in l:
    print(i)

def search():
     a = input('enter the named to be search')
     if a in l:
        print('given contact for seacrhed name is',l[a])
     else:
         print('sorrry we cant find the name')



def add_contact():
     b=input('enter the name you want to add in contact')
     c=int(input('enter the number'))
     l[b]=c
#
#


def delete():
     b=input('name you want to delete')
     del l[b]
print(l)



def edit():
     x=input('enter name u want to update')

     if x in l:
       z=input('editt the number')
       l[x]=z
       print('updated')
     else:
       print('sorry no contacts available')



flag=input("enter 1 2 3 4 5")
if flag=='1':
    search()
    print(l)
elif flag=='2':
    edit()
    print(l)
elif flag=='2':
    delete()
    print(l)
elif flag=='2':
    add_contact()
    print(l)



df=pd.DataFrame(data=l,index=[1])
df.to_excel('rrrrrr.xlsx')



