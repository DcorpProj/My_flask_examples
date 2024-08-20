from flask import Flask #pip install flask

app = Flask(__name__)

@app.route('/')
def index() -> str:
    return '''<title>Hello button (Flask)</title>
    <p1>Hi button</p1>
    <br>
    <button type=submit>Hi!</button>
    <button>A button.</button>
    '''

if __name__ == '__main__':
    app.run(debug=True)
