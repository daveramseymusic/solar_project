import pandas as pd
import os
import os.path



# name = '/Users/davidramsey/Documents/coding/solar/Oct_Meter_Readings_test/May'

# a_path = '/Users/davidramsey/Documents/jeopardy_starting/coding/solar/Oct_Meter_Readings_test'

import connect_csvs_function
import find_all_column_names_function


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
all_cols = []
new_cols = []

## get list all column names used in all these csvs

#start counter loop for cols list:
counter = 0

for file in file_list:
    #open a specific a specific file from this dir and do you work to each one
    name_of_file = file
    with open(os.path.join(dr_name,file), mode = 'r') as src_file:
        old_cols = find_all_column_names_function.find_col_names(src_file, dr_name, name_of_file, old_cols)
        
        
        #loop through to see if any column names match your columnnames list:
        if counter > 0:
            for col in old_cols:
                if col not in all_cols:
                    # if not in the list then add to empty list
                    new_cols.append(col)
            #add new list to all list
            all_cols.extend(new_cols)
            new_cols = [] #reset new list to be empty

        else:
            all_cols = old_cols
            counter += 1
            
        print(file + str(': columns scraped'))
        
        src_file.close()


print(all_cols)    

old_column_length = 20
## for cleaning and wrangling data
for file in file_list:
    #open a specific a specific file from this dir and do you work to each one
    name_of_file = file
    with open(os.path.join(dr_name,file), mode = 'r') as src_file:
        column_length = connect_csvs_function.clean_solar_data(src_file, dr_name, name_of_file, old_cols, all_cols)
        if column_length != old_column_length:
            print('columns not the same lenght!! !!!!!!')
        old_column_length = column_length            
        print(file + str(' is cleaned and wrangled'))
        
        src_file.close()
    

    