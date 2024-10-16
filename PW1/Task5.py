#
#region IMPORTS
import random as rnd
#endregion IMPORTS

def genDict(nameDict:str = "") -> dict:
    n = int(input(f"Введите длину словаря{(""," ")[len(nameDict)]+nameDict}: "))
    nDict = dict()
    print("Введите ключи и их значения: ")
    for _ in range(n):
        while True:
            key, val = (lambda x: (x[0], x[1]))(input("ключ и значение: ").split())
            if val.lower() in "randomrnd":val = rnd.randint(0, 100)
            try:
                nDict[key] = float(val)
                break
            except:
                input("Введено неверное значение!\nДля продолжения нажмите 'ENTER'/'ВВОД' ...")
    return nDict.copy()


def _main_() -> None:
    nDict_1 = genDict("'Первый'")
    print(nDict_1)
    nDict_2 = genDict("'Второй'")
    print(nDict_2)
    items = (lambda a, b:a-(a-b))(set(nDict_1.values()), set(nDict_2.values()))
    

    
    
    
    

if __name__ == "__main__": _main_()