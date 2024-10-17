import sys
len_fragment = list()
range_relative_dist = list()
for line in sys.stdin:
	line = line.strip()
	new_list = line.split(" ")
	range_relative_dist.append(new_list[0])
	len_fragment.append(new_list[1])
len_fragment.sort()
range_relative_dist.sort()
print(len_fragment)
"""
print("longest fragment:",len_fragment[-1])
print("shortest fragment:",len_fragment[0])
print("lowest_range:",range_relative_dist[0])
print("highest_range:",range_relative_dist[-1])
"""

