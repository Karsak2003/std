
#region IMPORTS
import random
import res
#endregion IMPORTS

def main() -> None:
    numbers = random.sample(range(0, 10), 4)
    
    print("\n".join(res.openName))
    
    print(numbers)
    print("\n".join(res.bull))
    print("\n".join(res.cow))
    
    pass

if __name__ == "__main__":main()