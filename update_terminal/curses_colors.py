import curses

def main(stdscr):
    stdscr.clear()
    curses.use_default_colors()
    #curses.init_color(1,400,0,0)
    if curses.has_colors():
        for i in xrange(1, curses.COLORS):
            curses.init_pair(i, i, curses.COLOR_BLACK)
            stdscr.addstr(str(curses.color_content(i))+"COLOR %d! " % i, curses.color_pair(i))
            stdscr.addstr(str(curses.can_change_color())+"BOLD! ", curses.color_pair(i) | curses.A_BOLD)
            stdscr.addstr("STANDOUT! ", curses.color_pair(i) | curses.A_STANDOUT)
            stdscr.addstr("UNDERLINE! ", curses.color_pair(i) | curses.A_UNDERLINE)
            stdscr.addstr("BLINK! ", curses.color_pair(i) | curses.A_BLINK)
            stdscr.addstr("DIM! ", curses.color_pair(i) | curses.A_DIM)
            stdscr.addstr("REVERSE! ", curses.color_pair(i) | curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getch()

if __name__ == '__main__':
    print "init..."
    curses.wrapper(main)
