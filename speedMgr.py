'''This module manages the data handling arround the speed tests.

this module performs a number of functions related to the internal organisation of speed test data.
It schedules speed tests,
stores the data in a daily file,
works out whether an email is necessary,
composes the email
sends the email
'''
import speedtest as st
from datetime import datetime, date, time, timedelta
import os.path as Path

def updatefile(speedcheck):
    filename = "results/{0} speedresults.csv".format(date.today())
    t = datetime.now().time().isoformat()
    if not Path.isfile(filename):
        with open(filename, "w") as fil:
            fil.write("time, ping, down, up\n")
    with open(filename, "at") as fil:
        line = "{0}, {1}, {2}, {3}\n".format(t, speedcheck.ping, speedcheck.downSpeed, speedcheck.upSpeed)
        fil.write(line)
        print(line)



if __name__ == "__main__":
    running = True
    nextRun = datetime.now()
    runs = 0
    while running:
        if (datetime.now() > nextRun):
            runs += 1
            nextRun = nextRun + timedelta(minutes = 1)
            speed = st.speed()
            updatefile(speed)
            if (runs >= 3):
                running = False
