import json


def jsonLoad(loc):

    """
    Function to read the file and return the fileset from location
    :param loc: location of the file is passed
    :return: dictionary of JSON data
    """

    f = open(loc)
    data = json.load(f)
    f.close()
    return data

    """
    Can use Dask dataframe to read objects if the file or data will be larger than the system memory, keeping things simple here.
    """