import numpy as np
import scipy.ndimage as sp

data = np.array([[3, 2, 1], [4, 5, 6], [7, 8, 6]])
a_data =[row for row in data if np.array_equal(row, np.sort(row)[::-1]) or np.array_equal(row, np.sort(row))]
print(a_data)
gewichtung = np.array([-1, 1])

# ascending_data = np.array([sp.convolve1d(row, gewichtung, mode='wrap') for row in ascending_data])
a_data = np.array(sp.convolve1d(a_data, gewichtung, mode='wrap'))
# descending_data_data = np.array([sp.convolve1d(row, gewichtung, mode='wrap') for row in descending_data])
a_data = abs(data[:, :-1])


print(a_data)
print(np.vstack((a_data, gewichtung)))