from web import form

class BForm(form.Form):
    def get_errors(self):
        errors = {}
        for i in self.inputs:
            if i.note:
                errors[i.name] = i.note
        return errors

form_add_tag = BForm(form.Textbox("tag",
        form.notnull,
        form.regexp('\w+', 'Must be alphanumeric'),
        form.Validator('Must be longer than 2', lambda x:len(x)>2),
        class_="ui-state-default"))
