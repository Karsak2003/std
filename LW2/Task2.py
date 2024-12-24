''' 
2. Реализовать в консоли трекер бюджета через классы. Данные хранить в
объекте во время работы программы, выгружать список задач в JSON-файл,
при запуске загружать файл (используя модуль  json). Реализовать
возможность ввода произвольной строки с описанием операции и суммой
расхода/дохода, возможность ввода произвольных категорий. Бонус:
установка лимитов на категории.
'''
#region IMPORTS
import json
#endregion IMPORTS


class MyTask():
    def __init__(self, name:str, description:str, type_:str = None) -> None:
        self.name:str = name
        self.description:str = description
        self.isDone:bool = False
        self.type_:str = type_
        

    def toDo(self) -> None: self.isDone = True

class MyTaskTracker():
    def __init__(self) -> None:
        self.__TaskList:list[MyTask] = []
    
    