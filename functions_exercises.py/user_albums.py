# User albums 8.8

def make_album(artist_name, album_title, num_songs=None):
    """Return dictionary containing artist and album title"""
    music_album = {"musician" : artist_name, "album" : album_title}
    if num_songs:
        music_album['num_songs'] = num_songs
    return music_album

while True:
    print("Enter an album's artist: ")
    print("Enter an album's title: ")
    print("Enter 'q' to quit ")

    a_artist = input("Artist album: ")
    if a_artist == "q":
        break
    a_title = input("Album title: ")
    if a_title == "q":
        break
    user_album = make_album(a_artist, a_title)
    print(user_album)