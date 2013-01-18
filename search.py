
import urllib2
from FtpSearch.exceptions import*

protocols = 'ftp://'

class OpenUrl(object):
    
    """
        This class opens a url after checking the protocol and has a class
        attribute which is urlopen instance of the passed url
    """

    def __init__(self,url):
        if(not url[0:6]== protocols):
            raise NoProtocol()
        self.url = url
        try:
            self.instance =urllib2.urlopen(self.url)
        except: 
            return
    def instance():
        return self.instance


class Page(OpenUrl):

    """
        This class instance prints the occurence of the keyword in url given
    """
    
    def __init__(self,url):
        super(Page,self).__init__(url)

    def search(self,keyword, strict_search=False):
        self.page_info = self.instance.readlines()
        if not strict_search:
            keyword = keyword.lower()
        self._search(keyword,strict_search)

    def _search(self,keyword,strict_search):
       for i in self.page_info:
            l = i.split()
            for j in l:
                if not strict_search:
                    j = j.lower()
                if keyword in j:
                    print self.url,' ',j

