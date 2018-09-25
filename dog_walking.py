from pets_class import  Dog
class Move(Dog):
    def __init__(self,name,kind,age):
        self.name=name

tom=Dog(name='Tom',kind='mammal',age=6)
fletcher=Dog(name='Fletcher',kind='mammal',age=7)
larry=Dog(name='Larry',kind='mammal',age=9)

pet_list=[tom,fletcher,larry]

for pet in pet_list:
    pet.walk()
    print("{} is walking!".format(pet.name))
