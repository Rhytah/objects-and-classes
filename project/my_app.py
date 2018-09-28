import re

class User:
    def __init__(self):
        self.accounts=[]
        self.user={}
        

    def signup(self, name, username,age,email,password, gender, status="inactive"):
        self.user=dict(
            name= name,
            username= username,
            age=age,
            email=email,
            password=password,
            gender =gender,
            status = "inactive"
        )
        

                    
        if username==name or len(username) < 4 :
            raise ValueError("Username should be different from name and not less than 4 characters")
            

        if type(age) != int or age < 0:
            raise ValueError("Age should be a number higher than 0")
           
        if not gender in ["female", "male"]:
            raise ValueError("Gender should be male or female")

        if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
            raise ValueError("Please use valid email format, john@mail.com")

        if not re.match(r'[A-Za-z0-9@#$%^&+=]{4,}', password):
            raise ValueError("Password should be at least 4 characters, contain a capital letter, a small letter,a digit and a special character")

        
        self.accounts.append(self.user)
    
    def login(self,Username,password):
    
       
        for user in self.user:
            username=user['username']
            password=user['password']
            if username == user['username'] and password == user['password']:
                print("{} you are logged in.".format(username))
                return True
            



# if __name__=='__main__':
#     user =User()
#     # user.signup(name,username,age,email,password,gender)
#     user.login()