from sys import stdout
from time import sleep
from math import floor

SYMBOLS = ["⋮", "⋰", "⋯", "⋱"]

class Loader:
    count = 0

    def load(self: object, percentage: float):
        """
        :param percentage: float
        - number between 0.0 and 100.0
        """
        progress = '='*floor(float(percentage)/2)
        left = ' '*(50-len(progress))
        stdout.write('\r')
        string = "{}% [{}] {}\t".format(int(percentage), progress + left, SYMBOLS[self.count % 4])
        stdout.write(string)
        stdout.flush()
        self.count += 1

def main():
    loader = Loader()
    for i in range(101):
        loader.load(i)
        sleep(0.2)

if __name__ == "__main__":
    main()
