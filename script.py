import zipfile
import os

# Fixing the AdSense script to avoid f-string issue by escaping curly braces with double braces

# Create a directory to hold the improved website files
dir_name = "healthwisdom_full_website"
os.makedirs(dir_name, exist_ok=True)

# Save the navigation HTML snippet and AdSense script for reuse
nav_html = '''<nav>
  <a href="index.html">Home</a>
  <a href="diseases.html">Diseases</a>
  <a href="foods.html">Food Insights</a>
  <a href="tips.html">Health Tips</a>
  <a href="about.html">About</a>
  <a href="contact.html">Contact</a>
</nav>'''

adsense_script = '''<script data-ad-client="ca-pub-5739867765605477" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>'''

# The CSS style block common to all pages
style_css = '''
  body, html {
    margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: #f6fff6; color: #333; scroll-behavior: smooth;
  }
  a { text-decoration: none; color: #177a75; }
  a:hover { color: #0d4f4d; }
  h1, h2, h3 { color: #11998e; }
  h3 { margin-top: 0; }
  p, li { line-height: 1.5em; }
  ul { margin-left: 1.5em; }

  /* Container */
  .container {
    max-width: 1100px;
    margin: auto;
    padding: 20px;
  }

  /* Navigation */
  nav {
    background: #38ef7d;
    color: white;
    display: flex;
    justify-content: center;
    padding: 13px 0;
    position: sticky;
    top: 0;
    z-index: 10;
    font-weight: bold;
    box-shadow: 0 2px 4px rgba(0,0,0,0.15);
  }
  nav a {
    margin: 0 20px;
    color: white;
    font-size: 1.1rem;
  }
  nav a:hover {
    color: #004d40;
    text-decoration: underline;
  }

  /* Section Titles */
  section h2 {
    border-bottom: 3px solid #38ef7d;
    padding-bottom: 6px;
    margin-bottom: 15px;
  }

  /* Footer */
  footer {
    background: #11998e;
    color: white;
    text-align: center;
    padding: 20px 0;
    font-size: 0.95rem;
    margin-top: 50px;
  }

  /* Responsive */
  @media (max-width: 600px) {
    nav {
      flex-wrap: wrap;
    }
    nav a {
      margin: 10px 8px;
      font-size: 1rem;
    }
  }
'''

# Because of curly braces in AdSense push, we escape them by doubling them
adsense_push_script = '<script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>'

# Prepare all page HTML content with proper layout, navigation, AdSense, and content
index_html = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>HealthWisdom AI - Home</title>
  {adsense_script}
  <style>{style_css}</style>
</head>
<body>
  {nav_html}
  <div class=\"container\">
    <h1>Welcome to HealthWisdom AI</h1>
    <p>Your one-stop source for trusted health tips, diet advice, Ayurvedic information, and natural home remedies.</p>
    
    <!-- AdSense Ad Unit -->
    <ins class=\"adsbygoogle\"
         style=\"display:block; text-align:center; margin: 20px auto;\"
         data-ad-layout=\"in-article\"
         data-ad-format=\"fluid\"
         data-ad-client=\"ca-pub-5739867765605477\"
         data-ad-slot=\"1234567890\"></ins>
    {adsense_push_script}

    <p>Explore our sections to learn more about diseases, foods, health tips, and home remedies.</p>
  </div>
  <footer>&copy; 2025 HealthWisdom AI. All rights reserved.</footer>
</body>
</html>"""

# Diseases Page
# (Abbreviated from earlier, expandable with full content later)
diseases_html = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Diseases - HealthWisdom AI</title>
  {adsense_script}
  <style>{style_css}</style>
</head>
<body>
  {nav_html}
  <div class=\"container\">
    <h1>Common Diseases - Tips and Control</h1>
    
    <!-- AdSense Ad Unit -->
    <ins class=\"adsbygoogle\" style=\"display:block; text-align:center; margin: 20px auto;\" data-ad-layout=\"in-article\" data-ad-format=\"fluid\" data-ad-client=\"ca-pub-5739867765605477\" data-ad-slot=\"1234567891\"></ins>
    {adsense_push_script}

    <section>
      <article>
        <h2>Diabetes</h2>
        <p><b>Symptoms:</b> Frequent urination, increased thirst, fatigue.</p>
        <p><b>Control Tips:</b></p>
        <ul>
          <li>Follow a diet low in refined sugars and high in fiber.</li>
          <li>Exercise regularly.</li>
          <li>Monitor blood sugar frequently.</li>
          <li>Consult your healthcare provider.</li>
        </ul>
        <p><b>Recommended Foods:</b> Leafy greens, berries, whole grains.</p>
      </article>

      <article>
        <h2>Hypertension</h2>
        <p><b>Symptoms:</b> Headaches, dizziness.</p>
        <p><b>Control Tips:</b></p>
        <ul>
          <li>Reduce salt intake.</li>
          <li>Eat potassium-rich foods.</li>
          <li>Exercise regularly.</li>
          <li>Limit alcohol and smoking.</li>
        </ul>
        <p><b>Recommended Foods:</b> Fruits, vegetables.</p>
      </article>

      <!-- More diseases can be added here -->
    </section>
  </div>
  <footer>&copy; 2025 HealthWisdom AI. All rights reserved.</footer>
</body>
</html>"""

# Foods Page
foods_html = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Foods - HealthWisdom AI</title>
  {adsense_script}
  <style>{style_css}</style>
</head>
<body>
  {nav_html}
  <div class=\"container\">
    <h1>Foods - Advantages & Disadvantages</h1>
    
    <!-- AdSense Ad Unit -->
    <ins class=\"adsbygoogle\" style=\"display:block; text-align:center; margin: 20px auto;\" data-ad-layout=\"in-article\" data-ad-format=\"fluid\" data-ad-client=\"ca-pub-5739867765605477\" data-ad-slot=\"1234567892\"></ins>
    {adsense_push_script}

    <section>
      <h2>Vegetables</h2>
      <ul>
        <li>Spinach: Rich in iron & vitamins, but high in oxalates which can reduce calcium absorption.</li>
        <li>Broccoli: High in fiber and antioxidants, may cause gas.</li>
        <li>Carrots: Good for eye health, but excessive intake may cause skin discoloration.</li>
      </ul>

      <h2>Fruits</h2>
      <ul>
        <li>Apple: High in fiber but can raise blood sugar quickly in diabetics.</li>
        <li>Banana: Rich in potassium; portion control needed due to sugar content.</li>
        <li>Orange: Rich in vitamin C, may worsen acid reflux in some people.</li>
      </ul>

      <h2>Dry Fruits</h2>
      <ul>
        <li>Almonds: Good for healthy fats but calorie dense.</li>
        <li>Walnuts: Rich in omega-3 but can cause allergies.</li>
        <li>Raisins: High in iron but high sugar content.</li>
      </ul>
    </section>
  </div>
  <footer>&copy; 2025 HealthWisdom AI. All rights reserved.</footer>
</body>
</html>"""

# Tips Page
tips_html = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Health Tips - HealthWisdom AI</title>
  {adsense_script}
  <style>{style_css}</style>
</head>
<body>
  {nav_html}
  <div class=\"container\">
    <h1>Health Tips</h1>
    
    <!-- AdSense Ad Unit -->
    <ins class=\"adsbygoogle\" style=\"display:block; text-align:center; margin: 20px auto;\" data-ad-layout=\"in-article\" data-ad-format=\"fluid\" data-ad-client=\"ca-pub-5739867765605477\" data-ad-slot=\"1234567893\"></ins>
    {adsense_push_script}

    <section>
      <h2>General Health Tips</h2>
      <ul>
        <li>Drink at least 6-8 glasses of water daily.</li>
        <li>Eat a balanced diet with fruits, vegetables, whole grains, and proteins.</li>
        <li>Exercise for at least 30 minutes a day, regularly.</li>
        <li>Aim for 7-9 hours of sleep every night.</li>
        <li>Reduce sugary snacks and processed foods.</li>
        <li>Manage stress through meditation and hobbies.</li>
        <li>Don’t skip yearly health checkups.</li>
        <li>Wash your hands properly and frequently.</li>
        <li>Use sunscreen when outdoors to protect your skin.</li>
        <li>Limit screen time before bedtime for better sleep quality.</li>
      </ul>
    </section>
  </div>
  <footer>&copy; 2025 HealthWisdom AI. All rights reserved.</footer>
</body>
</html>"""

# About Page
about_html = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>About Us - HealthWisdom AI</title>
  {adsense_script}
  <style>{style_css}</style>
</head>
<body>
  {nav_html}
  <div class=\"container\">
    <h1>About HealthWisdom AI</h1>
    <p>HealthWisdom AI combines trusted scientific knowledge and the power of artificial intelligence to provide personalized, actionable healthcare advice. Our mission is to make complex medical information simple and useful for everyone.</p>
    <p>We provide well-researched disease control tips, balanced nutritional guidance, Ayurvedic knowledge, and natural home remedies to help you live a healthier life.</p>
    <p><b>Disclaimer:</b> This site is for informational purposes only and is not a substitute for professional medical advice.</p>
  </div>
  <footer>&copy; 2025 HealthWisdom AI. All rights reserved.</footer>
</body>
</html>"""

# Contact Page
contact_html = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Contact Us - HealthWisdom AI</title>
  {adsense_script}
  <style>{style_css}</style>
</head>
<body>
  {nav_html}
  <div class=\"container\">
    <h1>Contact Us</h1>
    <p>If you have questions, suggestions, or need advice, please reach out using the form below.</p>
    <form>
      <label for=\"name\">Name:</label><br>
      <input type=\"text\" id=\"name\" name=\"name\" required style=\"width: 100%; padding: 10px; margin-bottom: 12px; border-radius: 6px; border: 1px solid #ccc;\"><br>
      <label for=\"email\">Email:</label><br>
      <input type=\"email\" id=\"email\" name=\"email\" required style=\"width: 100%; padding: 10px; margin-bottom: 12px; border-radius: 6px; border: 1px solid #ccc;\"><br>
      <label for=\"message\">Message:</label><br>
      <textarea id=\"message\" name=\"message\" rows=\"6\" required style=\"width: 100%; padding: 10px; margin-bottom: 12px; border-radius: 6px; border: 1px solid #ccc;\"></textarea><br>
      <button type=\"submit\" style=\"background: #38ef7d; color: white; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 1.1rem;\">Send Message</button>
    </form>
  </div>
  <footer>&copy; 2025 HealthWisdom AI. All rights reserved.</footer>
</body>
</html>"""

# Write all files
files_content = {
    "index.html": index_html,
    "diseases.html": diseases_html,
    "foods.html": foods_html,
    "tips.html": tips_html,
    "about.html": about_html,
    "contact.html": contact_html
}

for fname, fcontent in files_content.items():
    with open(os.path.join(dir_name, fname), 'w', encoding='utf-8') as file:
        file.write(fcontent)

# Create zip archive
zip_filename = "healthwisdom_full_website.zip"
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            zipf.write(os.path.join(root, file), arcname=file)

zip_filename
