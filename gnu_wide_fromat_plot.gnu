gnuplot -e "
set terminal pngcairo size 800,600;
set output 'vplot_heatmap_wide_new.png'; 
set title 'V-Plot: Fragment Length vs Relative Position';
set xlabel 'Relative Position (-509 to +509)';
set ylabel 'Fragment Length (bp)';
set grid;
set palette defined (0 'white', 1 'blue', 2 'green', 3 'yellow', 4 'red');  
set cblabel 'Counts';
set pm3d map; 
set xtics (-509, -250, 0, 250, 509); 
set ytics autofreq;  
set style data pm3d;  
unset key; 
splot 'final_matrix_wide_new.txt' matrix with image;
"
