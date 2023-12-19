# Album 8.7

def make_album(artist_name, album_title, num_songs=None):
    """Return dictionary containing artist and album title"""
    music_album = {"musician" : artist_name, "album" : album_title}
    if num_songs:
        music_album['num_songs'] = num_songs
    return music_album

musician = make_album('metallica', 'master of puppets')
musician2 = make_album('tupac', 'all eyez on me')
musician3 = make_album('motley crue', 'shout at the devil')
musician4 = make_album('biggie smalls', 'ready to die', num_songs=5)

print(musician)
print(musician2)
print(musician3)
print(musician4)