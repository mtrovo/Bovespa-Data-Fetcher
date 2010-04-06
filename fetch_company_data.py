from urllib import urlopen
import re
from django.utils import simplejson
from models import Company
from google.appengine.ext import db

IDT_LIST_URL = 'http://cotacoes.economia.uol.com.br/ws/asset/stock/list?size=10000'

def geturl(url):
    print 'looking url ' + (url)
    content = urlopen(url).read()
    print 'load successful'
    return content

def main():
    idtstr = geturl(IDT_LIST_URL)
    idtjson = simplejson.loads(idtstr)
    for comp in idtjson['data']:
        old = Company.get_by_key_name(comp['code'])

        if old:
          print "Company %s already exists" % old.code
        else:
          c = Company(key_name=comp['code'])
          for att in comp:
            c.__setattr__(att, comp[att])
          c.put()
          print str(c)
        
if (__name__=='__main__'):
    main()
 
