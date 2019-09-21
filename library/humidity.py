#a2.t2 #This program is to create a function to assess humidity
#taking advantage of python statistics library
import statistics
def get_humidity_value(humidity_value):
    if statistics.median(humidity_value) < 30:
        return "It is Dry"
    elif statistics.median(humidity_value) > 60:
        return "High Humidity"
    else:
        return "It's OK"
