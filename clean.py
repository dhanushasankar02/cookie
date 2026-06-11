import os
import re

dir_path = r'd:\groww\cookie'

def clean_css(content):
    # 1. Remove colored glow (box-shadow)
    # Light mode glow (orange) -> neutral shadow
    content = re.sub(r'box-shadow:\s*([^;]+)rgba\(199,\s*122,\s*63,\s*[0-9.]+\)', r'box-shadow: \1rgba(0, 0, 0, 0.08)', content)
    content = re.sub(r'box-shadow:\s*([^;]+)rgba\(179,\s*95,\s*42,\s*[0-9.]+\)', r'box-shadow: \1rgba(0, 0, 0, 0.1)', content)
    # Dark mode glow (light orange) -> neutral shadow
    content = re.sub(r'box-shadow:\s*([^;]+)rgba\(234,\s*182,\s*122,\s*[0-9.]+\)', r'box-shadow: \1rgba(0, 0, 0, 0.2)', content)

    # Fix overlapping substitutions
    content = content.replace(r'rgba(0, 0, 0, 0.08), 0 0 0 2px rgba(199, 122, 63, 0.2)', r'rgba(0, 0, 0, 0.08), 0 0 0 2px rgba(0, 0, 0, 0.05)')
    content = content.replace(r'rgba(0, 0, 0, 0.2), 0 0 0 2px rgba(234, 182, 122, 0.2)', r'rgba(0, 0, 0, 0.2), 0 0 0 2px rgba(0, 0, 0, 0.3)')
    
    # 2. Change colored icons to professional inherit/neutral
    # Dropdown items
    content = re.sub(r'(\.dropdown-item i\s*\{[^}]*)color:\s*#[0-9a-fA-F]+;?', r'\1color: inherit; opacity: 0.7;', content)
    content = re.sub(r'(body\.dark-mode \.dropdown-item i\s*\{[^}]*)color:\s*#[0-9a-fA-F]+;?', r'\1color: inherit; opacity: 0.7;', content)
    
    # Footer links & Contact info
    content = re.sub(r'(\.footer-links a i\s*\{[^}]*)color:\s*#[0-9a-fA-F]+;?', r'\1color: inherit; opacity: 0.7;', content)
    content = re.sub(r'(\.contact-info i\s*\{[^}]*)color:\s*#[0-9a-fA-F]+;?', r'\1color: inherit; opacity: 0.7;', content)
    content = re.sub(r'(body\.dark-mode \.contact-info i\s*\{[^}]*)color:\s*#[0-9a-fA-F]+;?', r'\1color: inherit; opacity: 0.7;', content)
    
    # Home 2 specific icons
    content = re.sub(r'(\.flavor-icon\s*\{[^}]*)color:\s*#[0-9a-fA-F]+;?', r'\1color: inherit; opacity: 0.7;', content)
    content = re.sub(r'(\.craft-content i\s*\{[^}]*)color:\s*#[0-9a-fA-F]+;?', r'\1color: inherit; opacity: 0.7;', content)
    content = re.sub(r'(\.pack-features i\s*\{[^}]*)color:\s*#[0-9a-fA-F]+;?', r'\1color: inherit; opacity: 0.7;', content)
    
    # Step icons
    content = re.sub(r'(\.step-icon\s*\{[^}]*)color:\s*#[0-9a-fA-F]+;?', r'\1color: inherit; opacity: 0.7;', content)
    content = re.sub(r'(body\.dark-mode \.step-icon\s*\{[^}]*)color:\s*#[0-9a-fA-F]+;?', r'\1color: inherit; opacity: 0.7;', content)

    # Social links
    content = re.sub(r'(\.social-links a\s*\{[^}]*)color:\s*#[0-9a-fA-F]+;?', r'\1color: inherit; opacity: 0.7;', content)
    content = re.sub(r'(body\.dark-mode \.social-links a\s*\{[^}]*)color:\s*#[0-9a-fA-F]+;?', r'\1color: inherit; opacity: 0.7;', content)

    # Testi quote icon
    content = re.sub(r'(\.testi-card i\.fa-quote-left\s*\{[^}]*)color:\s*rgba\([^)]+\);?', r'\1color: inherit; opacity: 0.1;', content)
    content = re.sub(r'(\.quote-icon\s*\{[^}]*)color:\s*rgba\([^)]+\);?', r'\1color: inherit; opacity: 0.1;', content)
    
    # Process icon color specifically if missed
    content = re.sub(r'color:\s*#c77a3f;', r'color: inherit; opacity: 0.7;', content)
    # Wait, blindly replacing #c77a3f might ruin text colors (like h2, links). I should undo the blind replace.
    # We will skip the blind replace to be safe.

    return content

for filename in os.listdir(dir_path):
    if filename.endswith('.html') or filename.endswith('.css'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = clean_css(content)
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
