import requests


def asr(filename):
    url = "http://localhost:8888/asr/"
    f1 = open(filename, 'rb')
    response = requests.post(url, files={"audio_blob": f1}) #several files accepted maybe
    input_text = response.json()['r'][0]['response'][0]['text']
    print('input:', input_text)
    return input_text
