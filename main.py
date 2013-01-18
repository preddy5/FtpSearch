import urllib2
from FtpSearch.exceptions import *
from FtpSearch.search import *
from FtpSearch.proxy_package import *
      
class FtpRepo(Page):
    """
        This class is used to search repo for the keyword
        
    """
    def __init__(self,url):
        self.url = url
        super(FtpRepo,self).__init__(url)

    def searchRepo(self,keyword, depth, strict_search=False):
        try:
                self.search(keyword, strict_search) 
                #print self.page_info
                leng = self.page_info[0].split().__len__()-1
        except:
                return
        for i in self.page_info:
                if depth-1 == 0:
                    break
                l = i.split()
                if not '.' in l[-1]:
                    FtpRepo(self.url+'/'+"%20".join(l[leng:])+'/').searchRepo(keyword,depth-1,strict_search)
    

class SetProxy(ProxyPackage):
    """
        This class is used to set proxy for searching the repo
    """

    def __init__(self,kind='http',name='',password='',proxy='',port=''):
        super(SetProxy,self).__init__(kind,name,password,proxy,port)


