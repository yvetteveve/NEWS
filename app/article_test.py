import unittest
from models import article
Article=article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Article class
    '''
    def setUp(self):
        '''
        set up method that will run before every Test
        '''
        self.new_article=Article("one","Nicole","WSJ Wealth Adviser Briefing","Brief price gaps","http://m.wsj.net/video/","hey there i love","yah you do","ofcourse")

    def test_article(self):
        self.assertTrue(isinstance(self.new_article,Article))

if __name__ == '__main__':
    unittest.main()