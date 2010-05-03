from web.template import compile_templates
import pyinotify


def watch_templates():
    wm = pyinotify.WatchManager()
    mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_CLOSE_WRITE 

    class HandleEvents(pyinotify.ProcessEvent):
        def process_default(self, event):
            if event.name.strip().endswith('.html'):
                print "compile_templates, changes detected in", event.name 
                compile_templates('templates')

    p = HandleEvents()
    notifier = pyinotify.Notifier(wm, p)
    wdd = wm.add_watch('templates', mask, rec=True)
    print "nottmp changes detecter started, hit ctr^c to kill me"
    notifier.loop()

if __name__=='__main__':
    watch_templates()
