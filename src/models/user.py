from abc import ABC, abstractmethod

class User(ABC):

  def __init__(self,user_id: str, name:str, email:str):
    #encapsulation: protected attributes
    self._user_id = user_id
    self._name = name
    self._email = email
  
#   #encapsulation using @property decorators (getters)
  @property  
  def user_id(self) -> str:
    """Getter for user_id - makes it read-only from the outside."""
    return self._user_id

#   @property
#   def name(self) -> str:
#     return self._name

#   @property
#   def email(self) -> str:
#     return self._email

#   @abstractmethod
  def get_role_permissions(self) -> list[str]:
    """polymorphic method to be overriden by subclasses."""
    return []
#   def to_dict(self) ->dict:
#     """helper to serialize object state for json storage."""
#     return {
#       "user_id": self._user_id,
#       "name":self._name,
#       "email":self._email,
#       "role": self.__class__.__name__
#     }
  
class Customer(User):
  """Represents a regular customer who ca make bookings"""

  def __init__(self, user_id : str, name: str, email: str):
    super().__init__(user_id, name, email)

  def get_role_permissions(self) -> list[str]:
    return["VIEW_RESOURCES","CREATE_RESERVATIONS","CANCEL_OWN_RESERVEATIONS"]

class Admin(User):
  """represents an admin who manages resources and all bookings"""

  def __init__(self, user_id:str, name:str, email:str):
    super().__init__(user_id, name, email)

  def get_role_permissions(self) -> list[str]:
    return ["VIEW_RESOURCES", "CREATE_RESERVATIONS","CANCEL_ANY_RESERVATION","ADD_RESOURCE","REMOVE_RESOURCE"]

def get_info(self) -> str:
    return f"user_id: {self._user_id}, name:{self._name}, email:{self._email}"