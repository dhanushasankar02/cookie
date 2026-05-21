import glob
import re

for f in glob.glob('d:/cookie/*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace anything that looks like a Tutorials link that points to '#' or './Tutorials.html'
    # with href="Tutorials.html"
    new_content = re.sub(r'<a\s+href="[^"]*"\s+class="nav-link">Tutorials</a>', '<a href="Tutorials.html" class="nav-link">Tutorials</a>', content)
    new_content = re.sub(r'<a\s+href="[^"]*"\s+class="nav-link active">Tutorials</a>', '<a href="Tutorials.html" class="nav-link active">Tutorials</a>', new_content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Updated {f}')
