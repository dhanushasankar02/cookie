import re

with open('classes.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CSS
css_start = content.find('/* ── HERO ── */')
css_end = content.find('/* ── RESPONSIVE ── */')

new_css = """/* ── HERO WORKSHOPS ── */
    .hero {
      position: relative;
      width: 100%;
      height: 70vh;
      min-height: 500px;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
    }
    .hero-bg {
      position: absolute;
      inset: 0;
      background: url('./images/classes 5.jpg') center/cover no-repeat;
      z-index: 0;
    }
    .hero-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(160deg, rgba(58,32,21,0.7) 0%, rgba(58,32,21,0.5) 55%, rgba(58,32,21,0.8) 100%);
      z-index: 1;
    }
    .hero-content {
      position: relative;
      z-index: 3;
      max-width: 820px;
      padding: 24px;
      opacity: 0;
      animation: fadeInUp 1.1s ease-out 0.2s forwards;
    }
    .hero-glass {
      background: rgba(255,255,255,0.15);
      backdrop-filter: blur(14px);
      border: 1px solid rgba(255,255,255,0.3);
      border-radius: var(--radius-xl);
      padding: 52px 60px;
    }
    .hero-eyebrow {
      font-family: var(--font-body);
      font-size: 0.85rem;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      color: #f7c894;
      margin-bottom: 20px;
      display: block;
      font-weight: 600;
    }
    .hero h1 {
      font-family: var(--font-display);
      font-size: clamp(2.8rem, 5.5vw, 4.8rem);
      font-weight: 800;
      color: #ffffff;
      line-height: 1.1;
      margin-bottom: 22px;
    }
    .hero h1 em { font-style: italic; font-weight: 600; color: #ffebcc; }
    .hero-sub {
      font-size: 1.15rem;
      color: rgba(255,255,255,0.9);
      font-weight: 400;
      line-height: 1.75;
      max-width: 600px;
      margin: 0 auto;
    }

    /* ── MARQUEE ── */
    .marquee-strip {
      background: var(--espresso);
      color: var(--sand);
      padding: 13px 0;
      overflow: hidden;
      white-space: nowrap;
      font-size: 0.8rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      font-family: var(--font-body);
      font-weight: 600;
    }
    .marquee-track {
      display: inline-block;
      animation: marquee 30s linear infinite;
    }

    /* ── SECTION SHARED ── */
    .container { max-width: 1200px; margin: 0 auto; padding: 0 28px; }
    .section-title {
      text-align: center;
      font-family: var(--font-display);
      font-size: clamp(2.2rem, 5vw, 3.2rem);
      font-weight: 800;
      color: var(--mocha);
      margin-bottom: 20px;
    }
    body.dark-mode .section-title { color: var(--mocha); }
    .section-subtitle {
      text-align: center;
      font-size: 1.1rem;
      color: var(--text-mid);
      max-width: 700px;
      margin: 0 auto 60px;
      line-height: 1.7;
    }
    body.dark-mode .section-subtitle { color: var(--text-light); }

    /* ── SCHEDULE CARDS ── */
    .section-schedule {
      padding: 100px 0;
      background: var(--cream);
    }
    .schedule-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 30px;
    }
    .class-card {
      background: var(--white);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-soft);
      transition: transform var(--transition), box-shadow var(--transition);
      display: flex;
      flex-direction: column;
    }
    body.dark-mode .class-card {
      background: rgba(37, 30, 25, 0.85);
    }
    .class-card:hover {
      transform: translateY(-8px);
      box-shadow: var(--shadow-lift);
    }
    .class-img {
      height: 220px;
      width: 100%;
      object-fit: cover;
    }
    .class-content {
      padding: 30px;
      flex-grow: 1;
      display: flex;
      flex-direction: column;
    }
    .class-tags {
      display: flex;
      gap: 10px;
      margin-bottom: 15px;
    }
    .tag {
      background: #f0e6d2;
      color: var(--bark);
      padding: 4px 12px;
      border-radius: var(--radius-pill);
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    body.dark-mode .tag { background: #3a2e24; color: var(--amber); }
    .class-title {
      font-family: var(--font-display);
      font-size: 1.6rem;
      color: var(--espresso);
      margin-bottom: 12px;
      font-weight: 700;
    }
    body.dark-mode .class-title { color: #f0e2d4; }
    .class-desc {
      color: var(--text-mid);
      font-size: 0.95rem;
      margin-bottom: 20px;
      line-height: 1.6;
    }
    body.dark-mode .class-desc { color: var(--text-light); }
    .class-details {
      margin-top: auto;
      border-top: 1px solid rgba(0,0,0,0.08);
      padding-top: 20px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 15px;
      font-size: 0.9rem;
      color: var(--text-dark);
    }
    body.dark-mode .class-details { border-top-color: rgba(255,255,255,0.1); color: #e2cfbc; }
    .detail-item {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .detail-item i { color: var(--amber); }
    .class-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: 25px;
    }
    .class-price {
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--mocha);
      font-family: var(--font-display);
    }
    body.dark-mode .class-price { color: var(--amber); }
    .btn-book {
      background: var(--mocha);
      color: var(--white);
      padding: 10px 24px;
      border-radius: var(--radius-pill);
      font-weight: 600;
      transition: background 0.2s;
      border: none;
      cursor: pointer;
    }
    body.dark-mode .btn-book { background: var(--amber); color: var(--white); }
    .btn-book:hover { background: var(--amber); }

    /* ── CURRICULUM / SKILLS ── */
    .section-curriculum {
      padding: 100px 0;
      background: var(--parchment);
    }
    .curriculum-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 60px;
      align-items: center;
    }
    .curriculum-text h3 {
      font-family: var(--font-display);
      font-size: 2.2rem;
      color: var(--espresso);
      margin-bottom: 20px;
    }
    body.dark-mode .curriculum-text h3 { color: #f0e2d4; }
    .skill-list {
      list-style: none;
      margin-top: 30px;
    }
    .skill-list li {
      margin-bottom: 15px;
      display: flex;
      align-items: flex-start;
      gap: 15px;
      font-size: 1.05rem;
      color: var(--text-dark);
    }
    body.dark-mode .skill-list li { color: #d4c4b7; }
    .skill-list i {
      color: var(--amber);
      font-size: 1.2rem;
      margin-top: 3px;
    }
    .curriculum-image {
      position: relative;
    }
    .curriculum-image img {
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-lift);
      width: 100%;
    }

    /* ── INSTRUCTOR ── */
    .section-instructor {
      padding: 100px 0;
      background: var(--cream);
    }
    .instructor-wrap {
      display: flex;
      background: var(--white);
      border-radius: var(--radius-xl);
      overflow: hidden;
      box-shadow: var(--shadow-lift);
      max-width: 1000px;
      margin: 0 auto;
    }
    body.dark-mode .instructor-wrap { background: #251e19; }
    .instructor-img {
      flex: 0 0 45%;
      position: relative;
    }
    .instructor-img img {
      height: 100%;
      width: 100%;
      object-fit: cover;
      position: absolute;
      inset: 0;
    }
    .instructor-content {
      padding: 60px 50px;
      flex: 1;
    }
    .instructor-eyebrow {
      color: var(--amber);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      font-size: 0.85rem;
      margin-bottom: 10px;
    }
    .instructor-name {
      font-family: var(--font-display);
      font-size: 2.4rem;
      color: var(--espresso);
      margin-bottom: 20px;
      font-weight: 700;
    }
    body.dark-mode .instructor-name { color: #f0e2d4; }
    .instructor-bio {
      color: var(--text-mid);
      font-size: 1.05rem;
      line-height: 1.7;
      margin-bottom: 30px;
    }
    body.dark-mode .instructor-bio { color: var(--text-light); }
    .instructor-stats {
      display: flex;
      gap: 30px;
    }
    .stat {
      text-align: center;
    }
    .stat-num {
      display: block;
      font-family: var(--font-display);
      font-size: 2rem;
      color: var(--mocha);
      font-weight: 800;
    }
    body.dark-mode .stat-num { color: var(--amber); }
    .stat-label {
      font-size: 0.8rem;
      color: var(--text-light);
      text-transform: uppercase;
      letter-spacing: 0.1em;
      font-weight: 600;
    }
"""

if css_start != -1 and css_end != -1:
    content = content[:css_start] + new_css + content[css_end:]
else:
    print("CSS markers not found")

# Replace HTML
html_start = content.find('<!-- ── HERO ── -->')
html_end = content.find('<!-- ========== UNIFIED FOOTER')

new_html = """<!-- ── HERO WORKSHOP ── -->
  <section class="hero">
    <div class="hero-bg" style="background-image: url('./images/classes 3.jpg');"></div>
    <div class="hero-overlay"></div>

    <div class="hero-content">
      <div class="hero-glass">
        <span class="hero-eyebrow">Interactive Learning Experiences</span>
        <h1>Cookie Decorating<br><em>Workshops</em></h1>
        <p class="hero-sub">
          Master the art of royal icing, discover professional techniques, and create edible masterpieces in our hands-on artisan classes.
        </p>
      </div>
    </div>
  </section>

  <!-- ── MARQUEE ── -->
  <div class="marquee-strip">
    <div class="marquee-track">
      <span>Royal Icing Basics &nbsp;·&nbsp; Floral Piping &nbsp;·&nbsp; Advanced Flooding &nbsp;·&nbsp; Watercolor Cookies &nbsp;·&nbsp; Holiday Themes &nbsp;·&nbsp; Kids Workshops &nbsp;·&nbsp; Private Events &nbsp;·&nbsp; Airbrushing Techniques &nbsp;·&nbsp;</span>
      <span aria-hidden="true">Royal Icing Basics &nbsp;·&nbsp; Floral Piping &nbsp;·&nbsp; Advanced Flooding &nbsp;·&nbsp; Watercolor Cookies &nbsp;·&nbsp; Holiday Themes &nbsp;·&nbsp; Kids Workshops &nbsp;·&nbsp; Private Events &nbsp;·&nbsp; Airbrushing Techniques &nbsp;·&nbsp;</span>
    </div>
  </div>

  <!-- ── CLASS SCHEDULES ── -->
  <section class="section-schedule">
    <div class="container">
      <h2 class="section-title">Upcoming Classes</h2>
      <p class="section-subtitle">Join us in the studio for fun, interactive cookie decorating classes. All supplies are provided—just bring your creativity!</p>
      
      <div class="schedule-grid">
        <!-- Class 1 -->
        <div class="class-card">
          <img src="./images/classes 1.jpg" alt="Beginner Royal Icing" class="class-img">
          <div class="class-content">
            <div class="class-tags">
              <span class="tag">Beginner</span>
              <span class="tag">Royal Icing</span>
            </div>
            <h3 class="class-title">Royal Icing 101</h3>
            <p class="class-desc">Perfect for beginners! Learn icing consistencies, basic outlining, and flooding techniques to create smooth, flawless cookies.</p>
            <div class="class-details">
              <div class="detail-item"><i class="far fa-calendar-alt"></i> Oct 15, 2025</div>
              <div class="detail-item"><i class="far fa-clock"></i> 2.5 Hours</div>
              <div class="detail-item"><i class="fas fa-users"></i> Max 12 Seats</div>
              <div class="detail-item"><i class="fas fa-signal"></i> All Levels</div>
            </div>
            <div class="class-footer">
              <span class="class-price">$75</span>
              <button class="btn-book">Book Now</button>
            </div>
          </div>
        </div>

        <!-- Class 2 -->
        <div class="class-card">
          <img src="./images/classes 4.jpg" alt="Floral Cookie Art" class="class-img">
          <div class="class-content">
            <div class="class-tags">
              <span class="tag">Intermediate</span>
              <span class="tag">Piping</span>
            </div>
            <h3 class="class-title">Floral Cookie Art</h3>
            <p class="class-desc">Elevate your skills by learning how to pipe delicate roses, leaves, and intricate floral patterns directly onto your cookies.</p>
            <div class="class-details">
              <div class="detail-item"><i class="far fa-calendar-alt"></i> Oct 22, 2025</div>
              <div class="detail-item"><i class="far fa-clock"></i> 3.0 Hours</div>
              <div class="detail-item"><i class="fas fa-users"></i> Max 10 Seats</div>
              <div class="detail-item"><i class="fas fa-signal"></i> Intermed.</div>
            </div>
            <div class="class-footer">
              <span class="class-price">$85</span>
              <button class="btn-book">Book Now</button>
            </div>
          </div>
        </div>

        <!-- Class 3 -->
        <div class="class-card">
          <img src="./images/classes 6.jpg" alt="Advanced Techniques" class="class-img">
          <div class="class-content">
            <div class="class-tags">
              <span class="tag">Advanced</span>
              <span class="tag">Airbrushing</span>
            </div>
            <h3 class="class-title">Mastering Textures</h3>
            <p class="class-desc">Dive into advanced methods including airbrushing, stenciling, watercolor painting on icing, and dimensional piping.</p>
            <div class="class-details">
              <div class="detail-item"><i class="far fa-calendar-alt"></i> Nov 05, 2025</div>
              <div class="detail-item"><i class="far fa-clock"></i> 4.0 Hours</div>
              <div class="detail-item"><i class="fas fa-users"></i> Max 8 Seats</div>
              <div class="detail-item"><i class="fas fa-signal"></i> Advanced</div>
            </div>
            <div class="class-footer">
              <span class="class-price">$120</span>
              <button class="btn-book">Book Now</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── CURRICULUM OVERVIEW ── -->
  <section class="section-curriculum">
    <div class="container curriculum-grid">
      <div class="curriculum-image">
        <img src="./images/classes 7.jpg" alt="Workshop details and curriculum">
      </div>
      <div class="curriculum-text">
        <h3>What You Will Learn</h3>
        <p class="section-subtitle" style="text-align: left; margin: 0; max-width: 100%;">Our workshops are designed to take you from a cookie enthusiast to a confident decorator. Every session includes hands-on practice, personalized feedback, and all the tools you need.</p>
        <ul class="skill-list">
          <li>
            <i class="fas fa-check-circle"></i>
            <div>
              <strong>Dough & Baking Secrets</strong>
              <p style="margin-top: 5px; font-size: 0.95rem;">Learn our signature recipe for no-spread sugar cookies that taste as good as they look.</p>
            </div>
          </li>
          <li>
            <i class="fas fa-check-circle"></i>
            <div>
              <strong>Royal Icing Consistencies</strong>
              <p style="margin-top: 5px; font-size: 0.95rem;">Master the 3 core consistencies: stiff for details, medium for outlining, and flood for smooth bases.</p>
            </div>
          </li>
          <li>
            <i class="fas fa-check-circle"></i>
            <div>
              <strong>Color Theory & Mixing</strong>
              <p style="margin-top: 5px; font-size: 0.95rem;">Understand how to achieve deep, vibrant colors and prevent color bleeding.</p>
            </div>
          </li>
          <li>
            <i class="fas fa-check-circle"></i>
            <div>
              <strong>Professional Tools</strong>
              <p style="margin-top: 5px; font-size: 0.95rem;">Get comfortable with piping bags, scribe tools, airbrush machines, and edible markers.</p>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </section>

  <!-- ── INSTRUCTOR PROFILE ── -->
  <section class="section-instructor">
    <div class="container">
      <div class="instructor-wrap">
        <div class="instructor-img">
          <img src="./images/classes 5.jpg" alt="Lead Instructor">
        </div>
        <div class="instructor-content">
          <div class="instructor-eyebrow">Meet Your Guide</div>
          <h3 class="instructor-name">Elena Rodriguez</h3>
          <p class="instructor-bio">
            With over 12 years of professional baking and decorating experience, Elena has transformed her passion for edible art into a thriving educational studio. Her work has been featured in leading bridal magazines and culinary shows.
            <br><br>
            Elena believes that anyone can create beautiful cookies with the right techniques, patience, and a little bit of magic. Her teaching style is patient, encouraging, and detailed.
          </p>
          <div class="instructor-stats">
            <div class="stat">
              <span class="stat-num">500+</span>
              <span class="stat-label">Students</span>
            </div>
            <div class="stat">
              <span class="stat-num">15k+</span>
              <span class="stat-label">Cookies</span>
            </div>
            <div class="stat">
              <span class="stat-num">4.9</span>
              <span class="stat-label">Rating</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  """

if html_start != -1 and html_end != -1:
    content = content[:html_start] + new_html + content[html_end:]
else:
    print("HTML markers not found")

with open('classes.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated classes.html successfully")
