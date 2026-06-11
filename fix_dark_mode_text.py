import os
import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False

    # 1. Update the toggle button HTML in navbar
    old_btn = '<button id="darkModeToggle" class="btn-outline" aria-label="Dark mode toggle"><i class="fas fa-moon"></i></button>'
    new_btn = '<button id="darkModeToggle" class="btn-outline" aria-label="Dark mode toggle"><i class="fas fa-moon"></i> Dark Mode</button>'
    if old_btn in content:
        content = content.replace(old_btn, new_btn)
        modified = True

    # 2. Update the JS logic in navbar pages
    old_js = "darkToggle.innerHTML = isDark ? '<i class=\"fas fa-sun\"></i>' : '<i class=\"fas fa-moon\"></i>';"
    new_js = "darkToggle.innerHTML = isDark ? '<i class=\"fas fa-sun\"></i> Light Mode' : '<i class=\"fas fa-moon\"></i> Dark Mode';"
    if old_js in content:
        content = content.replace(old_js, new_js)
        modified = True

    # 3. Update login/register HTML
    old_login_btn = '<div class="control-btn" id="darkModeToggle" title="Dark Mode">🌙</div>'
    new_login_btn = '<div class="control-btn" id="darkModeToggle" title="Dark Mode" style="width:auto; padding:0 15px; font-size:1rem; gap:8px;">🌙 Dark Mode</div>'
    if old_login_btn in content:
        content = content.replace(old_login_btn, new_login_btn)
        modified = True
        
    old_rtl_btn = '<div class="control-btn" id="rtlToggle" title="RTL Mode">⇄</div>'
    new_rtl_btn = '<div class="control-btn" id="rtlToggle" title="RTL Mode" style="width:auto; padding:0 15px; font-size:1rem; gap:8px;">⇄ RTL Mode</div>'
    if old_rtl_btn in content:
        content = content.replace(old_rtl_btn, new_rtl_btn)
        modified = True

    # 4. Update login/register JS
    old_login_js = "darkToggle.innerHTML = isDark ? '☀️' : '🌙';"
    new_login_js = "darkToggle.innerHTML = isDark ? '☀️ Light Mode' : '🌙 Dark Mode';"
    if old_login_js in content:
        content = content.replace(old_login_js, new_login_js)
        modified = True

    # RTL JS for login/register
    if "rtlToggle.innerHTML = 'LTR';" in content:
        content = content.replace("rtlToggle.innerHTML = 'LTR';", "rtlToggle.innerHTML = 'LTR Mode';")
        modified = True
    if "rtlToggle.innerHTML = '⇄';" in content:
        content = content.replace("rtlToggle.innerHTML = '⇄';", "rtlToggle.innerHTML = '⇄ RTL Mode';")
        modified = True

    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

print("Done.")
