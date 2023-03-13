class Ch_El:
    number=0
    __tempdefault = '20C'
    def __init__(self,name,atomic_number,code,coordinate0,coordinate1):
        self.name=name
        self.atomic_number=atomic_number
        self.code=code
        coordinate1=int(coordinate1)
        coordinate0=int(coordinate0)
        if coordinate1==1 and 1<=coordinate0<=2:
            self.coordinate=[coordinate0,coordinate1]
        elif 2<=coordinate1<=3 and 1<=coordinate0<=8:
            self.coordinate=[coordinate0,coordinate1]
        elif 4<=coordinate1<=5 and 1<=coordinate0<=18:
            self.coordinate=[coordinate0,coordinate1]
        elif 6<=coordinate1<=7 and 1<=coordinate0<=32:
            self.coordinate=[coordinate0, coordinate1]
        else:
            self.coordinate=[None,None]
        Ch_El.number+=1
    def info_element(self):
        return self.name,self.atomic_number,self.code,self.coordinate
    def Ar(self,k):
        self.Ar=k
        return k
em1= Ch_El('Hydrogen',1,'H',1,1)
em2 = Ch_El('Helium',2,'He',2,1)
em3 = Ch_El('Lithium',3,'Li',1,2)
em4 = Ch_El('Beryllium',4,'Be',2,2)
em5 = Ch_El('Boron',5,'B',3,2)
em6 = Ch_El('Carbon',6,'C',4,2)
em7 = Ch_El('Nitrogen',7,'N',5,2)
em8 = Ch_El('Oxygen',8,'O',6,2)
em9 = Ch_El('Florine',9,'F',7,2)
em10 = Ch_El('Neon',10,'Ne',8,2)
em11= Ch_El('Sodium',11,'Na',1,3)
em12= Ch_El('Magnesium',12,'Mg',2,3)
em13= Ch_El('Aluminium',13,'Al',3,3)
em14= Ch_El('Silicon',14,'Si',4,3)
em15= Ch_El('Phosphorous',15,'P',5,3)
em16= Ch_El('Sulfur',16,'S',6,3)
em17= Ch_El('Chlorine',17,'Cl',7,3)
em18= Ch_El('Argon',18,'Ar',8,3)
em19= Ch_El('Potassium',19,'K',1,4)
em20= Ch_El('Calcium',20,'Ca',2,4)
em21= Ch_El('Scandium',21,'Sc',3,4)
print(em17.info_element())
print(em1.Ar(1.008))
print(em1.Ar)

















