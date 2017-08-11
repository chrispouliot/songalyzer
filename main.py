
def main():
    from spotify import _get, BASE_URL
    url = "{base}/users/{user_id}/playlists/{playlist_id}".format(
        base=BASE_URL,
        user_id="moxuz",
        playlist_id="5EUAKAJMceKIfUlIUtVfxg",
    )
    print(_get(url))


if __name__ == '__main__':
    main()
