
import csv
from collections import OrderedDict     # for sorting of dictionary keys


def file_read():
    try:
        my_dict = {}
        with open('data.csv', mode='r') as open_data:  # Opening a file in read mode
            reader = csv.reader(open_data, delimiter=',')   # delimiter tells us about separator
            for row in reader:
                my_dict[row[0]] = (row[1], row[2])
    except FileNotFoundError:
        print("Data.csv file not found :(")
        exit()
    return my_dict


def main():
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
                print('1) Add new album')
            elif menu == 2:
                print('2) Find albums by artist')
            elif menu == 3:
                print('3) Find albums by year')
            elif menu == 4:
                print('4) Find musician by albu')
            elif menu == 5:
                print('5) Find albums by letter(s)')
            elif menu == 6:
                print('6) Find albums by genre')
            elif menu == 7:
                print('7) Calculate the age of all albums')
            elif menu == 8:
                print('8) Choose a random album by genre')
            elif menu == 9:
                print('9) ***Show the amount of albums by an artist')
            elif menu == 10:
                print('10) ***Find the longest-time album')
            elif menu == 0:
                break
            else:   # dupa test
                print('Choose proper menu number!')

        except ValueError:  # if you put non-int
            print('Is that a number?')

    print("See you next time! ( ͡° ͜ʖ ͡°)")


if __name__ == '__main__':
    main()
