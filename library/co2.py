#a2.t4 #This program is to create a function to check carbondioxide content in air
#taking advantage of python statistics library
import statistics
def check_air_quality(carbondioxide_data):
    if statistics.median(carbondioxide_data) >= 400 and statistics.median(carbondioxide_data) < 700:
        return "EXCELLENT"
    elif statistics.median(carbondioxide_data) >= 700 and statistics.median(carbondioxide_data) < 900:
        return "GOOD"
    elif statistics.median(carbondioxide_data) >= 900 and statistics.median(carbondioxide_data) < 1100:
        return "FAIR"
    elif statistics.median(carbondioxide_data) >= 1100 and statistics.median(carbondioxide_data) < 1600:
        return "MEDIOCRE"
    elif statistics.median(carbondioxide_data) >= 1600 and statistics.median(carbondioxide_data) <=2100:
        return "BAD"
