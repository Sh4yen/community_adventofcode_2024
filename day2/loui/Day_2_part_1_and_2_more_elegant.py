import numpy as np
import scipy.ndimage as sp


# read the input file
def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Each line in the file becomes a list of numbers
        # The lists are stored horizontally in a matrix
        # Each line corresponds to a line in the file
        # Each column corresponds to a number in the line
        data = [list(map(int, line.split(" "))) for line in lines]
    return data

data = read_input_file('input.txt')

# In order to easaly accomidate the problem dampener, all of the rules must be aplied element at the same time
# The rules are:
# 1. The row must be in ascending or descending order
# 2. The row must not contain any duplicates
# 3. The absolute difference between any two adjacent elements must be 3 or less

# These rules may be simplefied to:
#   a) The row must be in ascending or descending order
#   b) The absolute difference between any two adjacent elements must be 3 or less and greater than 0

# And simplified further to:
# For the the difference D_i between any two adjacent elements in a line L of lenth i+1 the following must be true:
#                   I)  0 < |D_i| =< 3  
#                   II) sgn(D_i) = Const.

# This is once again the same as saying that the following must be true:
#                   III) all(0 < D_i =< 3) or all(-3 =< D_i < 0)

# So any line (report) that compyls with rule III) is safe, any line that fails is not safe.
# To accomidate the problem dampener, if rule III) fails, we must check if it fails once or more than once.
# One failure of Ruele III) means, that by removing one element, the rule would be satisfied.
# So if a ruele fails, we simply remove each element, one at a time, and check if the rule is satisfied.
# If the rule is satisfied, during any of the removals, it must have only been 1 error.

# Should this semm overwhelming, Day_2_part_1_less_elegant.py is maby easier to understand, but less elegant.

# The following code implements the logic above using only rule III) and the dampening logic:
weight = np.array([1, -1])
safe_reports_with_dampener = 0
safe_reports_without_dampener = 0
for line in data:
    # determine the jump size between adjacent elements D_i and D_(i+1) with convolution (De: Faltung)
    # example: x = convolve1d([2, 1, 3], [1, -1], mode="wrap") -> x = [(-2+1), (-2+3), (-3+2)] = [-1, 2, -1]
    # chop off the last element as the distance between the last and first element is not relevant
    Diffrences = sp.convolve1d(line, weight, mode="wrap")[:-1]
    # does the line comply with rule III)?
    if all(0 < D_i <= 3 for D_i in Diffrences) or all(-3 <= D_i < 0 for D_i in Diffrences):
        # if yes, the report is safe
        safe_reports_with_dampener += 1
        safe_reports_without_dampener += 1
    # if not, does it compy if any one of the elements of the original line is removed
    else:	
        for i in range(len(line)):
            # for each loop, delete a different element
            modified_line = np.delete(line, i)
            # determine jump size as above
            D_i_modified = sp.convolve1d(modified_line, weight, mode="wrap")[:-1]
            # does the line comply with rule III) now
            if all(0 < D_i <= 3 for D_i in D_i_modified) or all(-3 <= D_i < 0 for D_i in D_i_modified):
                safe_reports_with_dampener += 1
                break
            # If not, delete a different element in the next loop
print("1.: ", safe_reports_without_dampener, "Reports are safe without dampener")
print("2.: ",safe_reports_with_dampener, "Reports are safe with dampener")