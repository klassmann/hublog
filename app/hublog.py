import pygments
from markdown import Markdown
from markdown.extensions.toc import TocExtension


def parse_markdown(content):
    """
    Small helper for parsing markdown files.
    """
    html = ''
    default_meta = {
        'title': [''],
        'subtitle': [''],
        'author': [''],
        'tags': [''],
        'published_at': ['']
    }
    meta = default_meta
    try:
        md = Markdown(extensions=[
            'meta', 
            'codehilite(linenums=False)', 
            'fenced_code', 
            'admonition', 
            TocExtension(baselevel=2)
        ])
        html = md.convert(content)
        meta = md.Meta
    except:
        meta = default_meta
    return html, meta