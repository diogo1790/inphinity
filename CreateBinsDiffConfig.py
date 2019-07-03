import pandas as pd
import numpy as np

def createVectorScores(line_bins:list, start_zero:bool):
    """
    Create list of values from bins frequencies list. give only a list with the frequencies. The method assumes that the first position correspond the score 0. If start_zero is False, the score zero wasn't considered.

    :param line_bins: list of frequencies
    :param start_zero: to know if the score 0 is considered or not

    :type line_bins: int 
    :type start_zero: int 


    :return: array with the proteins ids
    :rtype: array[int]

    """
    bins_value = 0
    n_repeats = 0
    list_Values = []
    if start_zero == False:
        bins_value = 1
        line_bins.pop(0)

    for n_repeat in line_bins:
        array_bins_aux = np.repeat(bins_value, n_repeat)
        list_Values = np.append(list_Values, array_bins_aux)
        bins_value +=1

    list_Values = list_Values.astype(int)
    return list_Values

def countNumberofScores(list_frequencys:list):
    """
    count the number of scores (not the sum of them but the quantity)

    :param list_frequencys: list of frequencies

    :type line_bins: list(1,4,3,...)


    :return: quantity of elements
    :rtype: int

    """

    list_without_zeros = [element for element in list_frequencys if element != 0]
    qty_elements = np.sum(list_without_zeros)
    return qty_elements


def createVecSizeOfBins(max_score:int, size_bins:int):
    """
    calculate teh vector of bins used in case you want a specific size of bins

    :param max_score: highest score that you can have in the bin
    :param size_bins: size of the bins

    :type max_score: int
    :type size_bins: int


    :return: quantity of elements
    :rtype: int

    """
    array_bins_config = np.arange(0, max_score, size_bins)
    if max_score % size_bins != 0:
        array_bins_config = np.concatenate(array_bins_config, max_score)
    return array_bins_config

def createHeaderBinsSize(vec_histo_values:np.array):
    """
    create the header for the dataset with the size of bins 

    :param vec_histo_values: vec with the intervals of each bins

    :type vec_histo_values: numPy array

    :return: vec with the labels
    :rtype: int

    """
    vec_designation = ['interaction_ID']
    element_start = vec_histo_values[0]
    element_end = vec_histo_values[1]
    for element in vec_histo_values[1:]:
        bins_interval_start = float("{0:.3f}".format(element_start))
        bins_interval_end = float("{0:.3f}".format(element_end))

        string_bin_designation = 'bin_' + str(bins_interval_start) + '_' + str(bins_interval_end)
        element_start = element_end
        element_end = element
        vec_designation.append(string_bin_designation)
    vec_designation.append('label')
    return vec_designation

def createHeaderBinsNumber(number_of_bins:int):
    """
    create the header for the dataset with the number of bins

    :param number_of_bins: number of bins

    :type number_of_bins: int

    :return: vec with the labels
    :rtype: int

    """
    vec_designation = ['interaction_ID']
    aux = 0
    while aux < number_of_bins:
        string_designation_bins = 'bins_' + str(aux)
        vec_designation.append(string_designation_bins)
        aux += 1
    vec_designation.append('label')
    return vec_designation

path_csv = 'bins_base_573_SB1_ZERO.csv'

dataframe_csv_base = pd.read_csv(filepath_or_buffer=path_csv, delimiter=';')
print(dataframe_csv_base)

list_values = []
number_of_bins = 10

dataframe_bins_data = pd.DataFrame()
dataframe_bins_bins_values = pd.DataFrame()

for index, row in dataframe_csv_base.iterrows():
    id_interaction = row.Interaction_ID
    label_value = row.Label
    list_values = row.values.tolist()
    list_values.pop(0)
    list_values.pop()
    list_frequencies_hist = createVectorScores(list_values, True)
    qty_elements = countNumberofScores(list_values)
    qty_scores = len(list_frequencies_hist)
    assert qty_scores == qty_elements

    vec_histo_size = createVecSizeOfBins(573, 10)
    histogram_vec = np.histogram(list_frequencies_hist, bins = vec_histo_size)
    vec_labels = createHeaderBinsSize(histogram_vec[1])
    


    histogram_vec = np.histogram(list_frequencies_hist, bins = number_of_bins)
    vec_labels_b = createHeaderBinsNumber(number_of_bins)
    


    print(histogram_vec)

