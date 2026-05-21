import sys
import re
import os

cp1252_chars = {
    0x80: '€', 0x82: '‚', 0x83: 'ƒ', 0x84: '„', 0x85: '…', 0x86: '†', 0x87: '‡',
    0x88: 'ˆ', 0x89: '‰', 0x8A: 'Š', 0x8B: '‹', 0x8C: 'Œ', 0x8E: 'Ž',
    0x91: '‘', 0x92: '’', 0x93: '“', 0x94: '”', 0x95: '•', 0x96: '–', 0x97: '—',
    0x98: '˜', 0x99: '™', 0x9A: 'š', 0x9B: '›', 0x9C: 'œ', 0x9E: 'ž', 0x9F: 'Ÿ'
}
char_to_byte = {v: k for k, v in cp1252_chars.items()}

def unmojibake_match(match):
    text = match.group()
    bytes_list = []
    for c in text:
        if c in char_to_byte:
            bytes_list.append(char_to_byte[c])
        elif ord(c) < 256:
            bytes_list.append(ord(c))
        else:
            return text # return original if it can't be decoded
    try:
        return bytes(bytes_list).decode('utf-8')
    except:
        return text

files_to_fix = ['custom.html', 'classes.html', 'login.html', 'register.html']

for fpath in files_to_fix:
    if not os.path.exists(fpath):
        print(f"Skipping {fpath}, not found.")
        continue
    
    with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Replace sequences of non-ASCII characters
    new_content = re.sub(r'[^\x00-\x7F]+', unmojibake_match, content)
    
    # manual replace for specific missed sequences that got separated due to ascii chars in between?
    # Actually, UTF-8 bytes are always > 127, so they always form a contiguous sequence of non-ASCII characters.
    # Therefore, re.sub(r'[^\x00-\x7F]+', ...) will correctly capture the whole mangled character perfectly.

    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {fpath}")
    else:
        print(f"No fixes needed in {fpath}")
