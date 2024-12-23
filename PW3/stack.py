
#region IMPORT
from typing import Any

#endregion IMPORT


class MyStack():
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
        return self.__listObjects__.pop()
        
    def __call__(self, *args) -> Any|None:
        """При вызове может вернуть либо занчение, либо дабавить заначение.\n
        Если args пустое, то вернёт последний элемент, иначе добавит значения из args.
        """
        if len(args):
            self.add(*args)
            return None
        else: return self.pull()
    
    def __len__(self) -> int: return len(self.__listObjects__)
    
    def __str__(self) -> str:
        return " ".join(list(map(str, self.__listObjects__))) if self.__len__() else None
    

def main() -> None:
    test:MyStack = MyStack()
    test.add("a", 1, 1.2)
    print(test)
    print(f"из '{test}' вытащали '{test.pull()}' получили '{test}'")
    print(test())
    test(*input("Введите что-либо: ").split())
    print(test)
    print(len(test))
    pass

if __name__ == "__main__":main()