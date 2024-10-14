# v_plot

Command to run it on terminal(using shell script and python):

"""

gzip -d filename.bed.gz| python3 main.py > final_marix.txt

"""

to check the working of code at smaller scale:
"""

gzip -d filename.bed.gz

head filename.bed|python3 main.py > check.txt

"""

main_1.py for working with shell and python

main_vplot.py for direct python code

"""
to plot the matrix and save it linux command is 

gnuplot -e "
set terminal pngcairo size 800,600;
set output 'vplot.png';
set title 'V-Plot: Fragment Length vs Relative Position';
set xlabel 'Relative Position (-500 to +500)';
set ylabel 'Fragment Length (bp)';
set grid;              
set palette defined (0 'white', 1 'blue', 2 'green', 3 'yellow', 4 'red');
set cblabel 'Frequency';                                                  
set pm3d map;
splot 'final_matrix_1.txt' matrix using 2:1:3 with image notitle;
set output;
"
"""
