
import unittest

from post import BlogPost

SAMPLE_POST = """Title: Lorem Ipsum Dolor
SubTitle: Small Example of a Blog Post
author: Author Name
published_at: 2017-10-11
thumb: www.thumbnail.com/image.png
tags: blogging web flask python github

## Si sum

Lorem markdownum nec sub ipso me vendit opposuitque Narve coniugis animisque
Achilles umbra modo vestibus: fortis, unda. Exiguam adest custos et atque
liquebat corpus addenda de populus."""

class TestBlogPost(unittest.TestCase):
    
    def setUp(self):
        self.post = BlogPost('blog_post_test', SAMPLE_POST)

    def test_sample_post_name(self):
        self.assertEqual(self.post.name, 'blog_post_test')
    
    def test_sample_post_markdown_metadata(self):
        self.assertEqual(self.post.published, '2017-10-11')
        self.assertEqual(self.post.title, 'Lorem Ipsum Dolor')
        self.assertEqual(self.post.subtitle, 'Small Example of a Blog Post')
        self.assertEqual(self.post.thumb, 'www.thumbnail.com/image.png')
        self.assertEqual(self.post.tags, 'blogging web flask python github')

        
if __name__ == '__main__':
    unittest.main()
