import numpy as np

column1 = []
column2 = []

with open('input.txt', 'r') as file:
    for line in file:
        parts = line.split('   ')  # Split by triple space
        if len(parts) == 2:
            column1.append(float(parts[0].strip()))
            column2.append(float(parts[1].strip()))

column1 = np.array(column1)
column2 = np.array(column2)

column1 = np.sort(column1)
column2 = np.sort(column2)


dif = abs(column1- column2)

dif = sum(dif)

print(dif)


sum = 0
for number in column1:
    count = np.count_nonzero(column2 == number)
    sum += number *count

print(sum)