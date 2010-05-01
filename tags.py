import web
from google.appengine.api import users
from google.appengine.ext import db
from django.utils import simplejson
from web import form

from models import Tag
from forms import form_add_tag

urls = (
    '/ajax/tags/get/', 'get_tags',
    '/ajax/tags/add/', 'add_tag',
    )

render = web.template.render('templates')


class get_tags:
    def GET(self):
        user = users.get_current_user()
        tags = db.GqlQuery("SELECT * FROM Tag WHERE user = :1 ORDER BY date", user)
        object = {}
        object['tags'] = []
        for tag in tags:
            object['tags'].append(tag.name)
        return simplejson.dumps(object)

class add_tag:
    def POST(self):
        user = users.get_current_user()
        object = {}
        return simplejson.dumps(object)
        #tag = Tag(user=user, name=tag_name)

app = web.application(urls, globals())
main = app.cgirun()

