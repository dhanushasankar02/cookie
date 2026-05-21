import glob

old_text = """    .nav-link:hover, .nav-link.active { color: #c16f34; }
    body.dark-mode .nav-link:hover, body.dark-mode .nav-link.active { color: #f7c894; }"""

new_text = """    .nav-link:hover { color: #c16f34; }
    .nav-link.active { color: #c0392b; font-weight: 700; } /* Distinct active color */
    body.dark-mode .nav-link:hover { color: #f7c894; }
    body.dark-mode .nav-link.active { color: #ff6b81; font-weight: 700; } /* Distinct active color */"""

for f in glob.glob('d:/cookie/*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")
    else:
        print(f"Not found in {f}")
