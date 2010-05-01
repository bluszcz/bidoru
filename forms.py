from web import form

form_add_tag = form.Form(
    form.Textbox("tag",
        form.notnull,
        form.regexp('\w+', 'Must be alphanumeric'),
        form.Validator('Must be longer than 2', lambda x:int(x)>2)))

