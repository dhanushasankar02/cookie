import os
from PIL import Image

for f in os.listdir('images'):
    if f.startswith('classes') and f.endswith('.jpg'):
        path = os.path.join('images', f)
        print(f'{f}: {Image.open(path).size}')
