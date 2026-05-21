import sys

def analyze(filepath):
    print(f"--- Analyzing {filepath} ---")
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if any(ord(c) > 127 for c in line):
            encoded_line = line.strip().encode('ascii', 'backslashreplace').decode('ascii')
            print(f"{i+1}: {encoded_line}")

analyze('d:/cookie/custom.html')
analyze('d:/cookie/classes.html')
