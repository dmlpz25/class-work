def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('Banda Blanca', 'banana')
print(album)

album = make_album('Los Tigre del Norte', 'Somas Más Americanos')
print(album)

album = make_album('Eydie Gormé', 'Sabor a Mí')
print(album)