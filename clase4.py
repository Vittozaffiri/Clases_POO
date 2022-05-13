# encapsulamiento

class User:

    def __init__(self, username, password):

        self.__username = username
        self.__password = password

    @property
    def username(self):

        return self.__username
    
    @username.setter

    def username(self, value):

        if (self.__username == None):
            self.__username = value


    @property 
    def password(self):

        return "nunca te voy a dar la clave"


    @property 
    def password(self, value):

        if (value.length > 6):

            12




usr = User("admin","1234")

#print(usr.__password)

#usr.__password = "hola"

#print(usr.__password)

print(usr.username)

usr.username = "admin 2"

print(usr.username)








    