# Generation
lt1=[1,2,3,4,5,6,7,8,9,10,11]
lt2=list('python.javascript.html')
lt3=list(range(1,7))
lt4=[[1,2],[3,3],[6,7],[33,4],[24,1],[63,39]]

# Access
print(lt1,lt2,lt3,lt4,end='\n',sep='\n')
print(lt1[0:5])
print(lt2[0:-7])
print(lt3[:])
print(lt4[5][1])
for index1 in range(len(lt4)):
    for index2 in range(len(lt4[index1])):
        print(lt4[index1][index2],end=' ')
    print()

# Assignment
lt5=lt1
lt5[3:7]=[4,5,6,7]
print(lt1,lt5,end='\n') 
print(id(lt1),id(lt5)) # The storing address of two lists with the same contents are the same

# Variation
lt1.append(23)
print(lt1)
lt2.remove('p')
print(lt2)
lt3.insert(2,'lemon')
print(lt3)
del lt5[3]
print(lt5)
lt5.pop()
print(lt5)

# Additional Functions
import random
random.shuffle(lt5)
print(lt5)
print(sorted(lt5))
print(sum(lt5))
print()
