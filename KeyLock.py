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
                # print(i, users[0].get_lower_bound(i), time[i], users[0].get_upper_bound(i))
        print("Behavior match of:", round(((13 - error_count) / 12.0) * 100, 2), "%")
        if error_count > 5:
            print("Behavior not recognized: Access Denied")
        else:
            print("Behavior accepted: Access Granted")
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

    user = User.User(username, times, passwords)
    user.calculate()
    # user.save()
    return


def record():
    chars = []
    times = []
    x = input("The password is cutiehack2017, press enter to continue")
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
    # calibrate()
    return


def get_users():

    return


def hard_code_user():
    users = []
    # average = [0.0, 0.1434384822845459, 0.18655734062194823, 0.15121641159057617, 0.11398177146911621,
    #            0.2563174247741699, 0.15948715209960937, 0.19812865257263185, 0.17024898529052734,
    #            0.24525556564331055, 0.16770267486572266, 0.1372781753540039, 0.28838601112365725]
    # max_difference = [0, 1.0390203952789308, 0.05423254966735841, 0.019052171707153315, 0.04508228302001953,
    #                   0.09336166381835936, 0.05545606613159179, 0.015803146362304676, 0.04236888885498047,
    #                   0.044680690765380865, 0.07027626037597656, 0.020728731155395502, 0.20064315795898435]

    # average = [0.0, 0.11896739006042481, 0.16470274925231934, 0.10321245193481446, 0.12813382148742675,
    #            0.13887276649475097, 0.11833658218383789, 0.2154146671295166, 0.13225293159484863, 0.16560139656066894,
    #            0.12357182502746582, 0.15518922805786134, 0.16103367805480956]
    # max_difference = [0, 0.6472875118255615, 0.05145611763000488, 0.011251306533813482, 0.0316934108734131,
    #                   0.002700710296630854, 0.022640609741210932, 0.031599378585815435, 0.028830766677856445,
    #                   0.044561719894409185, 0.025412130355834964, 0.017115068435668956, 0.052982282638549816]

    average = [0.0, 0.11495003700256348, 0.1513669490814209, 0.0997690200805664, 0.1288576602935791,
               0.1336491584777832, 0.12804708480834961, 0.18513069152832032, 0.11374320983886718,
               0.14815707206726075, 0.12388978004455567, 0.13360671997070311, 0.14046182632446289]
    max_difference = [0, 0.9025970935821533, 0.03393197059631348, 0.020350074768066412, 0.07194538116455079,
                      0.03846068382263185, 0.028853988647460943, 0.023185586929321295, 0.02988495826721191,
                      0.02065281867980956, 0.016804361343383784, 0.012607860565185536, 0.02646527290344239]
    justin = User.User('jchan110', 'cutiehack2017', average, max_difference)
    users.append(justin)
    return users

if __name__ == '__main__':
    # users = hard_code_user()
    function()