import sys

replacements = {
    "â€”": "—",    # em dash
    "â€™": "'",    # apostrophe
    "â€“": "–",    # en dash
    "Â©": "©",     # copyright
    "â€‘": "-",    # non-breaking hyphen
    "Â°": "°",     # degree
    "âœ¦": "✦",    # four pointed star
    "â†“": "↓",    # down arrow
    "âš ï¸ ": "⚠️", # warning
    "âœ✨": "✨",   # sparkles
    "âœ¨": "✨",   # sparkles
    "âˆ’": "−"     # minus
}

file_path = 'd:/cookie/contact.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

for bad, good in replacements.items():
    content = content.replace(bad, good)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Fixed encoding issues in {file_path}")
