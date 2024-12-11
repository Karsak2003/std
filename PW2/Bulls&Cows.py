
#region IMPORTS
import random
#endregion IMPORTS

def eqaNum(firs:list[int], sect:list[int]) -> tuple[int, int, bool]:
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
            
        

class s_BullsCows:
    openName = [
    r"  ________  ___  ___  ___       ___       ________           ________  ________   ________          ________  ________  ___       __   ________       ",
    r" |\   __  \|\  \|\  \|\  \     |\  \     |\   ____\         |\   __  \|\   ___  \|\   ___ \        |\   ____\|\   __  \|\  \     |\  \|\   ____\      ",
    r" \ \  \|\ /\ \  \\\  \ \  \    \ \  \    \ \  \___|_        \ \  \|\  \ \  \\ \  \ \  \_|\ \       \ \  \___|\ \  \|\  \ \  \    \ \  \ \  \___|_     ",
    r"  \ \   __  \ \  \\\  \ \  \    \ \  \    \ \_____  \        \ \   __  \ \  \\ \  \ \  \ \\ \       \ \  \    \ \  \\\  \ \  \  __\ \  \ \_____  \    ",
    r"   \ \  \|\  \ \  \\\  \ \  \____\ \  \____\|____|\  \        \ \  \ \  \ \  \\ \  \ \  \_\\ \       \ \  \____\ \  \\\  \ \  \|\__\_\  \|____|\  \   ",
    r"    \ \_______\ \_______\ \_______\ \_______\____\_\  \        \ \__\ \__\ \__\\ \__\ \_______\       \ \_______\ \_______\ \____________\____\_\  \  ",
    r"     \|_______|\|_______|\|_______|\|_______|\_________\        \|__|\|__|\|__| \|__|\|_______|        \|_______|\|_______|\|____________|\_________\ ",
    r"                                            \|_________|                                                                                 \|_________| ", 
    ]
    cow = [
    r"                 ",
    r"  ,/         \,  ",
    r" ((__,-'''-,__)) ",
    r"  `--)~   ~(--`  ",
    r" .-'(       )`-, ",
    r" `~~`d\   /b`~~` ",
    r"     |     |     ", 
    r"     (6___6)     ",
    r"      `---`      ",
    ]
    bull = [
    r"  ,           ,  ",
    r" /             \ ",
    r"((__-^^-,-^^-__))", 
    r" `-_---' `---_-' ", 
    r"  <__|o` 'o|__>  ",  
    r"     \  `  /     ",   
    r"      ): :(      ",    
    r"      :o_o:      ",   
    r'       "-"       ',      
    ]
    space = [
    r"                 ",
    r"                 ",
    r"                 ",
    r"                 ",
    r"                 ",
    r"                 ",
    r"                 ",
    r"                 ",
    r"                 ",
    ]
    zero = [
    r"                 ",
    r" ________        ",
    r" |\   __  \      ",
    r" \ \  \|\  \     ",
    r"  \ \  \\\  \    ",
    r"   \ \  \\\  \   ",
    r"    \ \_______\  ",
    r"     \|_______|  ",
    r"                 ",
    ]
    one = [
    r"                 ",
    r"   _____         ",                                                       
    r"  / __  \        ",                                                       
    r" |\/_|\  \       ",                                                       
    r" \|/ \ \  \      ",                                                       
    r"      \ \  \     ",                                                       
    r"       \ \__\    ",                                                       
    r"        \|__|    ",  
    r"                 ",                                                     
    ]                                                              
    two = [
    r"                 ",
    r"   _______       ",
    r"  /  ___  \      ",
    r" /__/|_/  /|     ",
    r" |__|//  / /     ",
    r"     /  /_/__    ",
    r"    |\________\  ",
    r"     \|_______|  ",
    r"                 ",
    ]
    three = [
    r"                 ",
    r"  ________       ",
    r" |\_____  \      ",
    r" \|____|\ /_     ",
    r"       \|\  \    ",
    r"      __\_\  \   ",
    r"     |\_______\  ",
    r"     \|_______|  ",
    r"                 ",
    ]                                                                                                                        
    four = [
    r"                 ",
    r" ___   ___       ",                                                       
    r"|\  \ |\  \      ",                                                       
    r"\ \  \\_\  \     ",                                                       
    r" \ \______  \    ",                                                       
    r"  \|_____|\  \   ",                                                       
    r"         \ \__\  ",                                                       
    r"          \|__|  ", 
    r"                 ",
    ]                                                                                                                           
    nothing = [
    r"                                                                          ",
    r"  ________   ________  _________  ___  ___  ___  ________   ________      ",
    r" |\   ___  \|\   __  \|\___   ___\\  \|\  \|\  \|\   ___  \|\   ____\     ",
    r" \ \  \\ \  \ \  \|\  \|___ \  \_\ \  \\\  \ \  \ \  \\ \  \ \  \___|     ",
    r"  \ \  \\ \  \ \  \\\  \   \ \  \ \ \   __  \ \  \ \  \\ \  \ \  \  ___   ",
    r"   \ \  \\ \  \ \  \\\  \   \ \  \ \ \  \ \  \ \  \ \  \\ \  \ \  \|\  \  ",
    r"    \ \__\\ \__\ \_______\   \ \__\ \ \__\ \__\ \__\ \__\\ \__\ \_______\ ",
    r"     \|__| \|__|\|_______|    \|__|  \|__|\|__|\|__|\|__| \|__|\|_______| ",
    r"                                                                          ",
    ]         
    
    Congratulations = [
    r"  ________  ________  ________   ________  ________  ________  _________  ___  ___  ___       ________  _________  ___  ________  ________   ________  ___        ",
    r" |\   ____\|\   __  \|\   ___  \|\   ____\|\   __  \|\   __  \|\___   ___\\  \|\  \|\  \     |\   __  \|\___   ___\\  \|\   __  \|\   ___  \|\   ____\|\  \       ",
    r" \ \  \___|\ \  \|\  \ \  \\ \  \ \  \___|\ \  \|\  \ \  \|\  \|___ \  \_\ \  \\\  \ \  \    \ \  \|\  \|___ \  \_\ \  \ \  \|\  \ \  \\ \  \ \  \___|\ \  \      ",
    r"  \ \  \    \ \  \\\  \ \  \\ \  \ \  \  __\ \   _  _\ \   __  \   \ \  \ \ \  \\\  \ \  \    \ \   __  \   \ \  \ \ \  \ \  \\\  \ \  \\ \  \ \_____  \ \  \     ",
    r"   \ \  \____\ \  \\\  \ \  \\ \  \ \  \|\  \ \  \\  \\ \  \ \  \   \ \  \ \ \  \\\  \ \  \____\ \  \ \  \   \ \  \ \ \  \ \  \\\  \ \  \\ \  \|____|\  \ \__\    ",
    r"    \ \_______\ \_______\ \__\\ \__\ \_______\ \__\\ _\\ \__\ \__\   \ \__\ \ \_______\ \_______\ \__\ \__\   \ \__\ \ \__\ \_______\ \__\\ \__\____\_\  \|__|    ",
    r"     \|_______|\|_______|\|__| \|__|\|_______|\|__|\|__|\|__|\|__|    \|__|  \|_______|\|_______|\|__|\|__|    \|__|  \|__|\|_______|\|__| \|__|\_________\  ___  ",
    r"                                                                                                                                               \|_________| |\__\ ",
    r"                                                                                                                                                            \|__| ",
    ]
    
    def GET(s:str = " ") -> list[str]:
        assert type(s) is str
        s = s.lower()
        if s in "nothing": return s_BullsCows.nothing
        if s in "cow": return s_BullsCows.cow
        if s in "bull": return s_BullsCows.bull
        if s in " space": return s_BullsCows.space
        if s in "0zero": return s_BullsCows.zero
        if s in "1one": return s_BullsCows.one
        if s in "2two": return s_BullsCows.two
        if s in "3three": return s_BullsCows.three
        if s in "4four": return s_BullsCows.four
        if s in "opename": return s_BullsCows.four
        if s in "!congratulations!": return s_BullsCows.Congratulations
        raise ValueError                                                       
if __name__ == "__main__":main()