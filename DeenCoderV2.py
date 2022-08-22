#DeenCoder2 By username8bit 
import os
import datetime

now = datetime.datetime.now()

print(f""" _____    ______   ______   _   _    _____    ____    _____    ______   _____  
|  __ \  |  ____| |  ____| | \ | |  / ____|  / __ \  |  __ \  |  ____| |  __ \  login time: {"%s/%s/%s %s:%s:%s" % (now.month,now.day,now.year,now.hour,now.minute,now.second)}
| |  | | | |__    | |__    |  \| | | |      | |  | | | |  | | | |__    | |__) | email the creator @: deencodergit@gmail.com
| |  | | |  __|   |  __|   | . ` | | |      | |  | | | |  | | |  __|   |  _  /  github - https://github.com/BREKKKEN/DeenCoder
| |__| | | |____  | |____  | |\  | | |____  | |__| | | |__| | | |____  | | \ \  Developed by username8bit on github
|_____/  |______| |______| |_| \_|  \_____|  \____/  |_____/  |______| |_|  \_\ [DeenCoder2 v0.1]
------------------------------------------------------------------------------------------------------------------------------""")

win1 = "DeenCoder-main"

while True:
 os.system(f"title {win1}")

 MORSECODEDICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

 MORSE_TO_ENGLISH = {}
 for key, value in MORSECODEDICT.items():
    MORSE_TO_ENGLISH[value] = key
    
 def english_to_morse(message):
    morse = []
    for char in message:
        if char in MORSECODEDICT:
            morse.append(MORSECODEDICT[char])
        
    return " ".join(morse)
    
 def morse_to_english(message):
    message = message.split(" ")
    english = []
    for code in message:
        if code in MORSE_TO_ENGLISH:
            english.append(MORSE_TO_ENGLISH[code])
    return " ".join(english)

 def banner():
    print("""
[1] Convert Morse To English 
[2] English To Morse
[3] Show morse chart
[4] Exit
          """)

 def main():
    while True:
        banner()
        response = input("?~ ")
        if response == "1" or response == "2" or response == "3" or response == "4":
            break
    
    if response == "1":
        print("")
        print("Enter Morse Code: ")
        morse = input("> ")
        english = morse_to_english(morse)
        print("")
        print("MORSE TO ENGLISH:")
        print(english)
    
    elif response == "2":
        print("")
        print("Enter English Text: ")
        english = input("> ").upper()
        morse = english_to_morse(english)
        print("")
        print("ENGLISH TO MORSE:")
        print(morse)
    
    elif response == "3":
        print("")
        print("""A	.-	B	-...
C	-.-.	D	-..
E	.	F	..-.
G	--.	H	....
I	..	J	.---
K	-.-	L	.-..
M	--	N	-.
O	---	P	.--.
Q	--.-	R	.-.
S	...	T	-
U	..-	V	...-
W	.--	X	-..-
Y	-.--	Z	--..
0	-----	1	.----
2	..---	3	...--
4	....-	5	.....
6	-....	7	--...
8	---..	9	----.""")
    
    elif response == "4":
       print('')
       print("Are you sure you want to exit?")
       exi = input("(y)/(n): ")
       if exi == 'y':
         exit()
       if exi == 'n':
            ()

 if __name__ == "__main__":
    main()