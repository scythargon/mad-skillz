import urwid
from Aurwid import *
import random

class ItemWidget (urwid.WidgetWrap):

    def __init__ (self, id, description):
        self.id = id
        self.name = 'name'
        self.last_send = '1:15'
        self.pause = '1:00'
        self.last_new = '5:17'
        self.content = 'item %s: %s...' % (str(id), description[:25])
        """self.item = [
            ('fixed', 2, urwid.AttrWrap(urwid.Text('% 2s' % self.id), 'body', 'focus')),
            ('fixed', 15, urwid.Padding(urwid.AttrWrap(
                urwid.Text('item %s' % str(id)), 'body', 'focus'), left=2)),
            urwid.AttrWrap(urwid.Text('%s' % description), 'body', 'focus'),
        ]
        w = urwid.Columns(self.item)
        self.__super.__init__(w)
        """
        self.text = urwid.Text('bla bla bla bla bla bla bla bla bla bla bla bla bla bla ')
        self.text2 = urwid.Text('!!!! %s: %s' % (id, description))
        self.item = urwid.AttrWrap(
            self.text, 'body', 'focus'
            )
        self.item2 = urwid.AttrWrap(
            self.text2, 'body', 'focus'
            )
        super(ItemWidget, self).__init__(self.item)
    def selectable (self):
        return True

    def keypress(self, size, key):
        #self.text.set_text(str(key))
        self.item=self.item2
        super(ItemWidget, self).__init__(self.item2)
        return key
class ARow(AGridFlow):
    def __init__(self,t1,t2):
        AGridFlow.__init__(self,[t1,t2],cell_width=8,h_sep=1,v_sep=0, align='left')
    def selectable (self):
        return True
def main ():

    palette = [
        ('body','dark cyan', '', 'standout','#0f6',''),
        ('mooo','dark cyan', '', 'standout','light blue',''),
        ('focus','dark red', '', 'standout','light red',''),
        ('head','light red', 'black'),
        ]

    lorem = [
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'Sed sollicitudin, nulla id viverra pulvinar.',
        'Cras a magna sit amet felis fringilla lobortis.',
    ]
    
    def keystroke (input):
        if input in ('q', 'Q'):
            raise urwid.ExitMainLoop()

        if input is 'enter':
            focus = listbox.get_focus()[0].content
            view.set_header(urwid.AttrWrap(urwid.Text(
                'selected: %s' % str(focus)), 'head'))

    items = []
    for i in range(10):
        items.append(ItemWidget(i, random.choice(lorem)))
    t1 = urwid.Text('11111')
    t2 = urwid.Text('!!!!')
    tt1=urwid.AttrWrap(
            t1, 'mooo', 'focus'
            )
    tt2=urwid.AttrWrap(
            t2, 'mooo', 'focus'
            )
    content = ARow(tt1,tt2)#,cell_width=3,h_sep=1,v_sep=0, align='left')
    items.append(content)
    header = urwid.AttrMap(urwid.Text('selected:'), 'head')
    listbox = urwid.ListBox(urwid.SimpleListWalker(items))
    view = urwid.Frame(urwid.AttrWrap(listbox, 'body'), header=header)
    loop = urwid.MainLoop(view, palette, unhandled_input=keystroke)
    loop.screen.set_terminal_properties(colors=256)
    loop.run()

if __name__ == '__main__':
    main()
