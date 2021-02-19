def convert_str(s):
    types = {int, float}
    for t in types:
        try:
            return t(s)
        except ValueError:
            pass
    return str(s).strip('\"')

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    res = []
    with open(csv_file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            row = []
            values = line.strip('\n').split(',')
            for val in values:
                row.append(convert_str(val))
            res.append(row)
    return res