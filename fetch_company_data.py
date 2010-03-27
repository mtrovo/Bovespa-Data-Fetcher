from urllib import urlopen
import re
from django.utils import simplejson
from models import Company

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
        c = Company()
        for att in comp:
            c.__setattr__(att, comp[att])
        comp.put()
        
if (__name__=='__main__'):
    main()
 
