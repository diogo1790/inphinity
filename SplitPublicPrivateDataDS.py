"""
This script is used to separate a dataset which contains public and private data into two:
- One that only contains public couples
- Second that only contains private couples (Greg)

To perform this it is necessary to give the ids of the public couples.

"""


import pandas as pd
from os import listdir

def loadPublicIds(file_name:str):

    dataframe_public_ids = pd.read_csv(filepath_or_buffer=file_name, delimiter=',')

    return dataframe_public_ids


def loadDataSet(file_name:str):

    dataframe_dataset = pd.read_csv(filepath_or_buffer=file_name, delimiter=',')

    return dataframe_dataset


def splitDataframePublicPrivate(dataframe_dataset:pd.DataFrame, list_public_ids:list):
    dataframe_public = dataframe_dataset[dataframe_dataset['interaction_ID'].isin(list_public_ids)]
    dataframe_private = dataframe_dataset[~dataframe_dataset['interaction_ID'].isin(list_public_ids)]

    return dataframe_public, dataframe_private

def saveDataframeToCSV(dataframe_dataset:pd.DataFrame, csv_file_name:str):
    dataframe_dataset.to_csv(path_or_buf = csv_file_name, sep =',', index=False)



def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]


#Load public ids
file_name_id_public_couple = "CSV_files\public_couples.csv"
dataframe_public_couples = loadPublicIds(file_name_id_public_couple)
list_public_ids = dataframe_public_couples.Id_couple.tolist()

#Load the names of CSV files
path_csv_files = "CSV_dataset"
list_csvs = find_csv_filenames(path_csv_files)


path_splited_dataset = "CSV_dataset_treated"

for name_file in list_csvs:

    complete_path_dataset = path_csv_files + "\\" + name_file
    dataframe_dataset = loadDataSet(complete_path_dataset)
    public_data, private_data = splitDataframePublicPrivate(dataframe_dataset, list_public_ids)
    public_csv_name = name_file[:-4] + '_public.csv'
    private_csv_name = name_file[:-4] + '_private.csv'

    public_path_csv = path_splited_dataset + '\\' + public_csv_name
    private_path_csv = path_splited_dataset + '\\' + private_csv_name

    saveDataframeToCSV(public_data, public_path_csv)
    saveDataframeToCSV(private_data, private_path_csv)

    print('Hello')




dataset_file_name = r"CSV_dataset\NB_100.csv"
dataframe_dataset = loadDataSet(dataset_file_name)

public_data, private_data = splitDataframePublicPrivate(dataframe_dataset, list_public_ids)

public_dataset_csv_name = 'NB_100_public.csv'

saveDataframeToCSV(public_data, public_dataset_csv_name)

print(dataframe_public_couples)