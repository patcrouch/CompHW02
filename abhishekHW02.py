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
def show_menu():
  print("1: A list of unique artists in the top 10 most played songs")
  print("2: Song details by ranking")
  print("3: Songs by an artist")
  print("4: Songs ordered by length")
  print("0: Exit")
def get_unique_artist():
  try:
   set_songs= set()
   for id,songs in spotify.items():
     for artist in songs["artists"]:
        if artist not in set_songs:
          set_songs.add(artist)
  except Exception as e :
    print('Could not get artists',e)
  print(", ".join(sorted(set_songs)))
def get_song_details():
  try:
   songid = input('Enter the ranking you are interested in (between 1 and 10): ')
   if not songid.isdigit():
     print('Invalid input. Please enter a number. ')
     return
   songid = int(songid)
   if songid > 10 or songid < 1:
     print('Ranking out of range.')
     return
   else:
     song_track =spotify[songid]
     print(f'{songid}: {song_track["title"]} by {", ".join(song_track["artists"])}')
  except Exception as e:
     print('Could not get song details',e)
def songs_by_artist():
  try:
    artist_songs=dict()
    artist_name =input('Enter the name of the artist you are interested in: ')
    for id,song in spotify.items():
       for name in song["artists"]:
         if(artist_name.lower() == name.lower()):
           artist_songs[id]=song["title"]
    if not artist_songs:
      print(f'No songs were found by {artist_name}')
    for key,items in artist_songs.items():
      print(f'{key}: {items.lower()}')
  except Exception as e:
     print('Could not get songs by artist',e)
def songs_by_length():
  try:
    length_input = input("Enter a number to view songs by length. (Positive: longest songs, Negative: shortest songs): ")
    number = int(length_input)
    if number>0:
        positive =True
    else:
        positive =False
    songs_details = []
    for song in spotify.values():
        minutes, seconds = map(int, song["length"].split(":"))
        time = minutes * 60 + seconds
        songs_details.append({
            "title": song["title"],
            "artists": song["artists"],
            "time": time
        })
    songs_details.sort(key=lambda x: x["time"], reverse=positive)
    number = abs(number)
    output_songs= songs_details[:number]
    for item in output_songs:
        artist_str = ", ".join(item["artists"])
        print(f'{item["title"]} by {artist_str} ({item["time"]} seconds)')
  except ValueError:
    print("Invalid value. Please enter a number.")
  return
while True:
  show_menu()
  n = input('Enter your option: ')
  if n =="0":
   break
  elif n =="1":
   get_unique_artist()
  elif n=="2":
   get_song_details()
  elif n=="3":
   songs_by_artist()
  elif n=="4":
    songs_by_length()