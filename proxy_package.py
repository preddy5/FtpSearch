
import urllib2

class ProxyPackage(object):
    """
        This class is used for installing python packages or to use urllib or urllib2 under proxy server
        create a instance of this class and urlopen will show no error
    """
    def __init__(self,kind='http',name='',password='',proxy='',port=''):
        if name=='':
            auth = '%s://%s:%s' % (kind, proxy , port)
        else:
            auth = '%s://%s:%s@%s:%s' % (kind,name , password , proxy , port)
        self.handler = urllib2.ProxyHandler({kind: auth})
        self.opener = urllib2.build_opener(self.handler)
        urllib2.install_opener(self.opener)
     
