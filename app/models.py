class Article:
    '''
    Article class to define Article objects
    '''
    
    def __init__(self,author,title,description,url,url_to_image,published_at):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.url_to_image = url_to_image
        self.published_at = published_at

class Source:
    '''
    Source class to define source objects
    '''
    
    def __init__(self,name,url,description):
        self.name = name
        self.url = url
        self.description = description



