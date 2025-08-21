app_js_code = '''// Google AdSense is best added as <script> in HTML, not inside app.js

// However, you can include this standard Ads initialization code in app.js if needed

(window.adsbygoogle = window.adsbygoogle || []).push({});

// Smooth scrolling for navigation links

document.querySelectorAll('nav a').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    if (this.hash !== "") {
      e.preventDefault();
      const target = document.querySelector(this.hash);
      if (target) {
        target.scrollIntoView({ behavior: 'smooth' });
      }
    }
  });
});

// Responsive nav toggle for mobile
const nav = document.querySelector('nav');
const toggleButton = document.createElement('button');
toggleButton.textContent = 'Menu';
toggleButton.classList.add('nav-toggle');
nav.prepend(toggleButton);

toggleButton.addEventListener('click', () => {
  nav.classList.toggle('nav-open');
});
'''

style_css_code = '''/* Reset margin and padding */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Typography */
body, html {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f6fff6;
  color: #333;
  scroll-behavior: smooth;
  line-height: 1.6;
  min-height: 100vh;
}

/* Navigation Bar */
nav {
  background-color: #38ef7d;
  padding: 15px 20px;
  display: flex;
  justify-content: center;
  position: sticky;
  top: 0;
  z-index: 1000;
  font-weight: bold;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

nav a {
  color: white;
  text-decoration: none;
  margin: 0 20px;
  font-size: 1.1rem;
  transition: color 0.3s ease;
}

nav a:hover,
nav a:focus {
  color: #004d40;
}

/* Responsive Navigation Toggle Button */
.nav-toggle {
  display: none;
  background-color: #11998e;
  color: white;
  border: none;
  padding: 8px 14px;
  font-size: 1rem;
  cursor: pointer;
  border-radius: 4px;
  margin-right: auto;
}

/* Show toggle in small devices */
@media (max-width: 768px) {
  nav {
    flex-wrap: wrap;
    justify-content: flex-start;
  }

  nav a {
    flex: 1 1 100%;
    margin: 10px 0;
    text-align: center;
  }

  .nav-toggle {
    display: block;
  }

  nav:not(.nav-open) a {
    display: none;
  }

  nav.nav-open a {
    display: block;
  }
}

/* Main container */
.container {
  max-width: 1100px;
  margin: auto;
  padding: 20px 15px;
}

/* Headings */
h1, h2, h3 {
  color: #11998e;
  margin-bottom: 15px;
}

/* Links */
a {
  color: #11998e;
}

a:hover {
  text-decoration: underline;
}

/* Footer */
footer {
  background-color: #11998e;
  color: white;
  text-align: center;
  padding: 20px 10px;
  margin-top: 40px;
  font-size: 0.95rem;
}

/* AdSense container styling */
ins.adsbygoogle {
  display: block;
  margin: 25px auto;
  text-align: center;
  max-width: 100%;
}

/* Card styling (if used) */
.card {
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 25px rgba(0, 0, 0, 0.05);
  padding: 25px;
  margin-bottom: 30px;
  transition: box-shadow 0.3s ease;
}

.card:hover {
  box-shadow: 0 8px 40px rgba(0, 0, 0, 0.1);
}
'''

# Write app.js
app_js_path = "static/js/app.js"
style_css_path = "static/css/style.css"

import os
os.makedirs(os.path.dirname(app_js_path), exist_ok=True)
os.makedirs(os.path.dirname(style_css_path), exist_ok=True)

with open(app_js_path, "w", encoding="utf-8") as f:
    f.write(app_js_code)

with open(style_css_path, "w", encoding="utf-8") as f:
    f.write(style_css_code)

(app_js_path, style_css_path)