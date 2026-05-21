import glob

old_text = """      // Highlight active nav item
      const currentPath = window.location.pathname.split('/').pop() || 'index.html';
      const navLinks = document.querySelectorAll('.nav-menu .nav-link, .dropdown-item');
      navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath) {
          link.classList.add('active');
          if (link.classList.contains('dropdown-item')) {
            const parentToggle = document.getElementById('homeDropdownToggle');
            if (parentToggle) parentToggle.classList.add('active');
          }
        }
      });"""

new_text = """      // Highlight active nav item
      const currentPath = (window.location.pathname.split('/').pop() || 'index.html').toLowerCase();
      const navLinks = document.querySelectorAll('.nav-menu .nav-link, .dropdown-item');
      navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href && href.replace(/^\.\//, '').toLowerCase() === currentPath) {
          link.classList.add('active');
          if (link.classList.contains('dropdown-item')) {
            const parentToggle = document.getElementById('homeDropdownToggle');
            if (parentToggle) parentToggle.classList.add('active');
          }
        }
      });"""

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
