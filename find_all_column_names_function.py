import csv
import pandas as pd
import datetime as dt  #maybe you don't have to import dateitme anymore?
import sys
import re


'''This script is what i'm usin to clean individual csv tabs and reconnect
them once they have been converted to csv from xlsx.'''

# csv_filenames = '/Users/davidramsey/Documents/coding/solar/Oct_Meter_Readings_test/May 2020-Table 1.csv'
# concated_csv_file_base_path = '/Users/davidramsey/Documents/coding/learning folder'

def find_col_names(csv_filenames, concated_csv_file_base_path, name_of_file, old_cols):

    # 1. find what these squares actually have and save it as a variable
    # visits = pd.read_csv('visits.csv', parse_dates=[1])
    csv_file = pd.read_csv(csv_filenames)


    # 2. save all column names as a list using:
    # list = nyt_filtered_san_diego.columns #make save all columns or column names into one list
    cols = csv_file.columns

    # 2.5 clean column names
    cols = cols.str.replace("b'",'').str.replace("'",'').str.replace(" ","_").str.lower().str.replace(r"\n","").str.replace('(','').str.replace(')','')


    
    
    csv_file.columns = cols
    datelike_headers_list = []
    

    for words in cols:
        if 'date' in words:
            datelike_headers_list.append(words)
    
    length_list = len(datelike_headers_list)  #create len of list
    if length_list < 1:
        new_headers = csv_file.iloc[0]
        # 2.5 clean column names
        new_headers = new_headers.str.replace("b'",'').str.replace("'",'').str.replace(" ","_").str.lower().str.replace(r"\n","").str.replace('(','').str.replace(')','')
        csv_file.columns = new_headers
        csv_file = csv_file.iloc[1:]
        csv_file.reset_index(drop=True,inplace=True)
        for words in new_headers:
            if 'date' in words:
                datelike_headers_list.append(words)
    
    old_cols = csv_file.columns
    return list(old_cols)


##at this point all columns are cleaned


    # #make date_like_headers_list singlular instead of a list
    # datelike_header = datelike_headers_list[0]
  
   
    # cols2 = csv_file.columns.drop(datelike_header) #drop datetime column
    
    # #turn all other columns numeric
    # csv_file[cols2] = csv_file[cols2].apply(pd.to_numeric, errors='coerce')


    # #sub all empty elements with NaN
    # nan_value = float("NaN")
    # # df.replace("",nan_value,inplace)
    # csv_file[cols2].replace("", nan_value, inplace=True)



    # #convert all dates in string fromat to datetime format in this column(col) 
    # #then keep date part when using to_datetime - use .date
    # # use pd.to_dateime(df['col],errors='coerce')
    
    # csv_file[datelike_header] = csv_file[datelike_header].apply(pd.to_datetime, format='%m/%d/%y',errors='coerce')
    
    # # csv_file[datelike_header] = csv_file[datelike_header].apply(pd.to_datetime, format='%Y-%m-%d',errors='coerce')
    # if isinstance(csv_file[datelike_header], dt.datetime):
    #         csv_file[datelike_header] = csv_file[datelike_header].dt.date
    

    # # filter out all rows with more than 3 na's
    # csv_file.dropna(thresh=10, inplace=True)
    
    # csv_file.reset_index(drop=True, inplace=True)
    # #filter out all rows that have nothin in the first column:


    # csv_file['period_start_date'] = csv_file[datelike_header].min()
    # csv_file['period_end_date'] = csv_file[datelike_header].max()
    
    
    # #save newly cleaned file under different name
    # cleaned_file = csv_file 

    # #use .to_csv() to save as a csv
    # #data_xls.to_csv('csvfile.csv', encoding='utf-8')
    # cleaned_file.to_csv(str('cln_') + name_of_file, index=False , encoding='utf-8')
    

    # # save cleaned column headers and returnd
    # old_cols = cleaned_file.columns
    # # turn the columns index into a list
    # # old_cols.tolist()




## call the function if your testing this alone
# clean_solar_data(csv_filenames, concated_csv_file_base_path)

if __name__ == '__main__':
    clean_solar_data(csv_filenames = sys.argv[1], concated_csv_file_base_path = sys.argv[2])