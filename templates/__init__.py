from web.template import CompiledTemplate, ForLoop


def dashboard():
    loop = ForLoop()
    _dummy  = CompiledTemplate(lambda: None, "dummy")
    join_ = _dummy._join
    escape_ = _dummy._escape

    def __template__ (username,tags,form_add_tag):
        yield '', join_('<html>\n')
        yield '', join_('        <head>\n')
        yield '', join_('                \n')
        yield '', join_('                <link type="text/css" href="/s/css/smoothness/jquery-ui-1.8.1.custom.css" rel="stylesheet" />\n')
        yield '', join_('                <script type="text/javascript" src="/s/js/jquery-1.4.2.min.js"></script>\n')
        yield '', join_('                <script type="text/javascript" src="/s/js/jquery-ui-1.8.1.custom.min.js"></script>\n')
        yield '', join_('                <script type="text/javascript" src="/s/js/jquery.form.js"></script>\n')
        yield '', join_('\n')
        yield '', join_('                <script type="text/javascript">\n')
        yield '', join_('                ', '$', '(document).ready( function() {\n')
        yield '', join_('                                ', '$', '("form#add_tag_form").ajaxForm({\n')
        yield '', join_("                                url:'/ajax/tags/add/',\n")
        yield '', join_("                                dataType:'json',\n")
        yield '', join_("                                type:'post',\n")
        yield '', join_('                                success:function(data) \n')
        yield '', join_('                                {\n')
        yield '', join_("                                        if (data['errors'] == undefined)\n")
        yield '', join_('                                        {\n')
        yield '', join_('                                                ', '$', "('<li>'+data['response']+'</li>').appendTo('#tags');\n")
        yield '', join_('                                        ', '$', '("#message").html(data[\'message\']);\n')
        yield '', join_('                                        }\n')
        yield '', join_('                                        else\n')
        yield '', join_('                                        {\n')
        yield '', join_('                                                \n')
        yield '', join_('                                        ', '$', '("#message").html(data[\'message\'] +\' - \'+data[\'errors\'][\'tag\']);\n')
        yield '', join_('                                        };\n')
        yield '', join_('                                        ', '$', '("form#add_tag_form").clearForm();\n')
        yield '', join_('                                        //alert(data)\n')
        yield '', join_('                                }\n')
        yield '', join_('                                });\n')
        yield '', join_('\n')
        yield '', join_('                }); \n')
        yield '', join_('                </script>\n')
        yield '', join_('        </head>\n')
        yield '', join_('        <body>\n')
        yield '', join_(escape_(username, True), '\n')
        yield '', join_('<ul id="tags">\n')
        for tag in loop.setup(tags):
            yield '', join_('    <li>', escape_(tag, True), '</li>\n')
        yield '', join_('</ul>\n')
        yield '', join_('<form id="add_tag_form">\n')
        yield '', join_(escape_(form_add_tag.render(), False), ' <input type="submit" id="add_tag" value="Add tag"/>\n')
        yield '', join_('<div id="message"></div>\n')
        yield '', join_('</form>\n')
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

