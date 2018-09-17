"""
Main script of our blog.
"""

import os
import pprint
import datetime
import sys
import glob
import base64

from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from flask import jsonify
from flask import session
from flask import make_response

from github import Github

try:
    from app import settings
except:
    import settings

from hublog import parse_markdown

app = Flask(__name__)
app.secret_key = settings.SECRET
running_local = settings.LOCAL

g = None
if not running_local:
    g = Github(settings.GITHUB_ACCESSKEY)

class BlogPost(object):
    def __init__(self, name, content):
        parsed, meta = parse_markdown(content)
        self.name = name
        self.published = None
        self.title = meta['title'][0]
        self.subtitle = meta['subtitle'][0]
        self.published = meta['published_at'][0]
        self.published_date = self.__try_parse_date(self.published)
        self.author = meta['author'][0]
        self.content = parsed

    def __try_parse_date(self, s):
        try:
            return datetime.datetime.strptime(s, '%Y-%m-%d')
        except:
            pass    # Silent Error
        return datetime.datetime.now()

class BlogPostsManager(object):
    def __init__(self):
        self.posts = {}
        if g:
            self.repo = g.get_repo(settings.GITHUB_REPOSITORY)

    def __name(self, s):
        return s.split('.')[0]

    def get_github_contents(self):
        if g:
            return self.repo.get_dir_contents('published')

    def get_github_posts(self):
        published = self.get_github_contents()
        posts = []
    
        def _decoded(c):
            return c.decoded_content.decode()
        
        posts = [BlogPost(self.__name(p.name), _decoded(p)) for p in published]
        
        return posts

    def get_local_posts(self):
        local_path = os.path.join(settings.BLOG_POSTS_DIR, '*' + settings.MARKDOWN_EXT)
        print(local_path)
        names = glob.glob(local_path)
        print(names)
        posts = []

        for filename in names:
            with open(filename) as f:
                content = f.read()
                name = os.path.basename(filename)
                posts.append(BlogPost(self.__name(name), content))
        return posts
    
    def load_posts(self):
        posts = []

        if running_local:
            posts = self.get_local_posts()
        else:
            posts = self.get_github_posts()
        
        self.posts = { p.name : p for p in posts}

    def get_post(self, name):
        return self.posts[name]

    def get_posts(self):
        posts = self.posts.values()
        posts = sorted(posts, key=lambda p: p.published_date, reverse=True)
        return posts

blog_manager = BlogPostsManager()
blog_manager.load_posts()

@app.route('/')
def blog():
    if running_local:
        blog_manager.load_posts()

    posts = blog_manager.get_posts()
    return render_template("index.html", posts=posts, local=running_local)

@app.route('/<string:slug>/')
def blog_post(slug):
    if running_local:
        blog_manager.load_posts()

    post = blog_manager.get_post(slug)
    return render_template("post.html", post=post, local=running_local)

