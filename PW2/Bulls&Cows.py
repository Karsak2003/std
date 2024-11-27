
#region IMPORTS
import random
import res
#endregion IMPORTS




def main() -> None:
    numbers = [random.randint(1, 10)] + random.sample(range(0, 10), 3)
    print("\n".join(res.openName))
    input("\n\n\nPlease press the 'ENTER' button to start the game...")
    while True:
        
        pass
    print(numbers)
    print("\n".join(res.bull))
    print("\n".join(res.cow))
    
    pass

if __name__ == "__main__":main()