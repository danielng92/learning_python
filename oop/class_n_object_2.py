class employee:
    def __init__(self,name:str,yob:int,id:int):
        self.name= name #local variable
        self.id= id
        self.yob= yob

    def age_calculator(self): # class method (encapsulation)
        return 2022-self.yob

if __name__ == "__main__":
    employee_1= employee("Daniel",1999,6969)#because of init, when declare all 3 properties as once
    print(employee_1.age_calculator())