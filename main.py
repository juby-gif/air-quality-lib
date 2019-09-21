#a2.t6 #This program is to perform Air Quality Monitoring
#taking advantage of python statistics library
#taking advantage of humidity library
#taking advantage of tvoc library
#taking advantage of co2 library
#taking advantage of python operating system library
import os
import library.statistics
import library.humidity
import library.tvoc
import library.co2
temperature = []
humidity = []
pressure = []
altitude = []
tvoc = []
co2 = []
time = []
#Provides the user with a graphical interface
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
    value = int(input("Please Input your option : "))
    os.system('clear')
    return value
#To perform User input selection and processing
def main():
    main_loop_is_running = True
    while main_loop_is_running:
        value = get_command_input()
        if value == 1:
            os.system('clear')
            print("Please input 3 sets of Readings .... \n")
            os.system('clear')
            print(" ")
            for i in range(0,3): #loop to Input 3 sets of user input data
                temp_values = int(input("Input Temperature (degrees): "))
                temperature.append(temp_values)
                os.system('clear')
                humid_values = int(input("Input Humidity (%): "))
                humidity.append(humid_values)
                os.system('clear')
                pres_values = int(input("Input Pressure (kPa): "))
                pressure.append(pres_values)
                os.system('clear')
                alt_values = int(input("Input Altitude (ft): "))
                altitude.append(alt_values)
                os.system('clear')
                tvoc_values = int(input("Input TVOC (ppb): "))
                tvoc.append(tvoc_values)
                os.system('clear')
                co2_values  = int(input("Input CO2 (ppm): "))
                co2.append(co2_values)
                os.system('clear')
                time_value = int(input("Input Time (0000):"))
                time.append(time_value)
                os.system('clear')
            print(" \n")
            print("Indoor Air Quality Monitoring Command Console\n")
            print(" ")
            print("* * * * * * * * * * * * * * * * * * * * * * * *\n")
            print(" ")
            print("Successfully saved reading\n")
            print(" ")
            print("* * * * * * * * * * * * * *")
            print(" \n")
            input("Enter any Key to go to the Main menu\n")

        elif value ==2:
#to tabulate the datas inputted by the user
            print(" \n")
            print(" \n")
            print("Indoor Air Quality Monitoring Command Console\n")
            print(" ")
            print("*********************************************\n")
            print(" ")
            print("LIST \n")
            print(" ")
            print(" ")
            class List_item:
                id = 0
                temp = 0
                pres = 0
                alt = 0
                tvoc = 0
                co2 = 0
                time1 = 0
                def __init__(self,id,temp,pres,alt,tvoc,co2,time1):
                    self.id = id
                    self.temp = temp
                    self.pres = pres
                    self.alt = alt
                    self.tvoc = tvoc
                    self.co2 = co2
                    self.time1 = time1
            List_item1 = List_item(1,temperature[0],pressure[0],altitude[0],tvoc[0],co2[0],time[0])
            List_item2 = List_item(2,temperature[1],pressure[1],altitude[1],tvoc[1],co2[1],time[1])
            List_item3 = List_item(3,temperature[2],pressure[2],altitude[2],tvoc[2],co2[2],time[2])
            print("ID ", "TEMP", "PRES", "ALT", "TVOC ", "C02 ", "TIME")
            print(List_item1.id," ", List_item1.temp, " ", List_item1.pres, " ", List_item1.alt, " ", List_item1.tvoc, " ", List_item1.co2, " ",List_item1.time1)
            print(List_item2.id," ", List_item2.temp, " ", List_item2.pres, " ", List_item2.alt, " ", List_item2.tvoc, " ", List_item2.co2, " ",List_item1.time1)
            print(List_item3.id," ", List_item3.temp, " ", List_item3.pres, " ", List_item3.alt, " ", List_item3.tvoc, " ", List_item3.co2, " ",List_item1.time1)
            print(" ")
            input("Enter any key to go back to Main Menu ")



        elif value == 3:
# To perform various operations by importing the functions from library and display them for Temperature,Humidity,Pressure,TVOC and CO2
            tvoc_arr = tvoc
            co2_arr = co2
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
            print("Max : ",library.statistics.get_max_value(temperature))
            print("Min : ",library.statistics.get_min_value(temperature))
            print("Median :",library.statistics.get_median(temperature))
            print("Mode : ",library.statistics.get_mode(temperature))
            print("Range :",library.statistics.get_range(temperature))
            print("Std : ",library.statistics.get_stdeviation(temperature))
            print("Var : ",library.statistics.get_variance(temperature))
            print(" \n")
            print("HUMIDITY ")
            print(" ")
            print("Unit :  % ")
            print("Air Quality : ",library.humidity.get_humidity_value(humidity))
            print("Max : ",library.statistics.get_max_value(humidity))
            print("Min : ",library.statistics.get_min_value(humidity))
            print("Median :",library.statistics.get_median(humidity))
            print("Mode : ",library.statistics.get_mode(humidity))
            print("Range :",library.statistics.get_range(humidity))
            print("Std : ",library.statistics.get_stdeviation(humidity))
            print("Var : ",library.statistics.get_variance(humidity))
            print(" \n")
            print("PRESSURE ")
            print(" ")
            print("Unit : kPa ")
            print("Max : ",library.statistics.get_max_value(pressure))
            print("Min : ",library.statistics.get_min_value(pressure))
            print("Median :",library.statistics.get_median(pressure))
            print("Mode : ",library.statistics.get_mode(pressure))
            print("Range :",library.statistics.get_range(pressure))
            print("Std : ",library.statistics.get_stdeviation(pressure))
            print("Var : ",library.statistics.get_variance(pressure))
            print(" \n")
            print("ALTITUDE ")
            print(" ")
            print("Unit : ft ")
            print("Max : ",library.statistics.get_max_value(altitude))
            print("Min : ",library.statistics.get_min_value(altitude))
            print("Median :",library.statistics.get_median(altitude))
            print("Mode : ",library.statistics.get_mode(altitude))
            print("Range :",library.statistics.get_range(altitude))
            print("Std : ",library.statistics.get_stdeviation(altitude))
            print("Var : ",library.statistics.get_variance(altitude))
            print(" \n")
            print("TVOC ")
            print(" ")
            print("Unit : ppb ")
            print("Air Quality : ",library.tvoc.get_tvoc_info(tvoc))
            print("Max : ",library.statistics.get_max_value(tvoc))
            print("Min : ",library.statistics.get_min_value(tvoc))
            print("Median :",library.statistics.get_median(tvoc))
            print("Mode : ",library.statistics.get_mode(tvoc))
            print("Range :",library.statistics.get_range(tvoc))
            print("Std : ",library.statistics.get_stdeviation(tvoc))
            print("Var : ",library.statistics.get_variance(tvoc))
            print(" \n")
            print("CO2 ")
            print(" ")
            print("Unit : ppm ")
            print("Air Quality : ",library.co2.check_air_quality(co2))
            print("Max : ",library.statistics.get_max_value(co2))
            print("Min : ",library.statistics.get_min_value(co2))
            print("Median :",library.statistics.get_median(co2))
            print("Mode : ",library.statistics.get_mode(co2))
            print("Range :",library.statistics.get_range(co2))
            print("Std : ",library.statistics.get_stdeviation(co2))
            print("Var : ",library.statistics.get_variance(co2))
            print(" \n")
            os.system('clear')
        elif value == 4:
            main_loop_is_running = False
if __name__ == "__main__":
 main()
