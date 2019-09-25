import os
import library.statistics
import library.humidity
import library.tvoc
import library.co2
import statistics
TEMPERATURE_ID = 1 #ID number is assigned
HUMIDITY_ID = 2
PRESSURE_ID = 3
ALTITUDE_ID = 4
TVOC_ID = 5
CO2_ID = 6
class TimeSeriesData:
    id = 0
    value = 0
    time = 0
    def __init__(self,id,value,time): #constructor
        self.id = id
        self.value = value
        self.time = time

class Instrument:
    data = [] #since data is initialized as a list no need for constructor
    def add_datum(self,id,value,time):
        datum = TimeSeriesData(id,value,time)
        self.data.append(datum)

    def get_values_by_id(self,id):
        values_list = [] #append values by id
        for datum in self.data:
            if datum.id == id:
                values_list.append(datum.value)
        return values_list

    def get_mean_by_id(self,id):
        values_list = self.get_values_by_id(id)
        mean = statistics.mean(values_list)
        return mean

    def get_median_by_id(self,id):
        values_list = self.get_values_by_id(id)
        median = statistics.median(values_list)
        return median

    def print_list(self):
        print("Id " + "\t" + "Data " + "\t" + "Time")
        for datum in self.data:
            print(str(datum.id) +"\t"+ str(datum.value) +"\t"+ str(datum.time))


tool = Instrument()
#Provides the user with a graphical user interface options
def get_command_input():
    print(" ")
    os.system('clear')
    print("Indoor Air Quality Monitoring Command Console")
    print(" ")
    print("**********************************************")
    print(" ")
    print("Please select from the following options: ")
    print(" ")
    print("     1. Add Reading\n")
    print("     2. List Readings\n")
    print("     3. Calculate\n")
    print("     4. Exit\n")
    print("  ")
    command_input = int(input("Please Input your option : "))
    os.system('clear')
    return command_input
#To perform User input selection and processing
def main():
    main_loop_is_running = True
    while main_loop_is_running:
        command = get_command_input()
        if command == 1:
            os.system('clear')
            print("Please input  Readings .... \n")
            os.system('clear')
            print(" ")
            id = int(input("Enter the ID Number : "))
            value = int(input("Ente the value : "))
            time = int(input("Enter the Time : "))
            tool.add_datum(id,value,time)

        elif command ==2:
#to tabulate the datas inputted by the user
            if len(tool.data) <=0:
                print("Enter Atleast one Single Data")
            else:
                print(" \n")
                print(" \n")
                print("Indoor Air Quality Monitoring Command Console\n")
                print(" ")
                print("*********************************************\n")
                print(" ")
                print("LIST \n")
                print(" ")
                print(" ")
                tool.print_list()

        elif command == 3:
    # To perform various operations by importing the functions from library and display them for Temperature,Humidity,Pressure,TVOC and CO2
            os.system('clear')
            print("---------------------------------------------\n")
            print(" ")
            print("Indoor Air Quality Monitoring Command Console\n ")
            print(" ")
            print("**********************************************\n")
            print(" \n")
            print("TEMPERATURE ")
            print(" ")
            print("Unit :  Degrees ")
            print("Max : ",library.statistics.get_max_value(tool.get_values_by_id(TEMPERATURE_ID)))
            print("Min : ",library.statistics.get_min_value(tool.get_values_by_id(TEMPERATURE_ID)))
            print("Median :",tool.get_median_by_id(TEMPERATURE_ID))
            print("Mode : ",library.statistics.get_mode(tool.get_values_by_id(TEMPERATURE_ID)))
            print("Range :",library.statistics.get_range(tool.get_values_by_id(TEMPERATURE_ID)))
            print("Std : ",library.statistics.get_stdeviation(tool.get_values_by_id(TEMPERATURE_ID)))
            print("Var : ",library.statistics.get_variance(tool.get_values_by_id(TEMPERATURE_ID)))
            print(" \n")
            print("HUMIDITY ")
            print(" ")
            print("Unit :  % ")
            print("Air Quality : ",library.humidity.get_humidity_value(tool.get_values_by_id(HUMIDITY_ID)))
            print("Max : ",library.statistics.get_max_value(tool.get_values_by_id(HUMIDITY_ID)))
            print("Min : ",library.statistics.get_min_value(tool.get_values_by_id(HUMIDITY_ID)))
            print("Median :",tool.get_median_by_id(HUMIDITY_ID))
            print("Mode : ",library.statistics.get_mode(tool.get_values_by_id(HUMIDITY_ID)))
            print("Range :",library.statistics.get_range(tool.get_values_by_id(HUMIDITY_ID)))
            print("Std : ",library.statistics.get_stdeviation(tool.get_values_by_id(HUMIDITY_ID)))
            print("Var : ",library.statistics.get_variance(tool.get_values_by_id(HUMIDITY_ID)))
            print(" \n")
            print("PRESSURE ")
            print(" ")
            print("Unit : kPa ")
            print("Max : ",library.statistics.get_max_value(tool.get_values_by_id(PRESSURE_ID)))
            print("Min : ",library.statistics.get_min_value(tool.get_values_by_id(PRESSURE_ID)))
            print("Median :",tool.get_median_by_id(PRESSURE_ID))
            print("Mode : ",library.statistics.get_mode(tool.get_values_by_id(PRESSURE_ID)))
            print("Range :",library.statistics.get_range(tool.get_values_by_id(PRESSURE_ID)))
            print("Std : ",library.statistics.get_stdeviation(tool.get_values_by_id(PRESSURE_ID)))
            print("Var : ",library.statistics.get_variance(tool.get_values_by_id(PRESSURE_ID)))
            print(" \n")
            print("ALTITUDE ")
            print(" ")
            print("Unit : ft ")
            print("Max : ",library.statistics.get_max_value(tool.get_values_by_id(ALTITUDE_ID)))
            print("Min : ",library.statistics.get_min_value(tool.get_values_by_id(ALTITUDE_ID)))
            print("Median :",tool.get_median_by_id(ALTITUDE_ID))
            print("Mode : ",library.statistics.get_mode(tool.get_values_by_id(ALTITUDE_ID)))
            print("Range :",library.statistics.get_range(tool.get_values_by_id(ALTITUDE_ID)))
            print("Std : ",library.statistics.get_stdeviation(tool.get_values_by_id(ALTITUDE_ID)))
            print("Var : ",library.statistics.get_variance(tool.get_values_by_id(ALTITUDE_ID)))
            print(" \n")
            print("TVOC ")
            print(" ")
            print("Unit : ppb ")
            print("Air Quality : ",library.tvoc.get_tvoc_info(tool.get_values_by_id(TVOC_ID)))
            print("Max : ",library.statistics.get_max_value(tool.get_values_by_id(TVOC_ID)))
            print("Min : ",library.statistics.get_min_value(tool.get_values_by_id(TVOC_ID)))
            print("Median :",tool.get_median_by_id(TVOC_ID))
            print("Mode : ",library.statistics.get_mode(tool.get_values_by_id(TVOC_ID)))
            print("Range :",library.statistics.get_range(tool.get_values_by_id(TVOC_ID)))
            print("Std : ",library.statistics.get_stdeviation(tool.get_values_by_id(TVOC_ID)))
            print("Var : ",library.statistics.get_variance(tool.get_values_by_id(TVOC_ID)))
            print(" \n")
            print("CO2 ")
            print(" ")
            print("Unit : ppm ")
            print("Air Quality : ",library.co2.check_air_quality(tool.get_values_by_id(CO2_ID)))
            print("Max : ",library.statistics.get_max_value(tool.get_values_by_id(CO2_ID)))
            print("Min : ",library.statistics.get_min_value(tool.get_values_by_id(CO2_ID)))
            print("Median :",tool.get_median_by_id(CO2_ID))
            print("Mode : ",library.statistics.get_mode(tool.get_values_by_id(CO2_ID)))
            print("Range :",library.statistics.get_range(tool.get_values_by_id(CO2_ID)))
            print("Std : ",library.statistics.get_stdeviation(tool.get_values_by_id(CO2_ID)))
            print("Var : ",library.statistics.get_variance(tool.get_values_by_id(CO2_ID)))
            print(" \n")
            os.system('clear')
        elif command == 4:
            main_loop_is_running = False
if __name__ == "__main__":
    main()
