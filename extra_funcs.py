from math import ceil
from random import randint

def rand_with_step(low,high,step,count=1,bias=False):
    n = 1/step
    if count > 1:
        val = randint(low*n,high*n,count)*step
    else:
        val= randint(low*n,high*n)*step

    if bias:
        bias = ceil(low/step)*step - low
    else:
        bias = 0
    return val - bias