file_path = 'd:/cookie/gallery.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'â€œ': '<i class="fas fa-quote-left"></i>',
    'â€”': '—',
    'â€¢': '•',
    'Â©': '©',
    'â€“': '–',
    'ðŸ ª': '🍪',
    'âœ✨': '✨',
    'ðŸŽ‰': '🎉'
}

for bad, good in replacements.items():
    content = content.replace(bad, good)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed mojibake in gallery.html')
