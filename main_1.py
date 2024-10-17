import numpy as np
import sys
from collections import defaultdict 

values = defaultdict(int)

def interval(start, stop):
    mid = (start + stop) / 2
    return int(mid)

for line in sys.stdin:
        line = line.strip()
        new_list = line.split("\t")
        ctcf_start = int(new_list[2])
        ctcf_stop = int(new_list[3])
        fragment_start = int(new_list[8])
        fragment_stop = int(new_list[9])
        len_fragment = int(new_list[11])
        
        
        mid_ctcf = interval(ctcf_start, ctcf_stop)
        mid_fragment = interval(fragment_start,fragment_stop)
        relative_distance = round(mid_fragment - mid_ctcf)
        
        
        values[(relative_distance,len_fragment)] += 1
        
def matrix_formation(dict_1,output_file):
    with open(output_file,'w') as file:
        for (relative_distance,len_fragment),count in dict_1.items():
            file.write(f"{relative_distance} {len_fragment} {count} \n")

matrix_formation(values,"final_matrix.txt")
