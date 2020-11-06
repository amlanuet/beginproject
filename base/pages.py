import uweb3
from uweb3 import model
import random
import os

__author__ = 'iemand <iets@iets.iets>'
__version__ = '0.1'


class Message(model.Record):

  """Abstraction class for messages stored in the database."""

"""Begin project."""

class PageMaker(uweb3.DebuggingPageMaker):
  """Begin project."""

  def __init__(self, *args, **kwds):
    """Overwrites the default init."""
    super(PageMaker, self).__init__(*args, **kwds)
    self.post = uweb3.request.QueryArgsDict(self.post)

  def Img(self, action=None):
   """img page"""
   if self.post.getfirst('search'):
     search = self.post.getfirst('search')
     Message.Create(self.connection, {'message' : search })
   else:
     search = ()
   return self.parser.Parse('img.html', search=search)

  def History(self, action=None):
   """History Page"""
   history = []
   for message in Message.List(self.connection):
     history.append(message)
   return self.parser.Parse('history.html', history=history,)



  def Index(self, action=None):
    """Returns the homepage."""
    if self.post.getfirst('user'):
      name=self.post.getfirst('user')
    else:
      name='Teun'
    coin=random.randint(0,1)
    return self.parser.Parse('index.html', name=name, coin=coin)


  def Teun(self, action=None):
    """Returns the teun page."""
    hobbies = ('drummen', 'keihard rennen', 'ijs eten')
    return self.parser.Parse('index.html', hobbies=hobbies)

  def NotFound(self):
    """Returns a 404 page."""
    return uweb3.Response('Document not found', httpcode=404)

    """ def main(): """
    """  return uweb3.uWeb(BeginProject, [('/', 'Index'), ('.*', 'Not Found')], os.path.dirname(__file__))"""

''' PACKAGE = 'BeginProject'
PAGE_CLASS = BeginProject
CONFIG = '/var/www/beginproject/beginproject.conf'
ROUTES = [('/', 'Index'),
	  ('/teun', 'Teun'),
          ('/img', 'Img'),
          ('/history', 'History'),
          ('(/img/.*)', 'Static'),
          ('(/styles/.*)', 'Static'),
          ('.*', 'NotFound')]

uweb3.ServerSetup(apache_logging=False) '''
