from flask import Flask, request, send_file
from TTS.api import TTS
import os

app = Flask(__name__)

# Load pretrained model
MODEL_NAME = "tts_models/en/ljspeech/tacotron2-DDC"
tts = TTS(MODEL_NAME)

@app.route("/api/tts", methods=["POST"])
def generate_tts():
    data = request.json
    text = data.get("text", "").strip()
    if not text:
        return {"error": "No text provided"}, 400

    # Generate speech file
    file_path = "output.wav"
    tts.tts_to_file(text=text, file_path=file_path)

    return send_file(file_path, mimetype="audio/wav")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 7860)))
