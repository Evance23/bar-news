class Source:
    '''
    Defining the news Source objects
    '''

    def __init__(self,id, name, description, url, category, language, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


#author, title, description, url, date
class Article:
    '''
    Defining the news article objects
    '''

    def __init__(self ,author, title, description, url, date, image):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.date = date
        self.image = image