from scipy import misc
import numpy as np


def read_as_1d_array(filename):
    print("reading as 1d array")
    ret = flatten(read_as_array(filename))
    print("read")
    return ret

def read_as_array(filename):
    return misc.imread(filename, flatten=True)

def flatten(ndarr):
    return np.reshape(ndarr, (1, -1))[0]

def difference(flat1, flat2):
    print("calculating diff")
    return abs(flat1 - flat2)

def similarity(flat1, flat2, threshold = 25):
    diff = difference(flat1, flat2)
    # diff_count = len(list(filter(lambda x: x >= threshold, diff)))
    "counting diff values"
    diff_count = sum(d >= threshold for d in diff)
    return 1.0 - (diff_count / len(diff))

def similarity_f(filename1, filename2, threshold = 25):
    return similarity(read_as_1d_array(filename1), read_as_1d_array(filename2), threshold)
