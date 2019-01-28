
import sys
import glob
import os

from app.post import BlogPost

try:
    from github import Github
except:
    print("error on loading github: try to install PyGithub library", file=sys.stderr)

class BaseRepositoryManager(object):
    def __init__(self):
        self.posts = {}

    def format_name(self, s):
        return s.split('.')[0]
    
    def load_posts(self):
        pass

    def load(self):
        _posts = self.load_posts()
        self.posts = { p.name : p for p in _posts}

    def get_post(self, name):
        return self.posts[name]

    def get_posts(self):
        posts = self.posts.values()
        posts = sorted(posts, key=lambda p: p.published_date, reverse=True)
        return posts


class GithubRepositoryManager(BaseRepositoryManager):
    def __init__(self, accesskey, repository):
        super().__init__()
        self.client = Github(self.accesskey)
        self.repository = self.client.get_repo(repository)

    def __get_contents(self):
        if self.client:
            return self.repository.get_dir_contents('published')
        return None

    def load_posts(self):
        posts = []
        published = self.__get_contents()

        def _decoded(c):
            return c.decoded_content.decode()
        
        posts = [BlogPost(self.format_name(p.name), _decoded(p)) for p in published]
        
        return posts

class LocalRepositoryManager(BaseRepositoryManager):
    def __init__(self, directory, markdown_ext):
        super().__init__()
        self.directory = directory
        self.markdown_ext = markdown_ext

    def load_posts(self):
        posts = []
        local_path = os.path.join(self.directory, '*' + self.markdown_ext)
        names = glob.glob(local_path)

        for filename in names:
            with open(filename) as f:
                content = f.read()
                name = os.path.basename(filename)
                posts.append(BlogPost(self.format_name(name), content))
        return posts


def get_repository_manager(settings):
    if settings.LOCAL:
        print('Hublog: Running Local')
        return LocalRepositoryManager(settings.BLOG_POSTS_DIR, settings.MARKDOWN_EXT)
    return GithubRepositoryManager(settings.GITHUB_ACCESSKEY, settings.GITHUB_REPOSITORY)