import curses
import time


def test(char, time):
    chars = char
    times = time
    print(chars)
    print(times)
    print(len(chars), len(times))
    return


def record():
    chars = []
    times = []

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    while True:
        c = stdscr.getch()
        print(time.time(), '\r')
        chars.append(chr(c))
        times.append(time.time())
        if c == ord('p'):
            print('print', '\r')
        elif c == ord('\n'):
            curses.endwin()
            break  # Exit the while loop
        elif c == curses.KEY_HOME:
            x = y = 0
    curses.endwin()

    test(chars, times)
    return


if __name__ == '__main__':
    record()