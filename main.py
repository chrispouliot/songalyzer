
def main():
    from services import get_music_service
    from analyzer import get_average_popularity
    playlist_query = input("Yo give me an playlist link: ")
    service = get_music_service(playlist_query)
    playlist = service.get_playlist()
    print(playlist.name)
    print(len(playlist.songs))
    print(get_average_popularity(playlist.songs))


if __name__ == '__main__':
    main()
