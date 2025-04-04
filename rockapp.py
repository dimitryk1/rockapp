from flask import Flask
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
import random, os

# Configure X-Ray recorder
xray_recorder.configure(service='classic-rock-api')
port = int(os.environ.get("PORT", 9003))
app = Flask(__name__)

# Initialize X-Ray middleware
XRayMiddleware(app, xray_recorder)

@app.route('/')
def classic_rock_artists():
    artists = [
        "Led Zeppelin",
        "The Rolling Stones",
        "Pink Floyd",
        "Guns N Roses",
        "Metallica"
    ]
    minind=0
    maxind=len(artists)-1
    index = random.randint(minind,maxind)
    artist=artists[index]
    print("Received request, returning " + artist)
    return (artist)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)