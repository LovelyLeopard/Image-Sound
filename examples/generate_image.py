from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from pydub import AudioSegment

# Create a simple Binary image
data = np.random.choice([0, 255], (10, 10)).astype(np.uint8)
img = Image.fromarray(data, 'L')
img.save('images/binary_image.png')

# Load and inspect
img_loaded = Image.open('images/binary_image.png')
pixels = np.array(img_loaded)

print("Image shape:", pixels.shape)
print("Pixel sample:", pixels[0][0])