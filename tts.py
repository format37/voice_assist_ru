import requests
import soundfile as sf
import numpy as np
from base64 import b64decode


def synthesize(text_output):
    filename = 'output.wav'

    data = '{"text": "'+text_output+'", "voice": "Natasha"}'
    data = data.encode('utf-8')
    url = "http://localhost:8899/synthesize/"
    headers = {"content-type": "application/json"}
    response = requests.post(
        url,
        headers=headers,
        data=data
    )
    print('output request:', response)
    audio = response.json()['response'][0]['response_audio']
    audio_bytes = b64decode(audio)
    with open(filename, 'wb') as f:
        f.write(audio_bytes)
    return filename
