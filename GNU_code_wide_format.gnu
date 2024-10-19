gnuplot <<EOF
set terminal pngcairo size 800,600;
set output "v_plot_wide.png";
set xlabel "Relative_position";
set ylabel "Length_fragment";
set xrange [-550:550];
set yrange [40:600];
set title "CTCF Binding relative to DNA fragment size";
set autoscale xfix;
set autoscale yfix;
set autoscale cbfix;
plot "final_matrix_wide.txt" matrix nonuniform with image;
replot;
EOF
