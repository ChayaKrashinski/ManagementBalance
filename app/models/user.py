from pydantic import BaseModel

class User(BaseModel):
    """
     Represents a user in the system.

     Attributes:
     - id (int): The unique identifier for the user.
     - name (str): The name of the user. Default is an empty string.
     - password (str): The password of the user. Default is an empty string.
     - mail (str): The email address of the user. Default is an empty string.
     """
    id:int
    name: str = ""
    password: str = ""
    mail: str = ""

