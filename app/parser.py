
try:
    import pygments
except:
    pass

try:
    from markdown import Markdown
    from markdown.extensions.toc import TocExtension
    from markdown.extensions.codehilite import CodeHiliteExtension
except:
    print("error on loading markdown: try to install Markdown library", file=sys.stderr)


def parse_markdown(content):
    """
    Small helper for parsing markdown files.
    """
    html = ''
    default_meta = {
        'title': ['',],
        'subtitle': ['',],
        'author': ['',],
        'tags': ['',],
        'published_at': ['',],
        'thumb': ['',]
    }
    meta = default_meta
    try:
        md = Markdown(extensions=[
            'markdown.extensions.meta',
            CodeHiliteExtension(linenums=False), 
            'markdown.extensions.fenced_code', 
            'markdown.extensions.admonition', 
            TocExtension(baselevel=2)
        ])
        html = md.convert(content)
        meta = md.Meta
    except:
        meta = default_meta
    return html, meta
