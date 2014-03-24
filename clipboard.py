import pygtk
pygtk.require('2.0')
import gtk
import time
clipboard = gtk.clipboard_get()
old_text=''
while True:
    text=clipboard.wait_for_text()
    if text!=old_text:
        print text
        old_text=text
    time.sleep(0.5)
