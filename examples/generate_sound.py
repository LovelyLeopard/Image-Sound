import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from pydub import AudioSegment

# Generate a 1 second sine wave at 440 Hz
rate = 44100
duration = 1.0
freq = 440
t = np.linspace(0, duration, int(rate * duration), endpoint=False)
wave = (0.5 * np.sin(2 * np.pi * freq * t)).astype(np.float32)

# Save as WAV file
write('sounds/sine_wave.wav', rate, wave)

# Convert to MP3
AudioSegment.from_wav('sounds/sine_wave.wav').export('sounds/sine_wave.mp3', format='mp3')

# Plotting
plt.plot(t[:1000], wave[:1000])  # Plot first 1000 samples
plt.title("440 Hz Sine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
plt.savefig('images/sine_wave_plot.png')