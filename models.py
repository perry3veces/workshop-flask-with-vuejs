# -*- coding: utf-8 -*-
# Librarys
import os
from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__)

# Settings
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Variables
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class User(db.Model):
    '''
    Table user
    '''

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    mail = db.Column(db.String(200))
    password = db.Column(db.String(106))
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<User Table {0}>'.format(self.username)


class News(db.Model):
    '''
    Table News
    '''
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    link = db.Column(db.String(500))
    user_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    # Relations
    user = db.relationship(
        'User', backref=db.backref('News', lazy=True))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
           'id': self.id,
           'title': self.title,
           'link': self.link,
           'user_id': self.user_id
        }

    def __repr__(self):
        return '<News Table {0}>'.format(self.title)


class Comment(db.Model):
    '''
    Table Comment
    '''
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))
    news_id = db.Column(
        db.Integer, db.ForeignKey('news.id'), nullable=False)
    user_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    # Relations
    user = db.relationship(
        'User', backref=db.backref('Comment', lazy=True))
    news = db.relationship(
        'News', backref=db.backref('Comment', lazy=True))

    def __repr__(self):
        return '<Comment Table {0}>'.format(self.id)


if __name__ == "__main__":
    manager.run()
