import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import time
import sys

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
        [data[data['Hogwarts_House'] == h][f] for h in HOGWARTS_HOUSE]

def main():
    if len(sys.argv) != 1:
        f = '../data/dataset_train.csv'
    else:
        f = sys.argv[1]
    histogram(f)

if __name__ == '__main__':
    main()
