from sanic import Sanic

from server.services import get_music_service
from server.analyzer import get_average_popularity, find_common_artists, find_common_songs


app = Sanic(__name__)
app.static('/static', './static')
app.static('/', './static/index.html')

app.run(host="0.0.0.0", port=8000)
