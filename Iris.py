import sys
from time import sleep

def print_lyrics():
    lines = [
        ("And I'd give up forever to touch you", 0.09),
        ("Cause I know that you feel me somehow", 0.11),
        ("You're the closest to heaven that I'll ever be", 0.11),
        ("And I don't wanna go home right now", 0.1),
        ("And all I could taste is this moment", 0.13),
        ("And all I can breathe is your life", 0.12),
        ("And sooner or later, it's over", 0.09),
        ("I just don't wanna miss you tonight", 0.05),
        ("And I don't want the world to see me", 0.05),
        ("'Cause I don't think that they'd understand", 0.06),
        ("When everything's made to be broken", 0.05),
        ("I just want you to know who I am", 0.08),
    ]
    
    delays = [0.3, 0.3, 0.3, 0.8, 1, 1, 1.7, 2.7, 2.7, 2.7, 2.7, 2.7] 
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        sleep(delays[i])
        print("")

print_lyrics()
