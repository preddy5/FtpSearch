
class FtpSearch(Exception):
    """Base class for exceptions raised by Ftpsearch"""


class UrlNotFound(FtpSearch):
    """Exception for url not found"""
    def __init__(self,message):
        super(UrlNotFound,self).__init__(message)

class NoProtocol(FtpSearch):
    def __init__(self):
        super(NoProtocol,self).__init__('Wrong Protocol or No Protocol')
