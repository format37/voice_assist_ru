from recorder import listen
from stt import asr
from dialogpt import dialog
from tts import synthesize
from play import speak

filename = listen(6)
# sudo docker-compose up -d sova-asr-gpu
text_input = asr('input.wav')

# inputs = [
#         {'speaker': 0, 'text': 'Что нового на Луне?'},
#         {'speaker': 1, 'text': 'На Луне есть все. Даже Луна. Правда, не в том виде, в каком мы привыкли.'},
#         {'speaker': 1, 'text': 'Тогда в каком?'}
#     ]

inputs = [{'speaker': 0, 'text': text_input},]
text_output = dialog(inputs)
synthesize(text_output.replace('"', ''))
speak('output.wav')
print('exit')
