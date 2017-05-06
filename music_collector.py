
import csv
from collections import OrderedDict     # for sorting of dictionary keys

while True:
    '''
    my_dict = {}
    with open('music.csv', 'r') as f:
        my_dict = dict(csv.reader(f))
    print(my_dict)
    '''
    try:
        print('/----------------------------------------------------------------------\ ')
        print(' Welcome in the CoolMusic! Choose the action:\n\
                1) Add new album\n\
                2) Find albums by artist\n\
                3) Find albums by year\n\
                4) Find musician by album\n\
                5) Find albums by letter(s)\n\
                6) Find albums by genre\n\
                7) Calculate the age of all albums \n\
                8) Choose a random album by genre\n\
                9) ***Show the amount of albums by an artist\n\
               10) ***Find the longest-time album\n\
                0) Exit')
        print('\----------------------------------------------------------------------/ ')

        menu = int(input("Choose option from menu: "))

        if menu == 1:
            print('dupa1')
        elif menu == 2:
            print('dupa2')
        elif menu == 3:
            print('dupa3')
        elif menu == 4:
            print('dupa4')
        elif menu == 5:
            print('dupa5')
        elif menu == 6:
            print('dupa6')
        elif menu == 7:
            print('dupa7')
        elif menu == 8:
            print('dupa8')
        elif menu == 9:
            print('dupa9')
        elif menu == 10:
            print('dupa10')
        elif menu == 0:
            break
        else:   # dupa test
            print('Choose proper menu number!')

    except ValueError:  # if you put non-int
        print('Is that a number?')

print("See you next time! ( ͡° ͜ʖ ͡°)")
