from google.appengine.ext import db

class Company(db.Model):
    companyAbvName = db.StringProperty()
    idt = db.IntegerProperty()
    code = db.StringProperty()
    name = db.StringProperty()
    companyName = db.StringProperty()

    def __str__(self):
        return "<Company code: %s, idt: %s, name: %s>" % (repr(self.code), repr(self.idt), repr(self.name))
        
