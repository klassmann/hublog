"""
Settings
You must change this configurations for work 
propertly with your Github Account.
"""

import os

# Is it running locally?
LOCAL = False

try:
    # We get the information from script run-local
    LOCAL = os.getenv('LOCAL')
except:
    pass

# https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/
GITHUB_ACCESSKEY = ''

# yourname/blog_repo
GITHUB_REPOSITORY = ''

# Path for local posts in markdown
BLOG_POSTS_DIR = os.path.realpath(os.getenv('HUBLOG_LOCAL_REPOSITORY'))

# The extension used by markdown files, you can change to .markdown
MARKDOWN_EXT = '.md'

"""
An important key for Flask
You can generate a new one doing this in the terminal:
>>> python -c "import os; print(os.urandom(16).hex())"
Paste the result inside the ''
"""
SECRET = '' 