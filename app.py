from sanic import Sanic, response
from sanic.exceptions import SanicException

from server.analyzer import get_average_popularity, find_common_artists, find_common_songs
from server.exceptions import InvalidQueryError
from server.services import get_music_service


app = Sanic(__name__)
app.static('/static', './static')
app.static('/', './static/index.html')


@app.exception(SanicException)
def error_middleware(request, exception):
    message = exception.message
    if exception.code == 500:
        print(message)
        message = "An error occured while handling your request"

    return response.json(
        {'message': message},
        status=exception.code
    )


@app.route('/analyze', methods=['GET'])
async def analyze(request):
    print(request.raw_args)
    playlist_url = request.raw_args.get('playlist_url')
    if not playlist_url:
        raise InvalidQueryError("Invalid Playlist URL")

    music_service = get_music_service(playlist_url)
    playlist = music_service.get_playlist()

    return response.json({
        "average_pop": get_average_popularity(playlist.songs)
    })


app.run(host="0.0.0.0", port=8000)
