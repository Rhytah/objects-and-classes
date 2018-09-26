class User:
    def __init__(self):
        self.accounts=[]
        self.user={}
        self.status=False
    def signup(self, name, username,age,email,password, gender):
        self.user=dict(
            name= name,
            username= username,
            age=age,
            email=email,
            password=password,
            gender =gender,
            # status = status
        )
        
                    
        if username==name :
            raise ValueError("Username should be different form name and not less than 4 characters")
            # return {"Error":"username cannot be the same as name or less than 4 characters"}

        if age ==str or age <0:
            raise ValueError("Age should be a number higher than 0")
            #  return {"Error":"Age cannot be a character or less than 0"}
        if gender !="female" and gender != "male":
            raise ValueError("Gender should be male or female")
        user=(name,username,age,email,password,gender)
        self.accounts.append(user)



# if __name__=='__main__':
#     user=User()

#     user.signup(name,username,age,email,password,gender)
