import requests


PREDICT_SERVICE_URL = 'http://localhost:8010/gpt/'


def dialog(inputs):

    params = {
        'max_length': 256,
        'no_repeat_ngram_size': 3,
        'do_sample': True,
        'top_k': 100,
        'top_p': 0.9,
        'temperature': 0.6,
        'num_return_sequences': 1,
        'device': 0,
        'is_always_use_length': True,
        'length_generate': '3',
    }

    res = requests.post(PREDICT_SERVICE_URL, json={'inputs': inputs, 'params': params})
    res = res.json()

    for response in res['outputs']:
        print('output:', response)
    return response
