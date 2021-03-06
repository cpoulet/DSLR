import matplotlib.pyplot as plt
import numpy as np
import time
import sys

FILE = '../data/dataset_train.csv'
HOGWARTS_HOUSE = {b'Gryffindor': 2, b'Hufflepuff': 3, b'Ravenclaw': 0, b'Slytherin': 1}

def histogram(f):

    data = np.genfromtxt(f, delimiter=',', names=True, dtype=None)
    
    FIELD = data.dtype.names[6:]
    for f in FIELD:
        rslt = [data[data['Hogwarts_House'] == h][f] for h in HOGWARTS_HOUSE]
        rslt = [arr[~np.isnan(arr)] for arr in rslt]
        plt.hist(rslt, bins=20, alpha=0.8, histtype='stepfilled')
        plt.title(f)
        plt.show()

def main():
    f = FILE if len(sys.argv) != 2 else sys.argv[1]
    histogram(f)

if __name__ == '__main__':
    main()
