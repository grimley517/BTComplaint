'''
This module Controlls the daily actions that take place as part of the monitoring schedule.

email generation
Daily stats generation
'''

import os
import statistics as s

def runDalies():
    genStats()

def genStats():
    files = os.listdir("results")
    if 'stats.csv' in files:
        files.remove("stats.csv")
    with open("results/stats.csv", "wt") as fil:
        fil.write("Date, Average Ping, StdDev Ping,  Average Download, StdDev download, Average Upload, StdDev Upload, Availability \n")
        for filename in files:
            stats = genStatsFromFile(filename)
            fil.write(stats)


def genStatsFromFile(filename):
    fails = 0
    total = 0
    pings = []
    Upspeeds = []
    Downspeeds = []
    date = filename[0:10]
    filename = "results/"+ filename
    with open(filename, "r")as fil:
        for line in fil:
            total += 1
            contents = line.split(",")
            if contents[1] == "failed":
                fails +=1
            elif contents[0] =="Time (IsoFormat)":
                pass
            else:
                pings.append(float(contents[1]))
                Downspeeds.append(float(contents[2]))
                Upspeeds.append(float(contents[3]))
    availability = (total - fails) / total
    return ("{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}\n".format(date, s.mean(pings), s.pstdev(pings),s.mean(Downspeeds), s.pstdev(Downspeeds),s.mean(Upspeeds), s.pstdev(Upspeeds), availability ))


if __name__ == "__main__":
    runDalies()
