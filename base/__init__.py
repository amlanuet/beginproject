"""A uweb3 test."""
import os
# Third-party modules
import uweb3

# Application
from . import pages

def main():
   return uweb3.uWeb(pages.PageMaker,
   [('/', 'Index'),
    ('/teun', 'Teun'),
    ('/img', 'Img'),
    ('/history', 'History'),
    ('(/img/.*)', 'Static'),
    ('(/styles/.*)', 'Static'),
    ('.*', 'NotFound')],
   os.path.dirname(__file__)
   )
