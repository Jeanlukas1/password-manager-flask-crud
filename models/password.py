class Password:
    def __init__(self, id:int, name:str, password:str) -> None:
        self.id = id
        self.name = name
        self.password = password
        
    def to_dict(self):
        return  {
            "id": self.id,
            "name": self.name,
            "password": self.password
        }