import gzip
import numpy as np

def normalize_mid(ctcf_start, ctcf_stop):
    ctcf_mid = (ctcf_start + ctcf_stop) / 2
    return int(ctcf_mid)

def matrix_formation(start, stop, mid):
    relative_start = start - mid
    relative_stop = stop - mid 
    matrix_row = np.zeros(1001, dtype=int) 
    
    for i in range(relative_start, relative_stop + 1):
        if -500 <= i <= 500:
            matrix_row[i + 500] = 1  
    return matrix_row

matrix_dict = {}

with gzip.open("mapped.bed.gz", 'rt') as f:
    for line in f:
        line = line.strip()
        new_list = line.split("\t")
        ctcf_start = int(new_list[2])
        ctcf_stop = int(new_list[3])
        fragment_start = int(new_list[8])
        fragment_stop = int(new_list[9])
        len_fragment = fragment_stop - fragment_start
        
        
        mid = normalize_mid(ctcf_start, ctcf_stop)
        
        
        matrix_row = matrix_formation(fragment_start, fragment_stop, mid)
        
        if len_fragment in matrix_dict:
            matrix_dict[len_fragment] += matrix_row
        else:
            matrix_dict[len_fragment] = matrix_row

sorted_lengths = sorted(matrix_dict.keys())
max_length = len(sorted_lengths)

final_matrix = np.zeros((max_length, 1002), dtype=int) 

for idx, length in enumerate(sorted_lengths):
    final_matrix[idx, 0] = length 
    final_matrix[idx, 1:] = matrix_dict[length]  

np.savetxt("final_matrix.txt", final_matrix, fmt="%d", delimiter="\t")
