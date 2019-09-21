#a2.t1 #This program is to create functions for performing conversion to Celsius, Fareheit and Kelvin
def c_to_f(c):
    f = (c * 9/5) + 32 #Formula to convert Celsius to Fareheit
    return f

def c_to_k(c):
    k = c + 273.15 #Formula to convert Celsius to Kelvin
    return k

def f_to_c(f):
    fa = (f-32) * 5/9 #Formula to convert Fareheit to Celsius
    return fa

def f_to_k(f):
    k = (f-32) * 5/9 + 273.15 #Formula to convert Fareheit to Kelvin
    return k

def k_to_c(k):
    c = k - 273.15 #Formula to convert Kelvin to Celsius
    return c

def k_to_f(k):
    f = (k - 273.15) * 9/5 + 32 #Formula to convert Kelvin to Fareheit
    return f
