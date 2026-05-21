import sys

# CP1252 mapping for 0x80-0x9F
cp1252_chars = {
    0x80: '€', 0x82: '‚', 0x83: 'ƒ', 0x84: '„', 0x85: '…', 0x86: '†', 0x87: '‡',
    0x88: 'ˆ', 0x89: '‰', 0x8A: 'Š', 0x8B: '‹', 0x8C: 'Œ', 0x8E: 'Ž',
    0x91: '‘', 0x92: '’', 0x93: '“', 0x94: '”', 0x95: '•', 0x96: '–', 0x97: '—',
    0x98: '˜', 0x99: '™', 0x9A: 'š', 0x9B: '›', 0x9C: 'œ', 0x9E: 'ž', 0x9F: 'Ÿ'
}
char_to_byte = {v: k for k, v in cp1252_chars.items()}

def unmojibake(text):
    bytes_list = []
    for c in text:
        if c in char_to_byte:
            bytes_list.append(char_to_byte[c])
        elif ord(c) < 256:
            bytes_list.append(ord(c))
        else:
            return None
    try:
        return bytes(bytes_list).decode('utf-8')
    except:
        return None

with open('sequences.txt', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

with open('fix_log.txt', 'w', encoding='utf-8') as out:
    for line in lines:
        if not line: continue
        seq = eval(line)
        fixed = unmojibake(seq)
        if fixed:
            out.write(f'{repr(seq)} -> {repr(fixed)}\n')
