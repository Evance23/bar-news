import unittest
import sys
sys.path.append('./app')
from models import Article

class TestArticle(unittest.TestCase):
    '''
    Test case to test the behaviour of the article model
    '''
    def setUp(self):
        '''
        function that runs before each test is executed
        '''
        self.new_article = Article("Alex Alex","Live Updates: 1 dead, 2 wounded in shooting at grocery store on New York's Long Island ","CBS News A grocery store employee was killed in a shooting at a Stop & Shop on New York's Long Island Tuesday morning, police said.""https://www.cbsnews.com/live-updates/stop-and-shop-shooting-west-hempstead-new-york/","A grocery store employee was killed and two others were wounded in a shooting at a Stop &amp; Shop on New York's Long Island Tuesday morning, police said. The two people injured were being treated","https://cbsnews1.cbsistatic.com/hub/i/r/2021/04/20/4223ae71-066d-4a7c-a4ea-56560e2819e2/thumbnail/1200x630/eedfe869bada6a25d5ed9da46eb8b70a/stop-and-shop-shooting-2021-04-20t174314z.jpg","2021-04-20T18:32:53Z")
    def test_isArticleInstance(self):
        self.assert_(isinstance(self.new_article,Article))
        
if __name__ == '__main__':
	unittest.main()