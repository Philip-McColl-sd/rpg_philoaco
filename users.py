import json

class user_manager: 
    '''
    Manages user information using json database
    
    Attributes
    ----------------
    self.name: str
        name of the user
    self.password: str
        password of the user

    Methods
    -------
    '''

    def __init__(self, name, password) -> None:
        self.name = name
        self.password = password
    
    def logger(self) -> None:
        pass
        