import numpy as np

a = [2, 3, 4, 5, 6, 7]

print(a)
print(type(a))# this is list
b=np.array([1,2,3,4,45,5,5,5,])
print(b)
#now this is array it wil be one dimtntona array
print(type(b))

c=np.array([[1,2,3],[4,5,6]])# this is two dimenstional array
print('lenght of array c?',len(c))

# the length of c will be two because there are two objects(list) inside the 2 d array
#x.ndim will give the dimensiontional of the array

# we use numpy because it is quite faster in terms of computation in comparison of lists,tuples,loops etc

print('shape of the c aarray',c.shape)#it gives the shapes of the array that is no. rows and cols


d=np.array([[1,2,3,4,5,6],
            [6,7,8,9,10,44]])
#accessing specific elements inside numpy
print('the array is',d)
print(d[0,5])#0th row that is first element and its 5th element will be printed

print(d[1,3])

print(d[:,0])# this will give me sepcific column
print('the fourth column is',d[:,3])


#changin the value

d[1,5]=400
d[0,0]=100
print('new array after chaninging the vaulue\n',d)

#np.zeros give and create a array with zero element
#np.ones same like that of zeroonly difference is elements will be 1
x=20
y=np.full((4,4),x)
print(y)# creates a full array of numbers you wan to pass

print(np.random.randint(1,99,size=(5,5)))# here 1 , 99  is the range and the numbers inside the array will be between these two values

e=np.array([
[1,2,3,4,5],
[133,233,333,433,533],
[1,22,33,3344,55],
[10,20,30,40,50],
[19,28,35,43,521],
[111,2222,3333,4444,555],
])
print(e)


print(e[0:3,1:5])# first 3 rows with last 4 columns

