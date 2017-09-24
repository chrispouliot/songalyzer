from flask import Flask

from server.services import get_music_service
from server.analyzer import get_average_popularity, find_common_artists, find_common_songs


app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return app.send_static_file('index.html')
