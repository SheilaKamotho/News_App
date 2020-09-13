import unittest
from models import source
Source = source.Source

class TestArticle (unittest.TestCase):
    '''
    Test class behavior for the Source class
    '''
    
    def setUp(self):
        '''
         Set up method that will run before every Test
        '''

        self.new_source = Source("ABC News","https://abcnews.go.com/","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.")
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_source.name,"ABC News")
        self.assertEqual(self.new_source.url,"https://abcnews.go.com/")
        self.assertEqual(self.new_source.description,"Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
    unittest.main()