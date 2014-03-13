import time
import curses


def pbar(window):
    curses.use_default_colors()
    for i in range(30):
        window.addstr(10, 10, "[" + ("=" * i) + ">" + (" " * (10 - i )) + "]")
        window.refresh()
        time.sleep(0.5)

curses.wrapper(pbar)
