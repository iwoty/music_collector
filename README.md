# music_collector
Do you like to listen to music? Mate loves it! He is the owner of a music store CoolMusic. Business developes really fast and he has a problem with arrangement the albums. Please, help him to create the catalog of all albums.

Description
Create a list music for storing his music albums.

Every element is a complex of two tuples - name and information

Tuple name contains two strings - a name of artist and a name of album.

Tuple information contains integer and two strings - year of release, genre and length.

Example:

music = [(("Pink Floyd", "The Dark Side Of The Moon"), (1973, "psychodelic rock", "43:00")),
         (("Britney Spears", "Baby One More Time"), (1999, "pop", "42:20"))]

Below is a the example menu. Your program should carry out the following functionalities.

Welcome in the CoolMusic! Choose the action:
         1) Add new album
         2) Find albums by artist
         3) Find albums by year
         4) Find musician by album
         5) Find albums by letter(s)
         6) Find albums by genre
         7) Calculate the age of all albums
         8) Choose a random album by genre
         9) Show the amount of albums by an artist *
        10) Find the longest-time album *
         0) Exit

9, 10) additional features (for 12 pts)

Details
1. The catalog has to be read from and written into CSV file music.csv (https://drive.google.com/open?id=0B2VL35dJa4R1V1AwOEpJc2J6eDg). You don't have to push it into repository, your program will be tested with our file.

2. Your script should be based on custom functions.

3. The name of album should be printed with the name of artist.

4. Album should be find by letters in any place of title. For example, if user input "the", program will print
every albums with "the" in the title - "The Dark Side of The Moon" and "Music of the Sun".
