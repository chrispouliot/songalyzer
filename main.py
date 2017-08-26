from services import get_music_service
from analyzer import get_average_popularity, get_intersection


def main():
    # just manual testing
    playlist_1, playlist_2 = input("Yo give me two playlist links, comma seperated: ").split(',')
    service_1, service_2 = get_music_service(playlist_1), get_music_service(playlist_2)
    playlist_1, playlist_2 = service_1.get_playlist(), service_2.get_playlist()

    print("pl1: average pop: {}".format(get_average_popularity(playlist_1.songs)))
    print("pl2: average pop: {}".format(get_average_popularity(playlist_2.songs)))

    matches = get_intersection(playlist_1.songs, playlist_2.songs)
    if matches:
        print("\nFound {} matching songs:\n".format(len(matches)))
        for matched_song in matches:
            print("{} - {}".format(matched_song.title, matched_song.artist))


if __name__ == '__main__':
    main()
