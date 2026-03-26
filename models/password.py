class Password:
    def __init__(self, id:int, name:str, password) -> None:
        self.id = id,
        self.name = name,
        self.password = password
        
    def to_dict(self):
        return  {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }