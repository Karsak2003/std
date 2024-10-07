#
#region IMPORTS
import random as rnd
#endregion IMPORTS


def _main_() -> None:
    n = int(input("Введите длину словаря: "))
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
    print(nDict)
    print()
    a = [(item, [i[0] for i in sorted(list(nDict.items()), key=(lambda x: x[1])) if i[1]==item]) for item in set(nDict.values())]
    print(a)
    

if __name__ == "__main__": _main_()