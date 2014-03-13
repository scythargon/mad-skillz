#!/usr/bin/env python
# -*- coding:utf-8 -*-
# example eventbox.py

import pygtk
pygtk.require('2.0')
import gtk

class EventBoxExample:
    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Event Box")
        window.connect("destroy", lambda w: gtk.main_quit())
        window.set_border_width(1)
        window.set_size_request(200, 200)
        # Создаём EventBox для нашего окна
        event_box = gtk.EventBox()
        window.add(event_box)
        event_box.show()

        # Создаём длинную метку
        label = gtk.Label("Кликните здесь, чтобы выйти, выйти, выйти...")
        event_box.add(label)
        label.show()

        # Обрезаем её.
        label.set_size_request(110, 20)

        # И привязываем к ней событие
        event_box.set_events(gtk.gdk.BUTTON_PRESS_MASK)
        event_box.connect("button_press_event", lambda w,e: gtk.main_quit())

        # И другие вещи для которых нужно X Window...
        event_box.realize()
        event_box.window.set_cursor(gtk.gdk.Cursor(gtk.gdk.HAND1))

        # Выбираем зелёный фон
        event_box.modify_bg(gtk.STATE_NORMAL,
                            event_box.get_colormap().alloc_color("green"))

        window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    EventBoxExample()
    main()
