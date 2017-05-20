import User

import curses
import time
import csv


def test(char, time):
    error_count = 0
    users = hard_code_user()
    actual_average = users[0].average_times
    actual_time = time
    pw = ''.join(char[:-1])

    temp = actual_average
    temp2 = actual_average
    temp[0] = 0
    temp2[0] = 0
    if users[0].get_password() == pw:
        for i in range(len(time) - 1, 0, -1):
            actual_time[i] = (time[i] - time[i - 1])
        # check range
        for i in range(len(time) - 1):
            if (time[i] > users[0].get_upper_bound(i)) or (time[i] < users[0].get_lower_bound(i)):
                error_count = (error_count + 1)
        if error_count > 6:
            print("Invalid Password")
    else:
        print("Invalid password")
    return


def calibrate():
    times = []
    passwords = []

    username = input("Enter your username: ")

    stdscr = curses.initscr()
    curses.echo()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.clear()
    for i in range(5):
        chars = []
        time_ = []
        start_time = time.time()
        while True:
            # start_time = time.time()
            c = stdscr.getch()
            time_.append(time.time() - start_time)
            if c != 10:
                chars.append(chr(c))
            else:
                curses.endwin()
                break
        passwords.append(chars)
        times.append(time_[:-1])
        stdscr.clear()
        curses.endwin()

    # trim data
    user = User.User(username, times, passwords)
    user.calculate()
    user.save()
    return


def record():
    chars = []
    times = []
    print("The password is cutiehack2017")
    stdscr = curses.initscr()
    curses.echo()
    curses.cbreak()
    stdscr.keypad(True)

    while True:
        c = stdscr.getch()
        chars.append(chr(c))
        times.append(time.time())
        if c == 10:
            curses.endwin()
            break
    curses.endwin()

    test(chars, times)
    return


def function():
    record()
    # if input("Are you new user? (Y/N) ") == "N":
    #     username = input("Enter your username: ")
    #     record()
    # else:
    #     calibrate()
    return


def get_users():
    # username = None
    # average_times = []
    # max_difference = []
    #
    # with open('users.csv', 'r') as csvfile:
    #     row = csv.reader(csvfile, delimiter=',', quotechar='"')
    #     for i in row:
    #         print(i)
    #         if i == 'jchan110':
    #             username = i
    #         elif i == 0.0:
    #             average_times.append(i)
    #         elif i == 0:
    #             max_difference.append(i)
    # print(average_times)
    # print(max_difference)
    return


def hard_code_user():
    users = []
    average = [0.0, 0.1434384822845459, 0.18655734062194823, 0.15121641159057617, 0.11398177146911621, 0.2563174247741699, 0.15948715209960937, 0.19812865257263185, 0.17024898529052734, 0.24525556564331055, 0.16770267486572266, 0.1372781753540039, 0.28838601112365725]
    max_difference = [0, 1.0390203952789308, 0.05423254966735841, 0.019052171707153315, 0.04508228302001953, 0.09336166381835936, 0.05545606613159179, 0.015803146362304676, 0.04236888885498047, 0.044680690765380865, 0.07027626037597656, 0.020728731155395502, 0.20064315795898435]
    user = User.User('jchan110', 'cutiehack2017', average, max_difference)
    users.append(user)
    return users

if __name__ == '__main__':
    users = hard_code_user()
    function()