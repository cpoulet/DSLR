import matplotlib.pyplot as plt
import numpy as np
import time
import sys

FILE = '../data/dataset_train.csv'
HOGWARTS_HOUSE = {b'Gryffindor': 2, b'Hufflepuff': 3, b'Ravenclaw': 0, b'Slytherin': 1}
HOUSE_CONV = np.vectorize(lambda x: HOGWARTS_HOUSE[x])

EPOC_PATTERN = '%Y-%m-%d'
EPOC_CONV = np.vectorize(lambda x: int(time.mktime(time.strptime(x.decode(),EPOC_PATTERN))))

def histogram(f):

    data = np.genfromtxt(f, delimiter=',', names=True, dtype=None)
    #data['Hogwarts_House']=HOUSE_CONV(data['Hogwarts_House'])
    #data['Birthday']=EPOC_CONV(data['Birthday'])
    
    FIELD = data.dtype.names[6:]
    for f in FIELD:
        r = data[f]
        r.sort()
        plt.scatter(r, np.arange(len(r)))
        plt.title(f)
        plt.show()

def main():
    f = FILE if len(sys.argv) != 2 else sys.argv[1]
    histogram(f)

if __name__ == '__main__':
    main()
