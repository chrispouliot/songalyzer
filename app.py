import logging

from sanic import Sanic, response
from sanic.exceptions import ServerError
from server.analyzer import get_average_popularity, \
    find_common_artists, \
    find_common_songs
from server.exceptions import InvalidQueryError
from server.services import get_music_service


app = Sanic(__name__)
app.static('/static', './static')
app.static('/', './static/index.html')


# @app.exception(SanicException)
# def middleware_error(request, exception):
#     return response.json(
#         {'message': exception},
#         status=exception.status_code
#     )


@app.route('/analyze', methods=['GET'])
async def analyze(request):
    raise ServerError("Invalid Playlist URL")
    playlists = request.raw_args.values()
    if not playlists:
        raise InvalidQueryError("Invalid Playlist URL")

    analyzed_playlists = []
    for playlist in playlists:
        # TODO: Async per playlist
        music_service = get_music_service(playlist)
        analyzed_playlists.append(music_service.get_playlist())

    return response.json({
        "playlists": analyzed_playlists
    })


app.run(host="0.0.0.0", port=8000)
