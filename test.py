import pyaudio
import os
import struct
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time
from tkinter import TclError


CO = True
end_time = time.time()

def on_close(event):
    global CO
    global end_time
    event.canvas.figure.axes[0].has_been_closed = True
    print("CLOSED")
    CO = False
    end_time = time.time()

# constants
CHUNK = 1024 * 2             # samples per frame
FORMAT = pyaudio.paInt16     # audio format (bytes per sample?)
CHANNELS = 1                 # single channel for microphone
RATE = 44100                 # samples per second

# create matplotlib figure and axes
# matplotlib.use('Agg')
fig, ax = plt.subplots(1, figsize=(15, 7))
fig.canvas.mpl_connect('close_event', on_close)
# ax.canvas.mpl_connect('close_event', on_close)
# fig.canvas.mpl_connect('close_event', handle_close)

# pyaudio class instance
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

# show the plot
plt.show(block=False)

print('stream started')

# for measuring frame rate
frame_count = 0
start_time = time.time()

while CO:
    # binary data
    # print(CO)
    data = stream.read(CHUNK)
    # convert data to integers, make np array, then offset it by 127
    data_int = struct.unpack(str(2 * CHUNK) + 'B', data)
    
    # create np array and offset by 128
    data_np = np.array(data_int, dtype='b')[::2] + 128
    
    line.set_ydata(data_np)
    
    # update figure canvas
    fig.canvas.draw()
    fig.canvas.flush_events()
    frame_count += 1

# calculate average frame rate
frame_rate = frame_count / (end_time - start_time)
print('stream stopped')
print('average frame rate = {:.0f} FPS'.format(frame_rate))

