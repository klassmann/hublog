

import datetime
try:
    from app.parser import parse_markdown
except:
    from parser import parse_markdown

class BlogPost(object):
    def __init__(self, name, content):
        parsed, meta = parse_markdown(content)
        self.name = name
        self.title = meta['title'][0]
        self.subtitle = meta['subtitle'][0]
        self.published = meta['published_at'][0]
        self.published_date = self.__try_parse_date(self.published)
        self.author = meta['author'][0]
        self.thumb = meta['thumb'][0]
        self.tags = meta['tags'][0]
        self.content = parsed

    def __try_parse_date(self, s):
        try:
            return datetime.datetime.strptime(s, '%Y-%m-%d')
        except:
            pass    # Silent Error
        return datetime.datetime.now()

