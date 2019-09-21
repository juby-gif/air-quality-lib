#a2.t3 #This program is to create functions to find mean,maximum and minimum value,median,range,mode,standard deviation.Variance
#taking advantage of python statistics library
import statistics
def get_mean(array):
    return statistics.mean(array)

def get_max_value(array):
    return max(array)

def get_min_value(array):
    return min(array)

def get_median(array):
    return statistics.median(array)

def get_range(array):
    return range(len(array))

def get_mode(array):
    return statistics.mode(array)

def get_stdeviation(array):
    return statistics.stdev(array)

def get_variance(array):
    return statistics.variance(array)
