import os
import glob
import pandas as pd

#choose the directory



'''Match the pattern (‘csv’) and save the list of file names in the
 ‘all_filenames’ variable. You can check out this link to learn
  more about regular expression matching.'''

extension = 'csv'
csvs_directory = "/solar/Clean_Meter_Readings"

def csv_concatinator(csvs_directory, extension ):

    os.chdir(csvs_directory)
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    #export to csv
    combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
    print(extension + str('files are concatenated'))