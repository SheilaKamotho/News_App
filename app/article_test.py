import unittest
from models import article
Article = article.Article

class TestArticle (unittest.TestCase):
    '''
    Test class behavior for the Article class
    '''
    
    def setUp(self):
        '''
         Set up method that will run before every Test
        '''

        self.new_article = Article("John Biggs","Crypto Traders Cut Out the Middleman, Simply Rob Victim", "Two alleged crypto traders in Singapore apparently came up with a fool-proof plan: rather than convert a customer’s 365,000 Singapore dollars to bitcoin, they would simply rob the victim when he came in to do the trade.Read more...","https://gizmodo.com/crypto-traders-cut-out-the-middleman-simply-rob-victim-1845011301","https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/li0fkkejdmaugm8v1fkw.jpg","2020-09-08T06:02:00Z")
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_article.author,"John Biggs")
        self.assertEqual(self.new_article.title,"Crypto Traders Cut Out the Middleman, Simply Rob Victim")
        self.assertEqual(self.new_article.description,"Two alleged crypto traders in Singapore apparently came up with a fool-proof plan: rather than convert a customer’s 365,000 Singapore dollars to bitcoin, they would simply rob the victim when he came in to do the trade.Read more...")
        self.assertEqual(self.new_article.url,"https://gizmodo.com/crypto-traders-cut-out-the-middleman-simply-rob-victim-1845011301")
        self.assertEqual(self.new_article.url_to_image,"https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/li0fkkejdmaugm8v1fkw.jpg")  
        self.assertEqual(self.new_article.published_at,"2020-09-08T06:02:00Z")


    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

if __name__ == '__main__':
    unittest.main()