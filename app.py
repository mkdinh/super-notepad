from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ

notepad = Flask(__name__)
notepad.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL') or 'sqlite:///notepad.sqlite'
db = SQLAlchemy(notepad)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)

@notepad.route('/')
def index():
    return render_template('index.html', name='Mike')


@notepad.route('/tasks')
def tasks():
    tasks = db.session.query(Task)
    data = []
    for task in tasks:
        item = {
            "id": task.id,
            "description": task.description
        }
        data.append(item)

    return jsonify(data)


if __name__ == '__main__':
    notepad.run(debug=True)