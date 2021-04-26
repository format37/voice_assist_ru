import pyaudio
import wave


def listen(record_seconds):

    chunk = 1024
    fmt = pyaudio.paInt16
    channels = 2
    rate = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=fmt,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print("* recording")

    frames = []

    for i in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    filename = "input.wav"

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(fmt))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()
    return filename
