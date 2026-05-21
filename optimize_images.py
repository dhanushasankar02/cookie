import os
import sys

try:
    from PIL import Image
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

image_dir = r"d:\cookie\images"
max_size = (1280, 1280) # Reduce max size to 1280 to save more space, typical for web

total_saved = 0

for filename in os.listdir(image_dir):
    filepath = os.path.join(image_dir, filename)
    if not os.path.isfile(filepath):
        continue
    
    try:
        original_size = os.path.getsize(filepath)
        with Image.open(filepath) as img:
            format = img.format
            if format not in ['JPEG', 'PNG']:
                continue
            
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            if format == 'PNG':
                img.save(filepath, format='PNG', optimize=True)
            else:
                img.save(filepath, format='JPEG', quality=75, optimize=True)
                
        new_size = os.path.getsize(filepath)
        saved = original_size - new_size
        total_saved += saved
        print(f"Optimized {filename} - Saved {saved / 1024 / 1024:.2f} MB")
    except Exception as e:
        print(f"Error optimizing {filename}: {e}")

print(f"\nTotal space saved: {total_saved / 1024 / 1024:.2f} MB")
