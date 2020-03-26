def analyze_data(seq):
    """ Takes a list of readings from sensors, seq, and returns a dictionary
    with the sensor name as key and min, max and amount of readings as
    values in a list """
    for elem in seq:
        res_dict = {elem[0]: [elem[1]] for x in seq}
    return res_dict


def merge_r(seq1, seq2):
    res = []

