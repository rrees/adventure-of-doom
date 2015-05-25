from google.appengine.ext import ndb

class Adventure(ndb.Model):
    name = ndb.StringProperty(required=True)

class Entry(ndb.Model):
    number = ndb.IntegerProperty(required=True)
    text = ndb.TextProperty(required=True)

class Option(ndb.Model):
    entry = ndb.KeyProperty(required=True, kind=Entry)
    text = ndb.StringProperty(required=True)
