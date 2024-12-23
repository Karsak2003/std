
#region IMPORT
from typing import Any

#endregion IMPORT


class MyQueue():
    def __init__(self, defList:list = None):
        self.__listObjects__:list = [] if defList is None else defList
    
    def add(self, *objs) -> None:
        for item in objs:
            self.__listObjects__.append(item)
    
    def pull(self) -> Any:
        """Возрощает первый добавленный элемент из очереди

        Returns:
            Any: Возрощаемый элемент
        """
        return self.__listObjects__.pop(0)
        
    def __call__(self, *args) -> Any|None:
        """При вызове может вернуть либо занчение, либо дабавить заначение.\n
        Если args пустое, то вернёт первый элемент в очереди, иначе добавит в очередь значения из args.
        """
        if len(args):
            self.add(*args)
            return None
        else: return self.pull()
    
    def __len__(self) -> int: return len(self.__listObjects__)
    
    def __str__(self) -> str:
        return " ".join(list(map(str, self.__listObjects__)))
    
    def __add__(self, other):
        if type(other) is tuple: return MyQueue(self.__listObjects__ + list(other)) 
        return MyQueue(self.__listObjects__ + [other])
    
    

def main() -> None:
    test:MyQueue = MyQueue()
    test.add("a", 1, 1.2)
    print(test)
    print(f"из '{test}' вытащали '{test.pull()}' получили '{test}'")
    print(test())
    test(*input("Введите что-либо: ").split())
    print(test)
    print(len(test))
    pass

if __name__ == "__main__":main()