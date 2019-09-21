#a2.t5 #This program is to create a function to check tvoc in air
#taking advantage of python statistics library
import statistics
def get_tvoc_info(TVOC_ppb):
    if statistics.median(TVOC_ppb) > 2200 and statistics.median(TVOC_ppb) < 5500:
        return "Unhealthy"
    elif statistics.median(TVOC_ppb) > 660 and statistics.median(TVOC_ppb) < 2200:
        return "Poor"
    elif statistics.median(TVOC_ppb) > 220 and statistics.median(TVOC_ppb) < 660:
        return "Moderate"
    elif statistics.median(TVOC_ppb) > 65 and statistics.median(TVOC_ppb) < 220:
        return "Good"
    elif statistics.median(TVOC_ppb) > 0 and statistics.median(TVOC_ppb) < 65:
        return "Excellent"
