'''Read a file of temperatures and find some basic information:
    highest, lowest, average, median
'''

class TemperatureFile():

    def __init__(self):
        self._read_temperature_file()
        self.length = len(self.temperatures)

    def _read_temperature_file(self):
        self.temperatures = []
        with open('ch5\lab_05.txt') as f:
            for row in f:
                self.temperatures.append(float(row.strip()))

    def highest(self):
        return max(self.temperatures)

    def lowest(self):
        return min(self.temperatures)

    def sum(self):
        return sum(self.temperatures)
    
    def median(self):
        if self.length % 2:
            return self.temperatures[self.length//2]
        else:
            return (self.temperatures[self.length//2] + self.temperatures[self.length//2 - 1]) / 2
    
    def average(self):
        return self.sum() / self.length

def main():
    temperature_file = TemperatureFile()
    print(temperature_file.highest())
    print(temperature_file.lowest())
    print(temperature_file.sum())
    print(temperature_file.median())
    print(temperature_file.average())

if __name__ == "__main__":
    main()