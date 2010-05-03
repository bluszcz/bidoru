import web
from google.appengine.api import users
from google.appengine.ext import db
from django.utils import simplejson
from web import form

from models import Tag, Note
from forms import form_add_tag, form_add_note

urls = (
    '/ajax/tags/get/', 'get_tags',
    '/ajax/tags/add/', 'add_tag',
    '/ajax/notes/add/', 'add_note',
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
        form = form_add_tag()
        object = {}
        if form.validates():
            object['success'] = True
            object['response'] = form.d.tag
            tag = Tag(author=user,  name=form.d.tag)
            tag.put()
            object['message'] = 'New tag has been created'
        else:
            object['success'] = False
            object['errors'] = form.get_errors()
            object['message'] = 'Tag has not been created'
        return simplejson.dumps(object)

class add_note:
    def POST(self):
        user = users.get_current_user()
        form = form_add_note()
        object = {}
        if form.validates():
            object['success'] = True
            object['response'] = form.d.note
            note = Note(author=user,  name=form.d.note,
                        tags=form.d.ntag_list.split(','))

            note.put()
            object['message'] = 'New note has been created'
        else:
            object['success'] = False
            object['errors'] = form.get_errors()
            object['message'] = 'Note has not been created'
        return simplejson.dumps(object)



app = web.application(urls, globals())
main = app.cgirun()

