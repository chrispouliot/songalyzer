
def main():
    from spotify import get_playlist
    playlist = get_playlist('moxuz', '5EUAKAJMceKIfUlIUtVfxg')
    print(playlist.name)
    print(len(playlist.songs))


if __name__ == '__main__':
    main()
