#
#region IMPORTS
import random as rnd
#endregion IMPORTS


def _main_() -> None:
    print("Введите список чисел или слово 'RANDOM'")
    n = list(input("Список:").lower().split())
    if isinstance(n[0], int) and (not n[0] in "randomrnd"):
        print(f"Исходный список: {" ".join(n)}")
        print(f"обратный список: {" ".join(n[::-1])}")
    else:
        l, r, c = map(int, input("Введите диапазон (левый и правый края) и длину списка - необходимо з числа:\n").split())
        a = [str(rnd.randint(min(l, r), max(l, r))) for _ in range(c)]
        print(f"Исходный список: {" ".join(a)}")
        print(f"обратный список: {" ".join(a[::-1])}")

if __name__ == "__main__": _main_()