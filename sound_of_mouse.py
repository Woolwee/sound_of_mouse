import math
import mouse
import pyaudio
from time import sleep


def main(mouse_position: tuple):

    p = pyaudio.PyAudio()     #initialize pyaudio
    BITRATE = 5000     #number of frames per second/frameset.
    FREQUENCY = int((mouse_position[0] * mouse_position[1]) / 103.68)  # Hz
    FREQUENCY = FREQUENCY if FREQUENCY != 0 else 1
    LENGTH = .1    #seconds to play sound

    if FREQUENCY > BITRATE:
        BITRATE = FREQUENCY + 100
    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    RESTFRAMES = NUMBEROFFRAMES % BITRATE
    WAVEDATA = ''

    #generating waves
    for x in range(1, NUMBEROFFRAMES + 1):
        WAVEDATA += chr(int(math.sin(x / ( (BITRATE/FREQUENCY) / math.pi )) * 127 + 128))
    for x in range(RESTFRAMES):
        WAVEDATA = WAVEDATA + chr(128)

    stream = p.open(format = p.get_format_from_width(1),
                    channels = 2,
                    rate = BITRATE,
                    output = True)
    stream.write(WAVEDATA)
    #stream.stop_stream()
    #stream.close()
    #p.terminate()


if __name__ == "__main__":
    while True:
        if (mouse_position := mouse.get_position()) == mouse.get_position():
            #sleep(1/60)
            continue
        else:
            main(mouse_position)
