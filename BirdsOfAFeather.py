import sys
from time import sleep

def print_lyrics():
    lines = [
        ("Birds of a feather, we should stick together, I know", 0.08),
        ("I said I'd never think I wasn't better alone", 0.08),
        ("Can't change the weather, might not be forever", 0.08),
        ("But if it's forever, ", 0.08),
        ("It's even better. . . ", 0.10),
        ("And I don't know what I'm cryin' for", 0.09),
        ("I don't think I could love you more", 0.10),
        ("It might not be long, but baby, I . . .", 0.08),
        ("I'll love you 'til the day that I die", 0.08),
        ("Til the day that I die", 0.08),
        ("Til the light leaves my eyes", 0.08),
        ("Til the day that I die", 0.08),
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
