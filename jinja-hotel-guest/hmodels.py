from google.appengine.ext import ndb

class Message(ndb.Model):
    text = ndb.StringProperty()
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)