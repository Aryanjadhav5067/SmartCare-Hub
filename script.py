python_code = '''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diseases')
def diseases():
    return render_template('diseases.html')

@app.route('/foods')
def foods():
    return render_template('foods.html')

@app.route('/tips')
def tips():
    return render_template('tips.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
'''

file_name = "scripy.py"
with open(file_name, "w", encoding="utf-8") as f:
    f.write(python_code)

file_name