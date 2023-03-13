# Generation
dict1={'python':1,'html':2,'java':3}
dict2=dict(zip(['python','html','java'],[1,2,3]))
dict3=dict([['python',1],['html',2],['java',3]])
dict4=dict((('python',1),('html',2),('java',3)))
dict5={}.fromkeys(['python','html','java'],1) # In setting multiple keys to the same value
dict6={w:id(w) for w in range(6)}

# Access
print(dict1,dict2,dict3,dict4,dict5,dict6,end='\n',sep='\n')
print(dict1.get('python','Doesn\'t Exist.'))
print(dict1.get('c++','Doesn\'t Exist.'))

print(dict2.items())
print(dict2.keys())
print(dict2.values())

for i in dict3:
    print(i,end='\n')
for i in dict3.items():
    print(i,end='\n')
for i in dict3.values():
    print(i, end='\n') # There're changes of line to all of these
print()

# Update
dict4['java']=4
dict4['c++']=3
print(dict4)

print(dict5.setdefault('java',4)) # Already exists,change nothing and enter the original value
print(dict5.setdefault('c++',4)) # Didn't exist,add key and enter new value
print(dict5) # The only change is that key 'c++' is added

dict7={'vb':4,'php':5,'c++':6}
print(dict7)
dict7.update(dict1)
print(dict7)
dict7.update(dict5)
print(dict7)

del(dict6[3])
print(dict6)
del dict6[2]
print(dict6)
del dict6
try:
    print(dict6)
except NameError:
    print('Name error.')

dict8={}.fromkeys(['Alex','Ajax','Brandon','Clint','Drake','Dimitri'],23)
print(dict8.pop('Bob','Doesn\'t exist')) # Didn't exist,enter given value
print(dict8.pop('Drake','Doesn\'t exist')) # Already exists,erase the key and enter the original value
print(dict8)# Method 'pop' has a similar pattern as mathod 'setdefault'

dict1.clear()
print(dict1)
