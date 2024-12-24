#region IMPORTS
import json
from datetime import datetime
#endregion IMPORTS

''' 
1 Реализовать в консоли таск-трекер через классы. Данные хранить в объекте
во время работы программы, выгружать список задач в JSON-файл, при
запуске загружать файл (используя модуль  json). Реализовать возможность
ввода произвольной строки с описанием задачи, возможность отметки
задания выполненным, возможность ввода произвольных категорий. Бонус
(опциональный): поиск по задачам; вывод всех задач в категории.
- [x] Задание выполнено #pstu
- [ ] Еще задача #work
- [ ] И еще задача #pstu
'''


class MyTask():
    def __init__(self, name:str, description:str|list[str], type_:str = None) -> None:
        self.Name:str = name
        self.Description:str|list[str] = description
        self.isDone:bool = False
        self.Type_:str = type_
        self.date:datetime = datetime.now()

    def toDo(self) -> None: self.isDone = True
    
    def __str__(self) -> str:
        temp_:str = f"""
[{(" ", "x")[self.isDone]}] {self.Name} #{self.Type_:}
{"\n".join(self.Description)}

{datetime.strftime(self.date, "%Y-%m-%d %H:%M:%S")}
"""
        return temp_

    def __repr__(self) -> str:
        temp_:str = "{" + f'''\n\
"Name":"{self.Name}",\n\
"Type":"{self.Type_:}",\n\
"Description":"{self.Description}",\n\
"isDone":"{("False","True")[self.isDone]}"\n
"date":"{datetime.strftime(self.date, "%Y-%m-%d %H:%M:%S")}"''' + "}"
        return temp_

    def toJSONType(self) -> dict:
        return {
            "Name":self.Name,
            "isDone":self.isDone,
            "Description":self.Description,
            "Type":self.Type_,
            "date":datetime.strftime(self.date, "%Y-%m-%d %H:%M:%S"),
        }
        
    def loadJSON(self, FileDataJSONType:dict) -> None:
        self.Name:str = FileDataJSONType["Name"]
        self.Description:str|list[str] = FileDataJSONType["Description"]
        self.isDone:bool = FileDataJSONType["isDone"]
        self.Type_:str = FileDataJSONType["Type"]
        self.date:datetime = datetime.strptime(FileDataJSONType["date"], "%Y-%m-%d %H:%M:%S")

def loadJSON(FileDataJSONType:dict) -> MyTask:
    Name:str = FileDataJSONType["Name"]
    Description:str|list[str] = FileDataJSONType["Description"]
    isDone:bool = FileDataJSONType["isDone"]
    Type_:str = FileDataJSONType["Type"]
    date:datetime = datetime.strptime(FileDataJSONType["date"], "%Y-%m-%d %H:%M:%S")
    temp:MyTask = MyTask(Name, Description, Type_)
    temp.date = date
    temp.isDone = isDone
    return temp
   
class MyTaskTracker():
    def __init__(self) -> None:
        self.__TaskList:list[MyTask] = []
        self.nameFile:str = "TaskTracker.json"
    
    def add(self, newTask:MyTask) -> None:
        self.__TaskList.append(newTask)
        pass
    
    def remove(self,ind:int) -> None:
        del self.__TaskList[ind]
    
    def load(self):
        pass
    
    def upload(self):
        with open(self.nameFile, "w+") as file:
            json.dump(self.__TaskList, file)
            pass
    
    def getTasks(self) -> list[MyTask]:
        return self.__TaskList

    def setNameFile(self, nameFile:str) -> None:
        pass



def main() -> None:
    test:MyTask = MyTask("testTask", "testDescription", "test")
    print(test)
    with open("test.json", "w+") as file:
        json.dump(test.toJSONType(), file)
    with open("test.json", "r+") as file:
        test.loadJSON(json.load(file))
        print(test)
        

if __name__ == "__main__":main()