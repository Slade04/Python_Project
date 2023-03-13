# Class

# Generation
class Ch_El:
    number=0
    __tempdefault = '20C'
    def __init__(self,name,atomic_number,code,coordinate1,coordinate0):
        self.name=name
        self.atomic_number=atomic_number
        self.code=code
        coordinate1=int(coordinate1)
        coordinate0=int(coordinate0)
        if coordinate1==1 and 1<=coordinate0<=2:
            self.coordinate=[coordinate1,coordinate0]
        elif 2<=coordinate1<=3 and 1<=coordinate0<=8:
            self.coordinate = [coordinate1, coordinate0]
        elif 4<=coordinate1<=5 and 1<=coordinate0<=18:
            self.coordinate = [coordinate1, coordinate0]
        elif 6<=coordinate1<=7 and 1<=coordinate0<=32:
            self.coordinate = [coordinate1, coordinate0]
        else:
            self.coordinate=[None,None]
        Ch_El.number+=1
    def info_element(self):
        return self.name,self.atomic_number,self.code,self.coordinate
# Fabrication of objects
em1= Ch_El('Hydrogen',1,'H',1,1)
em2 = Ch_El('Helium',2,'He',1,2)
em3 = Ch_El('Lithium',3,'Li',2,1)
em4 = Ch_El('Beryllium',4,'Be',2,2)
em5 = Ch_El('Boron',5,'B',2,3)

# Access
print(em2.info_element())
a,b='em3',em3.name
print(f'The element with the atomic number of {a} is {b}')
print('The element with the atomic number of {} is {}'.format(a,b))
# Update feature
em1.Ar=1.008
em2.Ar=4.003
em3.Ar=6.941
em4.Ar=9.012
em5.Ar=10.81

print(em5.Ar)
del em4.Ar
try:
    print(em4.Ar)
except AttributeError:
    print('Attribute doesn\'t exist.')
em4.Ar=16.00

# Public and private methods
# They are separated by their ways of being accessed(latter being more intimate)

class book:
    number=0 # Public attribute (of the class)
    __ones_I_like=0 # Private attribute (of the class)
    def __init__(self,name,author,price): # Public method (of the class)
        self.name= name # Public attribute (of the object)
        self.author=author
        self._price=price # Private attribute (of the object)
        book.number+=1
        if price!=int(price):
            book.__ones_I_like+=1
    def display(self):# Public method (of the class)
        return [self.name,self.author,self._price]
    def __I_LIKE(self):
        return book.__ones_I_like
book1=book('example1','me',30.01)
print(book1.display())
print(book.number)
print(book._book__ones_I_like) # Private access of an attribute (of the class)

# Class and static methods
class Bird:
    eyes = "two"
    def __init__(self,name, color):
        self.color = color
        self.name=name
    def call(self,cd):
        print("This bird:",cd)
    @classmethod # Able to access class attributes
    def Class_call(cls,cd):
        print('This bird:',cd)
    @staticmethod # Unable to access class attributes
    def Static_call(): # That's why it's empty
        print('This is a bird.')
bird1 = Bird('xique',"green")
bird1.call("gezhi")
bird1.Class_call("gezhi")
bird1.Static_call() # Although no attribute accessed, bird1 being a Bird made this function able to work

# Inheritance
class Ch_Cp:
    number=0
    def __init__(self,name,Ch_El,Mr,code):
        self.name=name
        self.Ch_El=Ch_El
        self.Mr=Mr
        self.code=code
        self.number+=1
class Acid(Ch_Cp):
    number=0
    def __init__(self,name,Ch_El,Mr,code,Chloro_ion):
        Ch_Cp.__init__(self,name,Ch_El,Mr,code)
        self.number+=1
        self.Chloro_ion=Chloro_ion
    def display(self):
        return [self.name,self.Ch_El,self.Mr,self.code,self.Chloro_ion]
cp1=Acid('sulphuric acid',['H','O','S'],98,'H2SO4','SO4^2-')
print(cp1.display())