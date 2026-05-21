import re

with open('d:/cookie/custom.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Insert CSS
new_css = """
    /* --- NEW CREATIVE CUSTOM PAGE CSS --- */
    .creative-main {
      background-color: var(--cream, #FAF6EE);
      overflow-x: hidden;
      font-family: 'DM Sans', sans-serif;
    }
    
    /* Marquee */
    .marquee-container {
      width: 100%;
      background: linear-gradient(90deg, #c77a3f, #eab67a);
      color: #fff;
      padding: 15px 0;
      overflow: hidden;
      display: flex;
      white-space: nowrap;
      font-weight: 600;
      letter-spacing: 2px;
      text-transform: uppercase;
      font-size: 0.9rem;
    }
    .marquee-content {
      display: flex;
      animation: marquee 20s linear infinite;
    }
    .marquee-content span { padding: 0 30px; }
    @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

    /* Hero */
    .creative-hero {
      min-height: 90vh;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 5% 8%;
      position: relative;
      background: var(--cream, #FAF6EE);
    }
    body.dark-mode .creative-hero { background: var(--cream, #1e1916); }
    
    .hero-glass-panel {
      flex: 1;
      max-width: 600px;
      background: rgba(255, 255, 255, 0.4);
      backdrop-filter: blur(20px);
      padding: 50px;
      border-radius: 30px;
      border: 1px solid rgba(255, 255, 255, 0.6);
      box-shadow: 0 30px 60px rgba(0,0,0,0.05);
      z-index: 10;
    }
    body.dark-mode .hero-glass-panel {
      background: rgba(40, 30, 25, 0.5);
      border-color: rgba(255,255,255,0.05);
      box-shadow: 0 30px 60px rgba(0,0,0,0.3);
    }
    
    .badge-new {
      display: inline-block;
      background: #c77a3f;
      color: white;
      padding: 6px 16px;
      border-radius: 50px;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      margin-bottom: 20px;
      letter-spacing: 1px;
    }
    
    .glitch-text {
      font-family: 'Playfair Display', serif;
      font-size: 4rem;
      line-height: 1.1;
      color: #2F241B;
      margin-bottom: 25px;
      position: relative;
    }
    body.dark-mode .glitch-text { color: #f0e2d4; }
    
    .hero-glass-panel p {
      font-size: 1.15rem;
      line-height: 1.7;
      color: #5d4a3d;
      margin-bottom: 40px;
    }
    body.dark-mode .hero-glass-panel p { color: #d4c4b7; }
    
    .action-group { display: flex; gap: 20px; flex-wrap: wrap; }
    
    .btn-creative-primary {
      background: linear-gradient(135deg, #c77a3f, #b35f2a);
      color: white;
      padding: 16px 32px;
      border-radius: 50px;
      text-decoration: none;
      font-weight: 600;
      font-size: 1.05rem;
      transition: all 0.3s ease;
      box-shadow: 0 10px 20px rgba(199, 122, 63, 0.3);
    }
    .btn-creative-primary:hover { transform: translateY(-3px); box-shadow: 0 15px 30px rgba(199, 122, 63, 0.4); color: white; }
    
    .btn-creative-secondary {
      background: transparent;
      color: #b35f2a;
      padding: 16px 32px;
      border-radius: 50px;
      text-decoration: none;
      font-weight: 600;
      font-size: 1.05rem;
      border: 2px solid #c77a3f;
      transition: all 0.3s ease;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    body.dark-mode .btn-creative-secondary { color: #eab67a; border-color: #eab67a; }
    .btn-creative-secondary:hover { background: #c77a3f; color: white; }
    body.dark-mode .btn-creative-secondary:hover { background: #eab67a; color: #1e1916; }

    .hero-visual {
      flex: 1;
      position: relative;
      height: 600px;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    
    .blob-bg {
      position: absolute;
      width: 500px;
      height: 500px;
      background: linear-gradient(135deg, #f7ede2, #f0dfce);
      border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%;
      animation: morph 8s ease-in-out infinite alternate;
      z-index: 1;
    }
    body.dark-mode .blob-bg { background: linear-gradient(135deg, #3a2c22, #2c211a); }
    
    @keyframes morph { 0% { border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%; } 100% { border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%; } }
    
    .floating-cookie {
      position: absolute;
      border-radius: 50%;
      overflow: hidden;
      box-shadow: 0 25px 50px rgba(0,0,0,0.15);
      z-index: 2;
      border: 6px solid white;
      animation: float 6s ease-in-out infinite;
    }
    body.dark-mode .floating-cookie { border-color: #251f1a; box-shadow: 0 25px 50px rgba(0,0,0,0.4); }
    
    .floating-cookie img { width: 100%; height: 100%; object-fit: cover; }
    
    .cookie-1 { width: 280px; height: 280px; top: 10%; right: 10%; animation-delay: 0s; }
    .cookie-2 { width: 180px; height: 180px; bottom: 15%; right: 40%; animation-delay: 1.5s; }
    .cookie-3 { width: 140px; height: 140px; top: 40%; left: 10%; animation-delay: 3s; }
    
    @keyframes float { 0%, 100% { transform: translateY(0) rotate(0deg); } 50% { transform: translateY(-20px) rotate(5deg); } }

    /* Tiers */
    .creative-tiers {
      padding: 100px 5%;
      background: #fff;
    }
    body.dark-mode .creative-tiers { background: #16120f; }
    
    .section-title {
      font-family: 'Playfair Display', serif;
      font-size: 3rem;
      text-align: center;
      margin-bottom: 60px;
      color: #2F241B;
    }
    body.dark-mode .section-title { color: #f0e2d4; }
    
    .tiers-wrapper {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 40px;
      max-width: 1200px;
      margin: 0 auto;
    }
    
    .tier-card {
      background: var(--cream, #FAF6EE);
      border-radius: 30px;
      padding: 50px 40px;
      position: relative;
      transition: all 0.4s ease;
      border: 1px solid rgba(0,0,0,0.05);
    }
    body.dark-mode .tier-card { background: #251e19; border-color: rgba(255,255,255,0.05); }
    
    .tier-card:hover { transform: translateY(-15px); box-shadow: 0 30px 60px rgba(199,122,63,0.15); }
    body.dark-mode .tier-card:hover { box-shadow: 0 30px 60px rgba(0,0,0,0.4); }
    
    .featured-tier {
      background: linear-gradient(145deg, #ffffff, #fdf5eb);
      transform: scale(1.05);
      border: 2px solid #eab67a;
      box-shadow: 0 20px 40px rgba(0,0,0,0.05);
    }
    body.dark-mode .featured-tier {
      background: linear-gradient(145deg, #2a221d, #1e1916);
      box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    }
    .featured-tier:hover { transform: scale(1.05) translateY(-10px); }
    
    .tier-badge {
      position: absolute;
      top: -15px;
      left: 50%;
      transform: translateX(-50%);
      background: #c77a3f;
      color: white;
      padding: 6px 20px;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 1px;
      text-transform: uppercase;
    }
    
    .tier-icon {
      font-size: 2.5rem;
      color: #c77a3f;
      margin-bottom: 25px;
    }
    
    .tier-card h3 {
      font-family: 'Playfair Display', serif;
      font-size: 2rem;
      color: #2F241B;
      margin-bottom: 15px;
    }
    body.dark-mode .tier-card h3 { color: #f0e2d4; }
    
    .tier-card p {
      color: #6b5545;
      line-height: 1.6;
      margin-bottom: 30px;
      font-size: 0.95rem;
    }
    body.dark-mode .tier-card p { color: #bbaaa0; }
    
    .tier-features {
      list-style: none;
      margin-bottom: 40px;
      padding-left: 0;
    }
    .tier-features li {
      margin-bottom: 15px;
      display: flex;
      align-items: center;
      gap: 12px;
      color: #2F241B;
      font-weight: 500;
    }
    body.dark-mode .tier-features li { color: #e2cfbc; }
    .tier-features li i { color: #c77a3f; }
    
    .tier-btn {
      width: 100%;
      padding: 16px;
      border-radius: 50px;
      background: transparent;
      border: 2px solid #c77a3f;
      color: #c77a3f;
      font-weight: 700;
      font-size: 1rem;
      cursor: pointer;
      transition: all 0.3s;
      font-family: inherit;
    }
    .tier-btn:hover { background: #c77a3f; color: white; }
    .tier-btn.primary { background: #c77a3f; color: white; }
    .tier-btn.primary:hover { background: #b35f2a; border-color: #b35f2a; }
    
    /* Masonry Gallery */
    .creative-gallery {
      padding: 100px 5%;
      background: var(--cream, #FAF6EE);
    }
    body.dark-mode .creative-gallery { background: #1e1916; }
    
    .masonry-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      grid-auto-rows: 250px;
      gap: 20px;
      max-width: 1400px;
      margin: 0 auto;
    }
    
    .masonry-item {
      border-radius: 20px;
      overflow: hidden;
      position: relative;
      cursor: pointer;
    }
    .masonry-item img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s ease;
    }
    .masonry-item:hover img { transform: scale(1.1); }
    
    .masonry-item::after {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(0,0,0,0.5), transparent);
      opacity: 0;
      transition: opacity 0.3s;
    }
    .masonry-item:hover::after { opacity: 1; }
    
    .masonry-item.tall { grid-row: span 2; }
    .masonry-item.wide { grid-column: span 2; }
    
    @media (max-width: 900px) {
      .creative-hero { flex-direction: column; text-align: center; padding-top: 120px; }
      .hero-glass-panel { padding: 30px; margin-bottom: 40px; }
      .action-group { justify-content: center; }
      .glitch-text { font-size: 3rem; }
      .hero-visual { width: 100%; height: 400px; }
      .blob-bg { width: 350px; height: 350px; }
      .cookie-1 { width: 200px; height: 200px; }
      .cookie-2 { width: 120px; height: 120px; right: 20%; }
      .cookie-3 { width: 100px; height: 100px; }
      .featured-tier { transform: scale(1); }
      .featured-tier:hover { transform: translateY(-10px); }
      .masonry-item.wide { grid-column: span 1; }
    }
    @media (max-width: 600px) {
      .glitch-text { font-size: 2.5rem; }
      .hero-visual { display: none; }
      .btn-creative-primary, .btn-creative-secondary { width: 100%; justify-content: center; }
      .masonry-item.tall { grid-row: span 1; }
    }
"""

html = html.replace('</style>', new_css + '\n</style>')

# 2. Extract Navbar and Head
nav_end_idx = html.find('</nav>') + len('</nav>')
head_and_nav = html[:nav_end_idx]

# 3. Extract Footer and scripts
footer_start_idx = html.find('<footer class="site-footer">')
footer_and_scripts = html[footer_start_idx:]

# 4. New HTML Content
new_html = """
<main class="creative-main">
  <!-- Dynamic Marquee -->
  <div class="marquee-container">
    <div class="marquee-content">
      <span>✨ Elevate Your Celebrations ✨ Custom Artistry ✨ Unique Flavors ✨ Bespoke Designs ✨ Handcrafted with Love ✨</span>
      <span>✨ Elevate Your Celebrations ✨ Custom Artistry ✨ Unique Flavors ✨ Bespoke Designs ✨ Handcrafted with Love ✨</span>
    </div>
  </div>

  <!-- Hero Interactive -->
  <section class="creative-hero">
    <div class="hero-glass-panel">
      <div class="badge-new">Your Vision, Baked to Perfection</div>
      <h1 class="glitch-text" data-text="Edible Masterpieces">Edible Masterpieces</h1>
      <p>Transforming your wildest ideas into breathtaking, mouth-watering cookie art. Whether it's a corporate gala, an intimate wedding, or a grand birthday bash, we craft cookies that steal the show.</p>
      <div class="action-group">
        <a href="#order-canvas" class="btn-creative-primary">Start Your Canvas</a>
        <a href="#gallery" class="btn-creative-secondary">View Inspiration <i class="fas fa-arrow-right"></i></a>
      </div>
    </div>
    <div class="hero-visual">
      <div class="floating-cookie cookie-1"><img src="./images/gallery 13.jpg" alt="Custom Cookie"></div>
      <div class="floating-cookie cookie-2"><img src="./images/gallery 7.jpg" alt="Custom Cookie"></div>
      <div class="floating-cookie cookie-3"><img src="./images/gallery 17.jpg" alt="Custom Cookie"></div>
      <div class="blob-bg"></div>
    </div>
  </section>

  <!-- Interactive Tiers -->
  <section class="creative-tiers" id="order-canvas">
    <h2 class="section-title">The Art of Customization</h2>
    <div class="tiers-wrapper">
      <div class="tier-card">
        <div class="tier-icon"><i class="fas fa-paint-brush"></i></div>
        <h3>The Classic</h3>
        <p>Perfect for birthdays and small gatherings. Includes up to 3 custom shapes and 2 colors.</p>
        <ul class="tier-features">
           <li><i class="fas fa-check"></i> 3 Custom Shapes</li>
           <li><i class="fas fa-check"></i> 2 Hand-mixed Colors</li>
           <li><i class="fas fa-check"></i> Standard Packaging</li>
        </ul>
        <button class="tier-btn">Select Classic</button>
      </div>
      <div class="tier-card featured-tier">
        <div class="tier-badge">Most Popular</div>
        <div class="tier-icon"><i class="fas fa-crown"></i></div>
        <h3>The Signature</h3>
        <p>Our most requested package. Ideal for weddings and corporate events. Up to 6 shapes.</p>
        <ul class="tier-features">
           <li><i class="fas fa-check"></i> 6 Custom Shapes</li>
           <li><i class="fas fa-check"></i> Unlimited Colors</li>
           <li><i class="fas fa-check"></i> Metallic Gold/Silver Accents</li>
           <li><i class="fas fa-check"></i> Premium Gift Boxes</li>
        </ul>
        <button class="tier-btn primary">Select Signature</button>
      </div>
      <div class="tier-card">
        <div class="tier-icon"><i class="fas fa-gem"></i></div>
        <h3>The Extravagant</h3>
        <p>No limits. 3D structures, hand-painted portraits, and luxury flavor profiles.</p>
        <ul class="tier-features">
           <li><i class="fas fa-check"></i> Unlimited Shapes & Colors</li>
           <li><i class="fas fa-check"></i> Hand-Painted Portraits</li>
           <li><i class="fas fa-check"></i> Luxury Flavor Profiles</li>
           <li><i class="fas fa-check"></i> Individual Ribbon Tying</li>
        </ul>
        <button class="tier-btn">Select Extravagant</button>
      </div>
    </div>
  </section>

  <!-- Masonry Gallery Inspiration -->
  <section class="creative-gallery" id="gallery">
    <h2 class="section-title">Endless Possibilities</h2>
    <div class="masonry-grid">
      <div class="masonry-item tall"><img src="./images/classes 11.jpg" alt="Inspiration 1"></div>
      <div class="masonry-item"><img src="./images/gallery 8.jpg" alt="Inspiration 2"></div>
      <div class="masonry-item wide"><img src="./images/about 5.jpg" alt="Inspiration 3"></div>
      <div class="masonry-item"><img src="./images/tutorials 9.jpg" alt="Inspiration 4"></div>
      <div class="masonry-item tall"><img src="./images/contact 2.png" alt="Inspiration 5"></div>
      <div class="masonry-item"><img src="./images/gallery 4.jpg" alt="Inspiration 6"></div>
    </div>
  </section>
</main>
"""

# 5. Save the updated file
final_html = head_and_nav + '\n' + new_html + '\n' + footer_and_scripts

with open('d:/cookie/custom.html', 'w', encoding='utf-8') as f:
    f.write(final_html)
    
print("custom.html successfully updated!")
