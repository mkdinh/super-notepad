from flask import Flask, render_template

notepad = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='Mike')


if __name__ == '__main__':
    notepad.run(debug=True)