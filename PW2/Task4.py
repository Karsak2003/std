"""
Написать функцию поиска всех делителей целого числа больше 0 и проверки
этого числа на то, является ли оно простым (ограничим до 100 тыс.)
"""
#region IMPORTS
import random 
#endregion IMPORTS

def findDiv(num:int) -> list[int]:
    divList:list[int] = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divList.append(i) 
            divList.append(num//i) if i != num//i else None
    return sorted(divList)

def isPrime(num:int) -> bool:
    return len(findDiv(num)) <= 2


def getValue() -> int:
    while True:
        try:
            strLine:str = input("Введите число: ")
            if strLine.lower() in "rndrandomрандом": return random.randint(1, 100000)
            assert strLine.isnumeric()
            assert 1 <= int(strLine) <= 100000
            return int(strLine)
        except:
            print("Неверно введено значения!")
            print("Введите значение занового.")
            input("Нажмите 'ENTER' для продолжения...")
            print("\033[F\033[F\033[F\033[J", end="")
            continue

def main() -> None:
    num:int = getValue()
    print("\033[F\033[J", end="")
    print(f"Все делители числа '{num}': \n", *findDiv(num))
    print(f"Данное число {("не являеться", "являеться")[isPrime(num)]} простым")







if __name__ == "__main__":main()