import pandas as pd
import os
import os.path



# name = '/Users/davidramsey/Documents/coding/solar/Oct_Meter_Readings_test/May'

# a_path = '/Users/davidramsey/Documents/jeopardy_starting/coding/solar/Oct_Meter_Readings_test'

import connect_csvs_function



# file_list = os.listdir("jsons")
# for file_name in file_list:
#     with open(os.path.join("jsons", file_name), "r") as src_file:
#         data = src_file.read()
#         print(data)

dr_name = '/Users/davidramsey/documents/coding/solar/Oct_Meter_Readings_test'

#write new directory name:
# new_dr_name = dr_name + str('_new')
file_list = os.listdir(dr_name)



old_cols = []
col_diff = []
csv_count = 1

##  Left off Thursday: how can I compare the colums to make sure they match?
#mostly, how can I keep the variable old_cols moving throug the for loop.



for file in file_list:
    #open a specific a specific file from this dir and do you work to each one
    name_of_file = file
    with open(os.path.join(dr_name,file), mode = 'r') as src_file:
        old_cols = connect_csvs_function.clean_solar_data(src_file, dr_name, name_of_file, old_cols, col_diff, csv_count )

        print(file)
        src_file.close()
        csv_count += 1
    
    
    #clean the file up by running your solar_data_cleaner
    #close the file 
    #append it to the last file


# without_extra_slash = os.path.normpath(a_path)

# print(a_path)
# last_part = os.path.basename(without_extra_slash)

# print(last_part)