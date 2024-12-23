
class Task():
    def __init__(self, name:str, description:str, type_:str = None) -> None:
        self.name:str = name
        self.description:str = description
        self.isDone:bool = False
        self.type_:str = type_
        pass