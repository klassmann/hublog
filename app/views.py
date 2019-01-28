"""
Main script of our blog.
"""

import os
import pprint
import datetime
import sys
import glob
import base64

try:
    from flask import Flask
    from flask import render_template, request, redirect, url_for, flash
    from flask import jsonify
    from flask import session
    from flask import make_response
    from flask import current_app
    from flask import g
except:
    print("error on loading flask: try to install Flask library", file=sys.stderr)


def blog():
    if current_app.running_local:
        current_app.manager.load()
    posts = current_app.manager.get_posts()
    return render_template("index.html", posts=posts, local=current_app.running_local)

def blog_post(slug):
    if current_app.running_local:
        current_app.manager.load()
    post = current_app.manager.get_post(slug)
    return render_template("post.html", post=post, local=current_app.running_local)

