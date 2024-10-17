len_fragment = list()
range_relative_dist = list()
with open("final_matrix.txt") as file:
    for line in  file:
    	new_list = line.split(" ")
    	range_relative_dist.append(int(new_list[0]))
    	len_fragment.append(int(new_list[1]))
len_fragment.sort()
range_relative_dist.sort()
print("longest fragment:",len_fragment[-1])
print("shortest fragment:",len_fragment[0])
print("lowest_range:",range_relative_dist[0])
print("highest_range:",range_relative_dist[-1])
