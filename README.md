# Trading Ek Mission - TTS Server

Custom Text-to-Speech (TTS) engine using [Coqui TTS](https://github.com/coqui-ai/TTS).

## Run locally
```bash
pip install -r requirements.txt
python app.py
```

## Deploy on Hugging Face Spaces
1. Create a new Space.
2. Select **Docker** as SDK.
3. Connect this GitHub repo.

The API will be available at:
```
https://<your-username>-trading-tts.hf.space/api/tts
```

## API Usage
```bash
POST /api/tts
{
  "text": "Hello Trading Ek Mission!"
}
```
Response: WAV audio file.
