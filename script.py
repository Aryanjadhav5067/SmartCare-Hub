req_txt_content = """flask
flask-cors
openai
gunicorn
"""

file_name = "requirements.txt"
with open(file_name, "w", encoding="utf-8") as f:
    f.write(req_txt_content)

file_name