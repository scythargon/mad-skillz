import urwid

palette = [
    ('banner', '', '', '', '#ffa', '#60d'),
    ('streak', '', '', '', 'g50', '#60a'),
    ('inside', '', '', '', 'g38', '#808'),
    ('outside', '', '', '', 'g27', '#a06'),
    ('bg', '', '', '', 'g7', '#d06'),]

txt = urwid.Text(('banner', u" Hello World "), align='center')
map1 = urwid.AttrMap(txt, 'streak')
txt2 = urwid.Text(('banner', u" Hello World2 "), align='center')
map2 = urwid.AttrMap(txt2, 'outside')
content = urwid.Pile([
    urwid.AttrMap(urwid.Divider(), 'outside'),
    urwid.AttrMap(urwid.Divider(), 'inside'),
    map1,
    urwid.AttrMap(urwid.Divider(), 'inside'),
    urwid.AttrMap(urwid.Divider(), 'outside')])
content = urwid.GridFlow([map1,map2],cell_width=20,h_sep=1,v_sep=0, align='left')
fill = urwid.Filler(content)
map2 = urwid.AttrMap(fill, 'bg')

def exit_on_q(input):
    if input in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    if input in ('k', 'K'):
        txt2 = urwid.Text(('inside', u" Hello World2 "), align='center')
        map2 = urwid.AttrMap(txt2, 'inside')
        loop.screen.draw_screen(loop.screen.get_cols_rows(),)

loop = urwid.MainLoop(map2, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)

loop.run()
