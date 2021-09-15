import unittest
import sys
sys.path.append('./app')
from models import Source

class TestSource(unittest.TestCase):
    '''
    test case to test the behaviour of the source model
    '''
    def setUp(self):
        self.new_source = Source('engadget','Engadget','Tesla now accepts Bitcoin in the US','https://www.engadget.com/sonys-flavor-graph-uses-ai-to-predict-how-ingredients-will-pair-together-092935932.html','AI has gone into games, self-driving and other areas with mixed success, and now its trying its hand at cooking. After Googles AI went up against a Great British Bake Off winner, Sony has developed','English','UK')

    def test_isSourceINstance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
	unittest.main()