
#region IMPORTS
import random
from resource import s_Wordle 
#endregion IMPORTS



def main() -> None:
    word:str = random.choice(s_Wordle.words)
    print(word)
    pass

if __name__ == "__main__":main()