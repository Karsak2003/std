
#region IMPORTS
import random
from PW2.resource import s_BullsCows 
#endregion IMPORTS

def eqaNum(firs:list[int], sect:list[int]) -> tuple:
    cow:int = 0 
    bull:int = 0
    
    for i in range(4):
        for j in range(4):
            if firs[i] == sect[j]:
                if i == j:cow+=1
                else:bull+=1
    
    n:bool = not (cow or bull)
    return cow, bull, n


def main() -> None:
    numbers = [random.randint(1, 10)] + random.sample(range(0, 10), 3)
    print("\n".join(s_BullsCows.openName))
    input("\n\n\nPlease press the 'ENTER' button to start the game...")
    print("\033[H\033[J", end="")
    while True:
        numFD:list[int] = []
        try:
            numFD = list(map(int ,input("Enter a four-digit number: ")))
            assert len(numFD) == 4 
        except:
            input("The value was entered incorrectly! To continue, press 'ENTER'...")
            continue
        _t = eqaNum(numbers, numFD)
        c:int = _t[0]
        b:int = _t[1] 
        n:bool = _t[2]
        del _t
        print("You see the following:")
        if n: print("\n".join(s_BullsCows.nothing))
        else:
            out_c:list[str] = [item[0] + " " + item[1] for item in  zip(s_BullsCows.GET(str(c)), s_BullsCows.cow)]
            out_b:list[str] = [item[0] + " " + item[1] for item in  zip(s_BullsCows.GET(str(b)), s_BullsCows.bull)]
            out:list[str] = [item[0] + " " + item[1] + " " + item[2] for item in  zip(out_c,s_BullsCows.GET(" ") , out_b)]
            print("\n".join(out))
            del out_c, out_b, out
        if c == 4: 
            print("\033[H\033[J", end="")
            print("\n".join(s_BullsCows.GET("!")))
            input("\n\n\nPlease press the 'ENTER' button to continue...")
            break
            
        


if __name__ == "__main__":main()