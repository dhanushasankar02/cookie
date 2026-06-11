import os
import re

dir_path = r'd:\groww\cookie'

for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # aggressively remove ALL colored box-shadows matching brand colors
        content = re.sub(r'rgba\(199,\s*122,\s*63,\s*0\.\d+\)', r'rgba(0, 0, 0, 0.1)', content)
        content = re.sub(r'rgba\(234,\s*182,\s*122,\s*0\.\d+\)', r'rgba(0, 0, 0, 0.1)', content)
        content = re.sub(r'rgba\(179,\s*95,\s*42,\s*0\.\d+\)', r'rgba(0, 0, 0, 0.1)', content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
