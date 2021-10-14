def make_album(album, author, songs=None):
    result = {'album': album, 'author': author}
    if songs:
        result['songs'] = songs
    return result


while True:
    print("Enter 'q' at any time to exit")
    album_f = input("Enter album: ")
    if album_f == 'q':
        break
    author_f = input("Enter author of album: ")
    if author_f == 'q':
        break
    songs_f = input("Enter number of songs: ")
    if songs_f == 'q':
        break
    album1 = make_album(album_f, author_f, songs_f)
    print()
    print(album1)
    print()
