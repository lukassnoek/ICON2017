import numpy as np
import os.path as op

def double_gamma(x, lag=6, a2=12, b1=0.9, b2=0.9, c=0.35):
    a1 = lag
    d1 = a1 * b1
    d2 = a2 * b2
    return np.array([(t/(d1))**a1 * np.exp(-(t-d1)/b1) - c*(t/(d2))**a2 * np.exp(-(t-d2)/b2) for t in x])

def single_gamma(x, lag=6, b=0.9):
    a = lag
    d = a * b
    return (x/d)**a * np.exp(-(x-d)/b)

def return_some_objects():

    obj1 = (5, 3, 2)
    obj2 = True
    obj3 = 5.3216
    return(obj1, obj2, obj3)

def sort_nifti_paths(paths, idf='tstat'):

    return sorted(paths, key=lambda x: int(op.basename(x).split('.')[0].split(idf)[-1]))
