import glob
import re

for f in glob.glob('d:/cookie/*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Update .nav-link.active
    content = re.sub(r'\.nav-link\.active\s*\{\s*color:\s*#[a-fA-F0-9]+;', '.nav-link.active { color: red;', content)
    
    # 2. Update body.dark-mode .nav-link.active
    content = re.sub(r'body\.dark-mode\s+\.nav-link\.active\s*\{\s*color:\s*#[a-fA-F0-9]+;', 'body.dark-mode .nav-link.active { color: red;', content)
    
    # 3. Update .dropdown-item.active
    content = re.sub(
        r'\.dropdown-item:hover,\s*\.dropdown-item\.active\s*\{\s*(background-color:[^;]+;)\s*color:\s*#[a-fA-F0-9]+;\s*\}',
        r'.dropdown-item:hover { \1 color: #c16f34; }\n    .dropdown-item.active { \1 color: red; }',
        content
    )

    # 4. Update body.dark-mode .dropdown-item.active
    content = re.sub(
        r'body\.dark-mode\s+\.dropdown-item:hover,\s*body\.dark-mode\s+\.dropdown-item\.active\s*\{\s*color:\s*#[a-fA-F0-9]+;\s*\}',
        r'body.dark-mode .dropdown-item:hover { color: #f7c894; }\n    body.dark-mode .dropdown-item.active { color: red; }',
        content
    )

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated {f}")
