from abc import ABC, abstractmethod


class User(ABC):

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass


class AdminUser(User):
    def __init__(self, user1):
        self.user1 = user1

    def get_role(self):
        return "Admin"

    
    def has_permission(self, permission):
        return True

class RegularUser(User):
    def __init__(self, user2):
        self.user2 = user2

    def get_role(self):
        return "Regular"
    
    def has_permission(self, permission):
        if permission == "read":
            return True
        
        else:
            return False
        


user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")

print(user1.has_permission("delete"))  # True
print(user2.has_permission("delete"))  # False