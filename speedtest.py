import subprocess
class speed:
    ping  = 0
    downSpeed = 0
    upSpeed = 0
    results = []

    def __init__(self):
        tester = self.runtest()
        self.ping = self.results[0]
        self.downSpeed = self.results[1]
        self.upSpeed = self.results[2]

    def extractNumbers(self, line):
        index1 = line.find(" ") +1
        line = line[index1:]
        index2 = line.find(" ")
        line = line[:index2]
        return float(line)

    def runtest(self):
        ''' Returns a List [Ping, download Speed, Upload speed] of results for a speedtest check.

         Ping is the latency in ms, download and upload are Speeds in Mbytes/s
        '''
        command = "speedtest-cli --bytes --simple"
        output = subprocess.check_output(command).decode()
        rows =  output.split("\r\n")
        answer = []
        for row in rows[0:3]:
            answer.append(self.extractNumbers(row))
        self.results = answer

if __name__ == "__main__":
    tester = speed()
    print(tester.results)
