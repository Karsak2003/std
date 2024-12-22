
#region IMPORTS
import random
#endregion IMPORTS


ScoreCounter:int = 0 
#// WinRate:int = 2 
NumGames:int = 3

Matrix:list[str] = ["0PC", "C0P", "PC0"]

RSP:list[str] = ["✂️","🪨","🗞️"]

"""
✂️🪨🗞️
 0 1 2

 012P
00PK
1K0P 
2PK0
C

"""

def getCombination() -> list[int]:
    selectCombo:list[int] = []
    for _ in range(NumGames):
        selectCombo.append( random.randint(0, len(RSP)-1))
    return selectCombo

def SelectTool() -> int:
    while True:    
        try:
            print("Выберете из ниже перечисленых:")
            print("1.✂️ : Ножницы ")
            print("2.🪨 : Камень ")
            print("3.🗞️ : бумага ")
            tempStr:str = input("Введите номер: ")
            assert tempStr.isnumeric()
            assert 1 <= int(tempStr) <= 3
            print("\033[F"*5, "\033[J")
            return int(tempStr) - 1
        except:
            print("\033[F"*5, "\033[J", end="")
            print("Неверно введено значение!")
            input("Нажмите 'ENTER' для продолжения...")
            print("\033[F\033[F\033[J", end="")
            continue

def contrast(a:int, b:int) -> str:
    global ScoreCounter
    temp:str = Matrix[a][b]
    if temp == "P":
        ScoreCounter+=1
        print("Выиграл Игрок!")
    if temp == "C":
        ScoreCounter-=1
        print("Выиграл Компьютер!")
    if temp == "0":print("Ничья!")
    pass

def main() -> None:
    input("Нажмите 'ENTER' для продолжения...")
    print("\033[F\033[K")
    for item in getCombination():
        pItem:int = SelectTool()
        print(f"Игрок выбрал:{RSP[pItem]}")
        print(f"Компьютер выбрал:{RSP[item]}")
        contrast(item, pItem)
        input("Нажмите 'ENTER' для продолжения...")
        print("\033[F"*5,"\033[J", end="")
    #// print(ScoreCounter)
    if ScoreCounter > 0:
        print("Выиграл Игрок!")
    elif ScoreCounter < 0:
        print("Выиграл Компьютер!")
    else: print("Ничья!")
        

if __name__ == "__main__":main()