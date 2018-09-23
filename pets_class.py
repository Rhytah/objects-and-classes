class Dog:
    def __init__(self,name,kind,age):
        self.name=name
        self.kind=kind
        self.age=age
        
    
     
    
               

class Pets:
    tom=Dog(name='Tom',kind='mammal',age=6)
    fletcher=Dog(name='Fletcher',kind='mammal',age=7)
    larry=Dog(name='Larry',kind='mammal',age=9)


    my_pets=[tom,fletcher,larry]
    print("I have three dogs")
    
    print ("And they're all mammals, of course.")

    
    