"""Make Album.

创建一个描述音乐专辑的字典.
接受歌手的名字和专辑名, 并返回一个包含这两项信息的字典.
"""

def make_album(singer, album_name, song_nums=''):
    """Make a album dict, include singer and album name."""
    if song_nums:        
        album = {'singer': singer, 'album_name': album_name, 'song_nums': song_nums}
    else:
        album = {'singer': singer, 'album_name': album_name}
    return album

while True:
    print('Please input a singer and his/her album: ')
    print('You can input "q" to quit.')
    singer = input('Singer: ')
    if singer == 'q':
        break
    album_name = input('Album Name: ')
    if album_name == 'q':
        break
    print('The album\'s info: \t', make_album(singer, album_name), '\n')
