import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    comments = db.relationship('Comment', backref='note', lazy=True)

    def __repr__(self):
        return f'<Note {self.id}: {self.title} by {self.user_id}>'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    note_id = db.Column(db.Integer, db.ForeignKey('note.id'), nullable=False)

    def __repr__(self):
        return f'<Comment {self.id} on Note {self.note_id} by User {self.user_id}>'


@app.route('/')
def hello_world():
    return 'Scribe online.'


if __name__ == '__main__':
    app.run()