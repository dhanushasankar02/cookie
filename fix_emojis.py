import sys

replacements = {
    "âœ‰ï¸ ": "✉️",
    "â „ï¸ ": "❄️",
    "âš ï¸ ": "⚠️",
    "ðŸ“ ": "📍",
    "ðŸ“ž": "📞",
    "ðŸš‡": "🚇",
    "ðŸ…¿ï¸ ": "🅿️",
    "ðŸŽ‚": "🎂",
    "ðŸ“¦": "📦",
    "ðŸ”¥": "🔥",
    "ðŸ ª": "🍪",
    "ðŸŽ‰": "🎉"
}

file_path = 'd:/cookie/contact.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

for bad, good in replacements.items():
    content = content.replace(bad, good)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Fixed emojis in {file_path}")
