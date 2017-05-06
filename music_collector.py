
import csv


def import_music_data():
    ''' Import music data from csv file to list with tuples. '''
    try:
        with open('music.csv', mode='r') as open_csv:
            reader = csv.reader(open_csv, delimiter='|')
            music_data = []
            for row in reader:  # read list
                music_data.append(row)
            for i in range(len(music_data)):  # change to proper tuples format
                music_data[i] = ((music_data[i][0].lstrip().rstrip(), music_data[i][1].lstrip().rstrip()),
                                 (int(music_data[i][2]), music_data[i][3].lstrip().rstrip(), music_data[i][4].lstrip()))
    except FileNotFoundError:
        print("music.csv file not found :(")
        exit()
    return music_data


def main():
    music_data = import_music_data()
    print(music_data)
    print(music_data[0][0][0])

    while True:
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

            menu_choice = int(input("Choose option from menu: "))

            if menu_choice == 1:
                print('1) Add new album')

            elif menu_choice == 2:
                print('You want to find albums by artist.')
                search = input('Enter artist name: ')
                for i in music_data:
                    if search == music_data[i][0][0]:
                        print('Album of artist', search, 'are:', music_data[i][0][1])
                    else:
                        print("There is no such artist. :(")

            elif menu_choice == 3:
                print('3) Find albums by year')
            elif menu_choice == 4:
                print('4) Find musician by albu')
            elif menu_choice == 5:
                print('5) Find albums by letter(s)')
            elif menu_choice == 6:
                print('6) Find albums by genre')
            elif menu_choice == 7:
                print('7) Calculate the age of all albums')
            elif menu_choice == 8:
                print('8) Choose a random album by genre')
            elif menu_choice == 9:
                print('9) ***Show the amount of albums by an artist')
            elif menu_choice == 10:
                print('10) ***Find the longest-time album')
            elif menu_choice == 0:
                print("See you next time! ( ͡° ͜ʖ ͡°)")
                exit()
            else:   # 'dupa' test - wrong number
                print('Choose proper menu number!')

        except ValueError:  # 'dupa' test - if you put non-int
            print('Is that a number?')


if __name__ == '__main__':
    main()
