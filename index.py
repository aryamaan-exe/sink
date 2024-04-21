from flask import Flask, request, render_template

app = Flask(__name__)
users = {}

@app.route('/')
def index():
    return "hi"
@app.route('/submit', methods=['POST'])
def submit():
    global clipboard
    if request.method == 'POST':
        text = request.form['text']
        clipboard = text
        password = request.form['password']
        if password == "$":
            return f'Text received: {text}'
        else:
            return 'Unauthorized: Incorrect password'
    else:
        return 'Invalid request method'
    
@app.route('/get', methods=['GET'])
def get():
    if request.method == 'GET':
        return clipboard

def handler(event, context):
    return app(event, context)
