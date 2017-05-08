
import csv
import random
import datetime

font_green = ('\033[1;32;40m')
font_red = ('\033[1;37;41m')
font_normal = ('\033[1;37;0m')


def import_music_data():
    ''' Import music data from csv file to list with tuples.
        Not working for csv with LAST LINE EMPTY
        - then you should make reader range shorter by 1 line range(number of lines minus 1)
        Final Look: [((name0, album0), (year0, genre0, length0)), ((name1, album1), (year1, genre1, length1)), ... ]
                 [0][0][0] [0][0][1] [0][1][0] [0][1][1] [0][1][2]'''
    try:
        with open('music.csv', mode='r') as open_csv:
            reader = csv.reader(open_csv, delimiter='|')
            music_data = []
            for row in reader:
                music_data.append(row)
            for i in range(len(music_data)):  # changes to proper tuples format
                music_data[i] = ((music_data[i][0].lstrip().rstrip(), music_data[i][1].lstrip().rstrip()),
                                 (int(music_data[i][2]), music_data[i][3].lstrip().rstrip(), music_data[i][4].lstrip()))
    except FileNotFoundError:
        print(font_red, "\bmusic.csv file not found :(", font_normal)
        exit()
    return music_data


def add_new_album():
    ''' Add new album to csv file. '''
    new_artist = input('Enter artist name: ')
    new_album = input('Enter album name: ')

    while True:     # new_year
        new_year = input('Enter year: ')
        if new_year.isdigit():  # 'dupa'test
            break
        else:
            print(font_red, '\bIs this a year?', font_normal)

    new_genre = input('Enter genre: ')

    while True:     # new_length
        new_length = input('Enter length in format MM:SS : ')
        new_length_check = new_length.split(':')    # split to list ['MM', 'SS'] for series of 'dupa' tests
        if len(new_length_check) != 2:
            print(font_red, '\bHave you put length IN PROPER FORMAT MM:SS ?! :| ', font_normal)
        else:
            if new_length_check[0].isdigit() and new_length_check[1].isdigit() and int(
                    new_length_check[0]) >= 0 and int(
                    new_length_check[1]) > 0 and int(
                    new_length_check[1]) < 60:
                break
            else:
                print(font_red, '\bMM are PROPER minutes and SS are PROPER seconds, yup? :| ', font_normal)

    print(font_green, '\bYou will see new album in CoolMusic 2.0 after program reboot ;)', font_normal)
    with open('music.csv', mode='a') as add_data:
        append_csv = csv.writer(add_data, delimiter='|')
        append_csv.writerow([new_artist, new_album, new_year, new_genre, new_length])


def albums_by_artist(music_data):
    ''' Shows albums by artist.'''
    answer_output = []
    search_input = input('Enter artist name: ')
    for i in range(0, len(music_data)):
        if search_input.upper() == music_data[i][0][0].upper():
            answer_output.append(music_data[i][0][1])
    if len(answer_output) == 0:
        print('There is no such artist. :(')
    else:
        print(font_green, '\bAlbum(s) of artist', search_input.upper(), 'is/are:', font_normal)
        for i in range(len(answer_output)):
            print(answer_output[i])


def albums_by_year(music_data):
    ''' Show albums by entered year.'''
    answer_output = []
    search_input = input('Enter year: ')
    if search_input.isdigit():  # 'dupa'test
        for i in range(0, len(music_data)):
            if int(search_input) == music_data[i][1][0]:
                answer_output.append((music_data[i][0][1], music_data[i][0][0]))
        if len(answer_output) == 0:
            print('There is no album from this year. :(')
        else:
            print(font_green, '\bAlbum(s) from year', search_input.upper(), 'is/are:', font_normal)
            for i in range(len(answer_output)):
                print(answer_output[i][0], 'by', answer_output[i][1])
    else:  # 'dupa'test
        print(font_red, '\bIs this a YEAR?', font_normal)


def musican_by_album(music_data):
    ''' Finds musician by album.'''
    answer_output = []
    search_input = input('Enter album name: ')
    for i in range(0, len(music_data)):
        if search_input.upper() == music_data[i][0][1].upper():
            answer_output.append(music_data[i][0][0])
    if len(answer_output) == 0:
        print('There is no such musician who create this album. :(')
    else:
        print(font_green, '\bMusician(s) who create album', search_input.upper(), 'is/are:', font_normal)
        for i in range(len(answer_output)):
            print(answer_output[i])


def album_by_letters(music_data):
    '''Finds album by any letters from it.'''
    answer_output = []
    search_input = input('Enter letters of album: ')
    for i in range(0, len(music_data)):
        if search_input.upper() in music_data[i][0][1].upper():
            answer_output.append((music_data[i][0][1], music_data[i][0][0]))
    if len(answer_output) == 0:
            print('There is no album with this letters. :(')
    else:
        print(font_green, '\bAlbum(s) with letters', search_input.upper(), 'is/are:', font_normal)
        for i in range(len(answer_output)):
            print(answer_output[i][0], 'by', answer_output[i][1])


def albums_by_genre(music_data):
    '''Finds albums by entered genre.'''
    answer_output = []
    search_input = input('Enter genre: ')
    for i in range(0, len(music_data)):
        if search_input.upper() == music_data[i][1][1].upper():
            answer_output.append((music_data[i][0][1], music_data[i][0][0]))
    if len(answer_output) == 0:
        print('There is no album from this genre. :(')
    else:
        print(font_green, '\bAlbum(s) from genre', search_input.upper(), 'is/are:', font_normal)
        for i in range(len(answer_output)):
            print(answer_output[i][0], 'by', answer_output[i][1])


def albums_age(music_data):
    '''Calculating age statistics etc.'''
    answer_output = []
    now = datetime.datetime.now()   # now.year returns current year
    sum_age = 0
    for i in range(0, len(music_data)):
        answer_output.append(music_data[i][1][0])   # adding years of albums to list

    print(font_green, '\bThe age of all albums is:', int(now.year * len(answer_output) - sum(answer_output)))
    print('Average age of album is:', int((now.year * len(answer_output) - sum(answer_output))
                                          / len(answer_output)), font_normal)
    print(font_green, '\bAverage year of album is:', int(sum(answer_output) / len(answer_output)), font_normal)


def rand_album_by_genre(music_data):
    '''Shows random album from entered genre.'''
    answer_output = []
    search_input = input('Enter genre: ')
    for i in range(0, len(music_data)):
        if search_input.upper() == music_data[i][1][1].upper():
            answer_output.append((music_data[i][0][1], music_data[i][0][0]))
    if len(answer_output) == 0:
        print('There is no album from this genre. :(')
    else:
        print(font_green, '\bRandom album from genre', search_input.upper(), 'is:'. font_normal)
        i = random.choice(range(0, len(answer_output)))
        print(answer_output[i][0], 'by', answer_output[i][1])


def amount_of_albums_by_artist(music_data):
    '''Shows number of album(s) of entered artist.'''
    answer_output = []
    search_input = input('Enter artist: ')
    for i in range(0, len(music_data)):
        if search_input.upper() == music_data[i][0][0].upper():
            answer_output.append(music_data[i][0][1])
    print(font_green, '\bNumber of album(s) by artist', search_input.upper(), 'is:', len(answer_output), font_normal)


def longest_album(music_data):
    '''Looks for longest-time album.'''
    answer_output = []
    for i in range(0, len(music_data)):
        answer_output.append(music_data[i][1][2].split(':'))
        answer_output[i] = int(answer_output[i][0]) * 60 + int(answer_output[i][1])
    i_of_longest = answer_output.index(max(answer_output))
    print(font_green, '\bThe longest-time album is:', music_data[i_of_longest][0][1].upper(),
          'by', music_data[i_of_longest][0][0].upper(), font_normal)


def print_menu():
    '''Prints main menu.'''
    print('/----------------------------------------------------------------------\ ')
    print('     Welcome in the CoolMusic 2.0! Choose the action:\n\
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


def main():
    music_data = import_music_data()
    while True:
        try:
            print_menu()
            menu_choice = int(input("Choose option from menu: "))
            if menu_choice == 1:
                add_new_album()
            elif menu_choice == 2:
                albums_by_artist(music_data)
            elif menu_choice == 3:
                albums_by_year(music_data)
            elif menu_choice == 4:
                musican_by_album(music_data)
            elif menu_choice == 5:
                album_by_letters(music_data)
            elif menu_choice == 6:
                albums_by_genre(music_data)
            elif menu_choice == 7:
                albums_age(music_data)
            elif menu_choice == 8:
                rand_album_by_genre(music_data)
            elif menu_choice == 9:
                amount_of_albums_by_artist(music_data)
            elif menu_choice == 10:
                longest_album(music_data)
            elif menu_choice == 0:
                print("See you next time! ( ͡° ͜ʖ ͡°)")
                exit()
            else:   # 'dupa' test - wrong number of menu_choice
                print(font_red, '\bChoose proper menu number!', font_normal)
        except ValueError:  # 'dupa' test - if you put non-int in menu_choice
            print(font_red, '\bIs that a number?', font_normal)


if __name__ == '__main__':
    main()
