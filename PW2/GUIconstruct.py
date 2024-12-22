
#region IMPORTS
import time 

#endregion IMPORTS












"""
a
"""


@staticmethod
def main() -> None:
    _t:list[int] = [1, 3, 2, 6, 4, 5] 
    i:int = 0
    while True:
        print(f"\033[{30+_t[i%len(_t)]}mtest\033[0m")
        i+=1
        time.sleep(0.1)
        print("\033[F\033[F\033[J")
    


if __name__ == "__main__":main()