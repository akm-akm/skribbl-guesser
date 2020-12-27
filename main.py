import itertools,pyautogui,time, os
Alphabet = ("abcdefghijklmnopqrstuvwxyz")

def screen_clear():
   os.system("cls")

def pp(i):
     pyautogui.typewrite(i)
     pyautogui.typewrite("\n")

def CharLength(xxx):

    passwords = (itertools.product(Alphabet, repeat = xxx))
    counter = 1
    print("\n \n")
    for i in passwords:
        counter += 1
        i = str(i)
        i = i.replace("[", "")
        i = i.replace("]", "")
        i = i.replace("'", "")
        i = i.replace(" ", "")
        i = i.replace(",", "")
        i = i.replace("(", "")
        i = i.replace(")", "")
        print(i)
        time.sleep(2)
        pp(i)

while True:
    screen_clear()
    xxx= int(input("LENGTH >>"))
    print("\nCLICK ON A TEXT FIELD IN 5 SECOND")
    time.sleep(5)
    CharLength(xxx)	