#
#region IMPORTS
import random as rnd
#endregion IMPORTS


def _main_() -> None:
    print("Введите 2 равных по длине списка чисел или слово 'RANDOM'")
    n1:list[str] = list(input("Список:").lower().split())
    if n1[0] in "randomrnd":
        temp:list[str] = list(map(int, input("Введите диапазон (левый и правый края) и длину списка - необходимо з числа:\n").split()))
        r, l = min(temp[0], temp[1]), max(temp[0], temp[1])
        n1:list[str] = [str(rnd.randint(min(l, r), max(l, r))) for _ in range(temp[-1])]
        print(f"Исходный список: {" ".join(n1)}")
    n2:list[str] = list(input("Список:").lower().split())
    if n2[0] in "randomrnd":
        temp = list(map(int, input("Введите диапазон (левый и правый края) и длину списка - необходимо з числа:\n").split()))
        r, l = min(temp[0], temp[1]), max(temp[0], temp[1])
        n2:list[str] = [str(rnd.randint(r, l)) for _ in range(len(n1))]
        print(f"Исходный список: {" ".join(n2)}")
    
    a = [(n1[i], n2[i])[i % 2] for i in range(len(n1))]
    print(f"Итоговый список: {" ".join(a)}")

if __name__ == "__main__": _main_()