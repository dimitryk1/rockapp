from flask import Flask, jsonify
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

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
        "Pink Floyd"
    ]
    print("Received request, returning list of artists:")
    print(artists)
    return jsonify(artists)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)