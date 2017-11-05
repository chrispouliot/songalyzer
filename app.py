import logging

from sanic import Sanic, response
from sanic.exceptions import SanicException
from server.analyzer import get_average_popularity, \
    find_common_artists, \
    find_common_songs
from server.exceptions import InvalidQueryError
from server.services import get_music_service


app = Sanic(__name__)
app.static('/static', './static')
app.static('/', './static/index.html')


@app.exception(SanicException)
def middleware_error(request, exception):
    message = "An error occured while handling your request"
    if hasattr(exception, 'message'):
        message = exception.message

    if exception.status_code == 500:
        logging.error(exception)

    return response.json(
        {'message': message},
        status=exception.status_code
    )


@app.route('/analyze', methods=['GET'])
async def analyze(request):
    raw_input = request.raw_args.get('input')
    if not raw_input:
        raise InvalidQueryError("Invalid Playlist URL")

    playlists = raw_input.split(',')

    analyzed_playlists = []
    for playlist in playlists:
        # TODO: Async per playlist
        music_service = get_music_service(playlist)
        analyzed_playlists.append(music_service.get_playlist())


    return response.json({
        "playlists": analyzed_playlists
    })


app.run(host="0.0.0.0", port=8000)
