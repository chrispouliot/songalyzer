from sanic import Sanic, response

from server.analyzer import get_average_popularity, find_common_artists, find_common_songs
from server.exceptions import InvalidQueryError
from server.services import get_music_service


app = Sanic(__name__)
app.static('/static', './static')
app.static('/', './static/index.html')


@app.route('/analyze', methods=['GET'])
async def analyze(request):
    playlist_url = request.raw_args.get('playlist_url')
    if not playlist_url:
        raise InvalidQueryError("Invalid Playlist URL")

    music_service = get_music_service(playlist_url)
    playlist = music_service.get_playlist()

    return response.json({
        "average_pop": get_average_popularity(playlist.songs)
    })


app.run(host="0.0.0.0", port=8000)
