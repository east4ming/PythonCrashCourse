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
print(make_album('Jay Chou', 'Fantancy', 10))
print(make_album('Jay Chou', 'Still Fantancy', song_nums=10))
print(make_album('Zuying Song', 'jasmine flower'))
