import time
import math
import sys
import csv


class User:
    # @classmethod
    # def __init__(self, username, times, passwords):
    #     self.username = username
    #     self.calibration_times = times
    #     self.password = passwords[0]
    #     self.average_times = []
    #     self.total_times = [0] * len(self.password)
    #     self.allowed_difference = []
    #     self.actual_times = [0] * len(self.password)
    #     self.calibration_actual = [0] * len(self.password)
    #     self.max_difference = [0] * len(self.password)

    def __init__(self, username, password, average_times, max_difference):
        self.username = username
        self.password = password
        self.average_times = average_times
        self.max_difference = max_difference

    def get_upper_bound(self, i):
        return self.average_times[i] + self.max_difference[i]

    def get_lower_bound(self, i):
        return self.average_times[i] - self.max_difference[i]

    def calculate(self):
        # gets total times
        for i in self.calibration_times:
            for j in range(len(self.calibration_times[0])):
                self.total_times[j] = self.total_times[j] + i[j]

        # gets differences
        for i in range(len(self.total_times) - 1, 0, -1):
            self.actual_times[i] = (self.total_times[i] - self.total_times[i - 1])

        # calculates average
        for i in range(len(self.total_times)):
            self.average_times.append(self.actual_times[i] / 5.0)

        # get actual times for all of the times
        # there's an issue for the 2nd time
        self.calibration_actual = self.calibration_times
        for i in self.calibration_actual:
            for j in range(len(self.calibration_times[0]) - 1, 0, -1):
                i[0] = 0.0
                i[j] = (i[j] - i[j - 1])

        # find max difference
        for i in self.calibration_actual:
            for j in range(len(i)):
                if abs(i[j] - self.average_times[j]) > abs(self.max_difference[j]):
                    self.max_difference[j] = abs(i[j] - self.average_times[j])
        print(self.average_times)
        print(self.max_difference)
        return

    def get_max_difference(self, index):
        return self.max_difference[index]

    def get_password(self):
        return self.password