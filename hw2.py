# DO NOT ADD LIBRARIES/PACKAGES.
# If you want to cover additional error cases other than the given below,
# feel free to create a error message.

spotify = {
    1: {"artists": ["ROSÉ", "Bruno Mars"], "title": "APT.", "length": "2:49"},
    2: {"artists": ["Lady Gaga", "Bruno Mars"], "title": "Die With a Smile",
        "length": "4:11"},
    3: {"artists": ["Ed Sheeran"], "title": "Sapphire", "length": "2:59"},
    4: {"artists": ["Billie Eilish"], "title": "Birds of a Feather",
        "length": "3:30"},
    5: {"artists": ["Benson Boone"], "title": "Beautiful Things",
        "length": "3:00"},
    6: {"artists": ["Sabrina Carpenter"], "title": "Manchild",
        "length": "3:33"},
    7: {"artists": ["Alex Warren"], "title": "Ordinary", "length": "3:06"},
    8: {"artists": ["Billie Eilish"], "title": "Wildflower", "length": "4:21"},
    9: {"artists": ["Sabrina Carpenter"], "title": "Espresso",
        "length": "2:55"},
    10: {"artists": ["Lady Gaga"], "title": "Abracadabra", "length": "3:43"}
}


user_choice_question = "Enter what you would like to browse:\n \
                        \t1: A list of artists in the top 10 most played songs\n \
                        \t2: Song by ranking\n \
                        \t3: Songs by an artist\n \
                        \t4: Songs ordered by length\n \
                        \t0: Exit\n"

ranking_question = "Enter the ranking you're interested in (between 1 and 10): "
ranking_value_error = "Invalid input. Please enter a number."
ranking_range_error = "Ranking out of range."

artist_question = "Enter the name of the artist you're interested in: "
artist_error = "No songs were found by "

length_question = "Enter a number to view songs by length. (Positive: longest songs, Negative: shortest songs): "
length_value_error = "Invalid vallue. Please enter a number."
#above is everything given in hw2.py, below is what we've written

def unique_artists():
    artist_list = []
    for song in spotify.values():
        for artist in song['artists']:
            if artist not in artist_list:
                artist_list.append(artist)

    artist_list.sort()

    print(', '.join(artist_list))
    return 

def song_by_rank(string_r):
    try:
        r = int(string_r)
    except:
        print(ranking_value_error)
        return

    if r < 1 or r > 10:
        print(ranking_range_error)
        return

    song = spotify[r]
    r_string = f"{r}: {song['title']} by {', '.join(song['artists'])}"

    print(r_string)
    return

def song_by_artist(artist):
    song_list = []

    for r in spotify:
        lower_aritsts = [a.lower() for a in spotify[r]['artists']]
        if artist.lower() in lower_aritsts:
            song_list.append(f"{r}: {spotify[r]['title']}")


    if not song_list:
        print(artist_error + artist)
        return 
    else:
        print('\n'.join(song_list))

def songs_by_length(list_length):
    try:
        n = int(list_length)
    except:
        print(length_value_error)
        return

    #creates mapping from time to song rank
    song_length_dict = {}
    for i in spotify:
        song_length_dict[spotify[i]['length']] = i

    #creates ascending sorted list based on time
    sorted_keys = list(song_length_dict.keys())
    sorted_keys.sort()
    sorted_song_length_list = [song_length_dict[i] for i in sorted_keys]

    #reverses order when length is positive
    if n > 0:
        sorted_song_length_list.reverse()

    #creates string list of artists
    song_list = []
    for r in sorted_song_length_list[:abs(n)]:
        title = spotify[r]['title']
        artists = ', '.join(spotify[r]['artists'])

        #converts time to seconds
        h, s = spotify[r]['length'].split(':')
        time_in_seconds = 60*int(h)+int(s)

        song_list.append(f"{title} by {artists} ({time_in_seconds} seconds)")
    
    print('\n'.join(song_list))
    
while True:
    user_input = input(user_choice_question)
    if int(user_input) == 0:
        break
    elif int(user_input) == 1:
        print(unique_artists())
    elif int(user_input) == 2:
        song_by_rank(input(ranking_question))
    elif int(user_input) == 3:
        song_by_artist(input(artist_question))
    elif int(user_input) == 4:
        songs_by_length(input(length_question))

