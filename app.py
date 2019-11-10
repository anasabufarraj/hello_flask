#!./venv/bin/python3.7
# © Anas Abu Farraj
"""Learning Flask"""

from flask import Flask, render_template

APP = Flask(__name__)
POSTS = {
    1: {
        'title': 'Alpha',
        'content': 'This is a post'
    },
    2: {
        'title': 'Beta',
        'content': 'This is a post'
    }
}


@APP.route('/')
def home():
    """Returns home page."""
    return 'Hello, Flask!'


@APP.route('/posts/<int:post_id>')
def posts(post_id):
    """Returns posts pages if found, otherwise returns 404 page."""
    post = POSTS.get(post_id)  # Returns None if key value is not found.
    if not post:
        return render_template('404.jinja2', message='Oops! Page not found', id=post_id)
    return render_template('posts.jinja2', post=post)


if __name__ == '__main__':
    APP.run()
