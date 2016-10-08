from scipy import misc
import numpy as np
from functools import reduce


def read_as_1d_array(filename):
    print("reading as 1d array")
    ret = flatten(read_as_array(filename))
    print("read")
    return ret

def read_as_array(filename):
    return misc.imread(filename, flatten=True)

def flatten(ndarr):
    return np.reshape(ndarr, (1, -1))[0]

def relative_diff(flat1, flat2, bias = 20):
    print("calculating diff")
    return abs(flat1 - flat2) / ((flat1 + flat2 + bias) / 2)

def difference(flat1, flat2, threshold = 0.2):
    diff = relative_diff(flat1, flat2)
    # diff_count = len(list(filter(lambda x: x >= threshold, diff)))
    print("counting diff values")
    # diff_count = sum(d >= threshold for d in diff)
    #diff_count = reduce(lambda count, i: count + (i >= threshold), diff, 0)
    diff_count = np.sum(diff >= threshold)
    print(diff_count)
    print(len(diff))
    print("returning")
    return (float(diff_count) / float(len(diff)))

def difference_f(filename1, filename2, threshold = 0.2):
    return difference(read_as_1d_array(filename1), read_as_1d_array(filename2), threshold)
