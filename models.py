from google.appengine.ext import db

class Tag(db.Model):
    author = db.UserProperty()
    name = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)

