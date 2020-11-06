import uweb as uweb3
from uweb import model
import random
import os

__author__ = 'iemand <iets@iets.iets>'
__version__ = '0.1'


class Message(model.Record):

  """Abstraction class for messages stored in the database."""

"""Begin project."""

class BeginProject(uweb3.DebuggingPageMaker):
  """Begin project."""

  def __init__(self, *args, **kwds):
    """Overwrites the default init."""
    super(BeginProject, self).__init__(*args, **kwds)

  def Img(self, action=None):
   """Image page"""
   pathlist = []
   if self.post.getfirst('search'):
     search = self.post.getfirst('search')
     savedSearch = Message.Create(self.connection, {'ID': search })

   else:
     search = None
     list = None
   return self.parser.Parse('img.html', search=search, pathlist=pathlist)

  def Index(self, action=None):
    """Returns the homepage."""
    test = self.get.getfirst('user')
    # raise
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

PACKAGE = 'BeginProject'
PAGE_CLASS = BeginProject
CONFIG = '/var/www/beginproject/beginproject.conf'
ROUTES = [('/', 'Index'),
	  ('/teun', 'Teun'),
          ('/img', 'Img'),
          ('(/img/.*)', 'Static'),
          ('(/styles/.*)', 'Static'),
          ('.*', 'NotFound')]

uweb3.ServerSetup(apache_logging=False)
