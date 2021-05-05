import curses

HEIGHT = 5
WIDTH = 40
BEGIN_X = 20
BEGIN_Y = 7

stdscr = curses.initscr()
stdscr.keypad(True)

curses.noecho()
curses.cbreak()

def close(stdscr):
	stdscr.keypad(False)
	curses.nocbreak()
	curses.echo()
	
	curses.endwin()

def main(stdscr):
	stdscr.clear()
	
	stdscr.addstr(0, 0, "hi", curses.A_BLINK)	
	stdscr.refresh()

curses.wrapper(main)
