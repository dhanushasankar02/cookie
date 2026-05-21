import glob
for f in glob.glob('d:/cookie/*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace("document.body.style.overflow = navCollapse.classList.contains('active') ? 'hidden' : '';", "// body overflow hidden removed to keep navbar sticky")
    content = content.replace("document.body.style.overflow = '';", "// body overflow reset removed")
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
