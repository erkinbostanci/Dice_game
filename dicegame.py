while True:
    dicecont = input ('Enter Command ')
    from random import randint
    if dicecont == '/dicegame':
        while True:
            try:
                diceside = input("How many faces want on dice ?: ")
                intdice = int(diceside)
                face = randint(1, intdice)
                print(f'{intdice} on face comming number :{face}')
                input('Press enter for quit')
                break
            except:
                print("Wrong input. Please enter the number")
    else:
        print('Wrong Command')
        pass