import numpy as np

# Function to read the content of input.txt and convert it to a list of lists
def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        data = [list(map(int, line.split())) for line in lines]
    return data

data = np.array(read_input_file('input.txt'))

