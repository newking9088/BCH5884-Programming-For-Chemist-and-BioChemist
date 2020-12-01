#!usr/bin/env python3

class Chromat():
    def __init__(self,fileName):
        f = open(fileName,'r')
        f.readline()
        f.readline()
        f.readline()
        lines = f.readlines()
        f.close()

        time = []
        absorbance = []
        for n in lines:
            words = n.split()
            if len(words) == 2:
                time.append(float(words[0]))
                absorbance.append(float(words[1]))
            self.time = np.array(time)
            self.absorbance= np.array(absorbance)

        def plot(self):
            plt.plot(self.time,self.absorbance,'ro')

if __name__ == "__main__":
    chromat = Chromat("superose6_50.asc")
    chromat.plot()
