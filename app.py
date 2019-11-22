#!/usr/bin/env python
# ------------------------------------------------------------------------------
#  Copyright (c) 2019. Anas Abu Farraj.
# ------------------------------------------------------------------------------
"""Learning Flask"""

from flask import Flask, render_template, request, url_for, redirect

APP = Flask(__name__)
POSTS = {
    0: {
        'post_id': 0,
        'title': 'Alpha',
        'content': 'This is a post'
    },
    1: {
        'post_id': 1,
        'title': 'Beta',
        'content': 'This is a post'
    }
}


@APP.route('/')
def index():
    """Returns index page."""
    return render_template('index.html', POSTS=POSTS)


@APP.route('/post/<int:post_id>')
def posts(post_id):
    """Returns posts pages if found, otherwise returns 404 page."""
    post = POSTS.get(post_id)  # Returns None if key value is not found.
    if not post:
        return render_template('404.html', message='Oops! Page not found')

    return render_template('posts.html', post=post)


@APP.route('/post/create', methods=['GET', 'POST'])
def submit():
    """Returns and Submit form data as 'POST' request, and add to database."""
    if request.method == 'POST':
        post_id = len(POSTS)
        title = request.form.get('title')
        content = request.form.get('content')
        POSTS[post_id] = {'post_id': post_id, 'title': title, 'content': content}

        return redirect(url_for('posts', post_id=post_id))

    return render_template('form.html')


if __name__ == '__main__':
    APP.run()
