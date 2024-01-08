from flask import Flask, request
import os
from gradio_client import Client
from audio import *

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'C:/Users/s.uguaaa/Desktop/react_native/Tafsiri/app/assets/downloads'

@app.route("/send", methods = ['GET', 'POST'])
def tafsiri_api():
    if request.method == 'POST':
        if 'file' not in request.files:
            return {
                "result": "no file received"
            }

        file = request.files['file']

        if file:
            filename = 'upload.jpeg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    client = Client("noble-nobody/tafsiri-test")
    result = client.predict(
        "C:/Users/s.uguaaa/Desktop/react_native/Tafsiri/app/assets/downloads/upload.jpeg",
        api_name = "/predict"
    )

    text_to_speech(result, 'C:/Users/s.uguaaa/Desktop/react_native/Tafsiri/app/assets/audio/speech.mp3')
    return result

# "https://noble-nobody-tafsiri-test.hf.space/--replicas/ixh5s"
# "C:/Users/s.uguaaa/Desktop/react_native/Tafsiri/app/assets/testing/friend.jpg"