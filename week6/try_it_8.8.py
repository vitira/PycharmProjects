# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title, number_of_tracks=''):

    dictionary_make_album = {
        "artist": artist_name.title(),
        "album title": album_title.title(),
    }
    dictionary_make_album = { "artist" : artist_name, "album title" : album_title, "tracks": number_of_tracks }
    return dictionary_make_album

while True:
    ar_name = input("artist name")
    al_name = input("album name")
    if ar_name == "quit":
        break
    #al_name = input("album name")
    if al_name == "q":
        break

    #artist_info = make_album(ar_name, al_name)
    #print(f"hello {artist_info}")
    #if ar_name == "q":
     # break
