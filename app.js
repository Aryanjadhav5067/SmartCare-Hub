// Google AdSense is best added as <script> in HTML, not inside app.js

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
