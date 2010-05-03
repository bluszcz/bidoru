from google.appengine.ext import db



class Tag(db.Model):
    author = db.UserProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    name = db.StringProperty()

class Note(db.Model):
    author = db.UserProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    name = db.StringProperty()
    tags = db.StringListProperty()
