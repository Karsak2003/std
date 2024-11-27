
#region IMPORTS
import random
from res import BullsCows
#endregion IMPORTS




def main() -> None:
    numbers = [random.randint(1, 10)] + random.sample(range(0, 10), 3)
    print("\n".join(BullsCows.openName))
    input("\n\n\nPlease press the 'ENTER' button to start the game...")
    while True:
        
        pass
    print(numbers)
    print("\n".join(BullsCows.bull))
    print("\n".join(BullsCows.cow))
    
    pass

if __name__ == "__main__":main()