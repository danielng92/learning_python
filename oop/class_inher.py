class veh:

    def __init__(self,make:str,color:str,model:str):
        self.make=make
        self.color=color
        self.model=model
    
    def print_detail(self):
        print(self.make,self.color,self.model)
    
    def is_flying(self):
        return "is able to fly to everywhere"

class car(veh):

    def __init__(self,make:str,color:str,model:str,type:str,eng:str):
        super().__init__(make,color,model) #inherit from veh class
        self.type=type
        self.eng=eng

    def printCartype(self):
        super().print_detail() #Inherited method from vehcile class
        print(self.type,self.eng)

class plane(veh):

   def __init__(self,make:str,color:str,model:str,wings:int,ori:str):
       super().__init__(make,color,model)
       self.wings=wings
       self.ori=ori

   def planeIn4(self):
       print("This",self.ori,super().is_flying())

if __name__ == "__main__":
    #veh1=veh("toyota","white","corolla")
    #veh1.print_detail()
    #car1=car("mersu","red","c class","sedan","diesel")
    #car1.printCartype()
    plane1=plane("airbus","red","370",2,"Russia")
    plane1.planeIn4()
