from web.template import CompiledTemplate, ForLoop


def dashboard():
    loop = ForLoop()
    _dummy  = CompiledTemplate(lambda: None, "dummy")
    join_ = _dummy._join
    escape_ = _dummy._escape

    def __template__ (username,tags,form_add_tag, form_add_note):
        yield '', join_('<html>\n')
        yield '', join_('        <head>\n')
        yield '', join_('                \n')
        yield '', join_('                <link type="text/css" href="/s/css/smoothness/jquery-ui-1.8.1.custom.css" rel="stylesheet" />\n')
        yield '', join_('                <link type="text/css" href="/s/css/bidoru.css" rel="stylesheet" />\n')
        yield '', join_('                <script type="text/javascript" src="/s/js/jquery-1.4.2.min.js"></script>\n')
        yield '', join_('                <script type="text/javascript" src="/s/js/jquery-ui-1.8.1.custom.min.js"></script>\n')
        yield '', join_('                <script type="text/javascript" src="/s/js/jquery.form.js"></script>\n')
        yield '', join_('\n')
        yield '', join_('                <script type="text/javascript">\n')
        yield '', join_('                ', '$', '(document).ready( function() {\n')
        yield '', join_('                                ', '$', '("#tabs").tabs();\n')
        yield '', join_('                                ', '$', '("form#add_tag_form").ajaxForm({\n')
        yield '', join_("                                url:'/ajax/tags/add/',\n")
        yield '', join_("                                dataType:'json',\n")
        yield '', join_("                                type:'post',\n")
        yield '', join_('                                success:function(data) \n')
        yield '', join_('                                {\n')
        yield '', join_("                                        if (data['errors'] == undefined)\n")
        yield '', join_('                                        {\n')
        yield '', join_('                                                ', '$', "('<li>'+data['response']+'</li>').appendTo('#tags');\n")
        yield '', join_('                                                ', '$', '("#message").html(data[\'message\']);\n')
        yield '', join_('                                        }\n')
        yield '', join_('                                        else\n')
        yield '', join_('                                        {\n')
        yield '', join_('                                                \n')
        yield '', join_('                                        ', '$', '("#message").html(data[\'message\'] +\' - \'+data[\'errors\'][\'tag\']);\n')
        yield '', join_('                                        };\n')
        yield '', join_('                                        ', '$', '("form#add_tag_form").clearForm();\n')
        yield '', join_('                                }\n')
        yield '', join_('                                });\n')
        yield '', join_('\n')
        yield '', join_('                                ', '$', '("form#add_note_form").ajaxForm({\n')
        yield '', join_("                                url:'/ajax/notes/add/',\n")
        yield '', join_("                                dataType:'json',\n")
        yield '', join_('                                beforeSerialize: function() \n')
        yield '', join_('                                {\n')
        yield '', join_('                                        result = ', '$', '.map(', '$', '("#tag_list a.highl"), function(elem) {return elem.innerHTML}).join(\',\');\n')
        yield '', join_('                                        ', '$', '("#ntag_list")[0].value=result;\n')
        yield '', join_('                                        alert(result);\n')
        yield '', join_('                                },\n')
        yield '', join_('\n')
        yield '', join_("                                type:'post',\n")
        yield '', join_('                                success:function(data) \n')
        yield '', join_('                                {\n')
        yield '', join_('                                        alert(data);\n')
        yield '', join_('                                }\n')
        yield '', join_('                                });\n')
        yield '', join_('\n')
        yield '', join_('                                ', '$', '("#tag_list a").click(function() {', '$', "(this).toggleClass('highl',50)});\n")
        yield '', join_('                                \n')
        yield '', join_('                }); \n')
        yield '', join_('                </script>\n')
        yield '', join_('        </head>\n')
        yield '', join_('        <body>\n')
        yield '', join_('  <div id="username" class="ui-widget ui-widget-content ui-corner-bottom"><p>', escape_(username, True), '</p></div>\n')
        yield '', join_('        <div id="tabs">\n')
        yield '', join_('                <ul class="tabs-header">\n')
        yield '', join_('                        <li><a href="#tabs-notes">notes</a>\n')
        yield '', join_('                        <li><a href="#tabs-tags">tags</a>\n')
        yield '', join_('                </ul>\n')
        yield '', join_('        \n')
        yield '', join_('                \n')
        yield '', join_('\n')
        yield '', join_('                <div id="tabs-notes">\n')
        yield '', join_('                        \n')
        yield '', join_('                        <form id="add_note_form">\n')
        yield '', join_('                        ', escape_(form_add_note.render(), False), ' <button class="ui-state-default">add new note</button>\n')
        yield '', join_('                        </form>\n')
        yield '', join_('                        <div id="tag_list" class="ui-widget ui-widget-content ui-corner-bottom"><a>asad</a> <a>dasdadas</a> <a>dasdasdas</a></div>\n')
        yield '', join_('                </div>\n')
        yield '', join_('                <div id="tabs-tags" class="ui-widget-content">\n')
        yield '', join_('                        <ul id="tags">\n')
        for tag in loop.setup(tags):
            yield '', join_('                        ', '    <li>', escape_(tag, True), '</li>\n')
        yield '', join_('                        </ul>\n')
        yield '', join_('                        <form id="add_tag_form">\n')
        yield '', join_('                        ', escape_(form_add_tag.render(), False), ' <input class="ui-state-default" type="submit" id="add_tag" value="Add tag"/>\n')
        yield '', join_('                        <div id="message"></div>\n')
        yield '', join_('                        </form>\n')
        yield '', join_('                </div>\n')
        yield '', join_('\n')
        yield '', join_('        </div>\n')
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

