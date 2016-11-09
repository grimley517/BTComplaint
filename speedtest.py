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
        try:
            command = ["python3", "speedtest-cli.py", "--bytes", "--simple"]
            output = subprocess.check_output(command).decode()
            print ("speedtest output -\n {0}".format(output))
            rows =  output.split("\n")
            answer = []
            print ("speedtest answer = {0}".format(answer))
            for row in rows[0:3]:
                answer.append(self.extractNumbers(row))
        except Exception as ex:
            answer = ["failed", 0, 0]
            print (" a {0} Exception occured".format(type(ex)))
            print(ex)

        self.results = answer

if __name__ == "__main__":
    tester = speed()
    print(tester.results)
