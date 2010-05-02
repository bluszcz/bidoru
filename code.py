import web
from google.appengine.api import users
from google.appengine.ext import db
from models import Tag
from forms import form_add_tag
from django.utils import simplejson

urls = (
    '/', 'index',
    )

render = web.template.render('templates')

class index:
    def GET(self):
        user = users.get_current_user()
        if user:
            greeting = ("Welcome, %s! (<a href=\"%s\">sign out</a>)" % (user.nickname(), users.create_logout_url("/")))
            query = Tag.all()
            query.filter('author=',user)
            results = query.fetch(10)
            query = Tag.all()
            query.filter('author',user)
            r = query.run()
            tags = c = [ c.name for c in r ]
            return render.dashboard(greeting,tags, form_add_tag)
        else:
            greeting = ("<a href=\"%s\">Sign in or register</a>." % users.create_login_url("/"))

        return render.index(greeting)

app = web.application(urls, globals())
main = app.cgirun()
