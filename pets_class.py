class Dog:
    def __init__(self,name,kind,age, is_hungry=True):
        self.name=name
        self.kind=kind
        self.age=age
        # self.is_hungry=is_hungry

    def eat(self,is_hungry):
        if is_hungry==True:
            return False
        
        
    
class Pets:
    tom=Dog(name='Tom',kind='mammal',age=6, is_hungry=True)
    fletcher=Dog(name='Fletcher',kind='mammal',age=7,is_hungry=True)
    larry=Dog(name='Larry',kind='mammal',age=9,is_hungry=True)

    my_pets=[tom,fletcher,larry]
    
    # print("I have three dogs")
    # print ("{} is {}.".format(tom.name, tom.age))
    # print("{} is {}.".format(fletcher.name, fletcher.age))
    # print("{} is {}.".format(larry.name, larry.age))
    # print ("And they're all mammals, of course.")
    print ("I have 3 dogs.")
    is_hungry=True
    

    for pet in my_pets:    
        print(pet.name,"is",pet.age)
        pet.eat(is_hungry)
        # print("my dog is not hungry")
        # print(pet.kind)
    print ("And they're all mammals, of course.")
    print("My dogs are not hungry")
        
      
    

            

    
    