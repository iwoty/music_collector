
import csv
import random
import datetime


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

    while True:
        try:
            print('/----------------------------------------------------------------------\ ')
            print('     Welcome in the CoolMusic! Choose the action:\n\
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
            answer_output = []  # empty list for answers

            if menu_choice == 1:
                print('You want to add new album')
                

            elif menu_choice == 2:
                print('You want to find albums by artist.')
                search_input = input('Enter artist name: ')
                for i in range(0, len(music_data)):
                    if search_input.upper() == music_data[i][0][0].upper():
                        answer_output.append(music_data[i][0][1])
                if len(answer_output) == 0:
                    print('There is no such artist. :(')
                else:
                    print('Album(s) of artist', search_input.upper(), 'is/are:')
                    for i in range(len(answer_output)):
                        print(answer_output[i])

            elif menu_choice == 3:
                print('You want to find albums by year.')
                search_input = input('Enter year: ')
                if search_input.isdigit():  # 'dupa'test
                    for i in range(0, len(music_data)):
                        if int(search_input) == music_data[i][1][0]:
                            answer_output.append((music_data[i][0][1], music_data[i][0][0]))
                    if len(answer_output) == 0:
                        print('There is no album from this year. :(')
                    else:
                        print('Album(s) from year', search_input.upper(), 'is/are:')
                        for i in range(len(answer_output)):
                            print(answer_output[i][0], 'by', answer_output[i][1])
                else:  # 'dupa'test
                    print('Is this a YEAR?')

            elif menu_choice == 4:
                print('You want to find musician by album.')
                search_input = input('Enter album name: ')
                for i in range(0, len(music_data)):
                    if search_input.upper() == music_data[i][0][1].upper():
                        answer_output.append(music_data[i][0][0])
                if len(answer_output) == 0:
                    print('There is no such musician who create this album. :(')
                else:
                    print('Musician(s) who create album', search_input.upper(), 'is/are:')
                    for i in range(len(answer_output)):
                        print(answer_output[i])

            elif menu_choice == 5:
                print('You want to find album by letters.')
                search_input = input('Enter letters of album:')

            elif menu_choice == 6:
                print('You want to find albums by genre.')
                search_input = input('Enter genre: ')
                for i in range(0, len(music_data)):
                    if search_input.upper() == music_data[i][1][1].upper():
                        answer_output.append((music_data[i][0][1], music_data[i][0][0]))
                if len(answer_output) == 0:
                    print('There is no album from this genre. :(')
                else:
                    print('Album(s) from genre', search_input.upper(), 'is/are:')
                    for i in range(len(answer_output)):
                        print(answer_output[i][0], 'by', answer_output[i][1])

            elif menu_choice == 7:
                print('You want to calculate the age of all albums.')
                now = datetime.datetime.now()   # now.year returns current year
                sum_age = 0
                for i in range(0, len(music_data)):
                    answer_output.append(music_data[i][1][0])   # adding years of albums to list

                print('The age of all albums is:', int(now.year * len(answer_output) - sum(answer_output)))
                print('Average age of album is:', int((now.year * len(answer_output) - sum(answer_output))
                                                      / len(answer_output)))
                print('Average year of album is:', int(sum(answer_output) / len(answer_output)))

            elif menu_choice == 8:
                print('You want to find random album by genre.')
                search_input = input('Enter genre: ')
                for i in range(0, len(music_data)):
                    if search_input.upper() == music_data[i][1][1].upper():
                        answer_output.append((music_data[i][0][1], music_data[i][0][0]))
                if len(answer_output) == 0:
                    print('There is no album from this genre. :(')
                else:
                    print('Random album from genre', search_input.upper(), 'is:')
                    i = random.choice(range(0, len(answer_output)))
                    print(answer_output[i][0], 'by', answer_output[i][1])

            elif menu_choice == 9:
                print('You want to know amount of album by an artist.')
                search_input = input('Enter artist: ')
                for i in range(0, len(music_data)):
                    if search_input.upper() == music_data[i][0][0].upper():
                        answer_output.append(music_data[i][0][1])
                print('Number of album(s) by artist', search_input.upper(), 'is:', len(answer_output))

            elif menu_choice == 10:
                print('10) ***Find the longest-time album')
                for i in range(0, len(music_data)):
                    answer_output.append(music_data[i][1][2].split(':'))
                    answer_output[i] = int(answer_output[i][0])*60 + int(answer_output[i][1])
                i_of_longest = answer_output.index(max(answer_output))
                print('The longest-time album is:', music_data[i_of_longest][0][1].upper(),
                      'by', music_data[i_of_longest][0][0].upper())

            elif menu_choice == 0:
                print("See you next time! ( ͡° ͜ʖ ͡°)")
                exit()

            else:   # 'dupa' test - wrong number of menu_choice
                print('Choose proper menu number!')

        except ValueError:  # 'dupa' test - if you put non-int in menu_choice
            print('Is that a number?')


if __name__ == '__main__':
    main()
