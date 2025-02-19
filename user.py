class User:
    def __init__(self, user, user_id, name, surname , email, password, birthday ):
     self.user_id = user_id
     self.name = name
     self.surname = surname
     self.__password = password
     self.birthday = birthday


    def get_details(self):
        return self.user_id , self.name, self.surname, self.__password, self.birthday

    def  get_age(self):
        return 2025 - int(self.birthday[-4:])