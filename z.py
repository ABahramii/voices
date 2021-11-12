import pyaudio
import struct # unpacked audio data into integers instead of binary numbers
import numpy as np
import matplotlib.pyplot as plt
import time
from tkinter import TclError

# how many voice(byte) process on a time -> audio samples per frame
CHUNK = 1024 * 2  # 2048 samples per chunk
FORMAT = pyaudio.paInt16     # bit depth
CHANNELS = 1                 # voice input -> get audio from one channel(one microphone)
RATE = 44100                 # samples per second -> sampling frequency -> 48KHZ(48000 cycle per sec)


p = pyaudio.PyAudio()

# stream object to get data from microphone
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

# create matplotlib figure and axes
fig, ax = plt.subplots(1, figsize=(15, 7))

# variable for plotting
x = np.arange(0, 2 * CHUNK, 2)
# create a line object with random data
line, = ax.plot(x, np.random.rand(CHUNK), '-', lw=2)

# basic formatting for the axes
ax.set_title('AUDIO WAVEFORM')
ax.set_xlabel('samples')
ax.set_ylabel('volume')
ax.set_ylim(0, 255)
ax.set_xlim(0, 2 * CHUNK)

plt.setp(ax, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0, 128, 255])

# show the plot -> non blocking because it's stream!
plt.show(block=False)

print('stream started')

# for measuring frame rate
frame_count = 0
start_time = time.time()

while True:
    # read data -> binary data
    data = stream.read(CHUNK)

    # convert data to integers
    data_int = struct.unpack(str(2 * CHUNK) + 'B', data)

    # create np array and offset by 128
    data_np = np.array(data_int, dtype='b')[::2] + 128

    line.set_ydata(data_np)

    # update figure canvas
    try:
        fig.canvas.draw()
        fig.canvas.flush_events()
        frame_count += 1
    except TclError:
        # calculate average frame rate
        stop_time = time.time()
        frame_rate = frame_count / (stop_time - start_time)

        print('stream stopped')
        print('average frame rate = {:.0f} FPS'.format(frame_rate))
        break