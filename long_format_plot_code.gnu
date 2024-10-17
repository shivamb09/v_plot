gnuplot << EOF
set terminal pngcairo size 800,600;
set output 'vplot_long.png';
set title 'V-Plot: Fragment Length vs Relative Position';
set xlabel 'Relative Position (-500 to +500)';
set ylabel 'Fragment Length (bp)';
set grid;
set palette defined (0 'white', 1 'blue', 2 'green', 3 'yellow', 4 'red');
set cblabel 'Count';
set style data points;  
set xtics -500,250,500;
set ytics autofreq;                               
plot 'final_matrix_long.txt' using 1:2:3 with points palette pointsize 0.3 pointtype 7 notitle;
EOF
