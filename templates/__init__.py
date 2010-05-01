from web.template import CompiledTemplate, ForLoop


def dashboard():
    loop = ForLoop()
    _dummy  = CompiledTemplate(lambda: None, "dummy")
    join_ = _dummy._join
    escape_ = _dummy._escape

    def __template__ (username,tags,form_add_tag):
        yield '', join_('<html>\n')
        yield '', join_('        <head>\n')
        yield '', join_('                <link type="text/css" href="/statics/css/smoothness/jquery-ui-1.8.1.custom.css" rel="stylesheet" />\n')
        yield '', join_('                <script type="text/javascript" src="/statics/js/jquery-1.4.2.min.js"></script>\n')
        yield '', join_('                <script type="text/javascript" src="/statics/js/jqui/js/jquery-ui-1.8.custom.min.js"></script>\n')
        yield '', join_('                <script type="text/javascript" src="/statics/js/jqui/js/jquery.form.js"></script>\n')
        yield '', join_('        </head>\n')
        yield '', join_('        <body>\n')
        yield '', join_(escape_(username, True), '\n')
        yield '', join_('<ul>\n')
        for tag in loop.setup(tags):
            yield '', join_('    <li>', escape_(tag, True), '</li>\n')
        yield '', join_('</ul>\n')
        yield '', join_(escape_(form_add_tag.render(), False), ' <button type="button" id="add_tag">Add tag</button>\n')
        yield '', join_('\n')
        yield '', join_('        </body>\n')
        yield '', join_('</html>\n')
    return __template__

dashboard = CompiledTemplate(dashboard(), 'templates/dashboard.html')


def index():
    loop = ForLoop()
    _dummy  = CompiledTemplate(lambda: None, "dummy")
    join_ = _dummy._join
    escape_ = _dummy._escape

    def __template__ (username):
        yield '', join_('\n')
        yield '', join_(escape_(username, True), '\n')
    return __template__

index = CompiledTemplate(index(), 'templates/index.html')

