cd 'C:\\Users\\Vandan\\Documents\\NST 2\\scicomp'


set logscale x
set xrange [0.3:3000000]
plot 'CT1_results.dat' using 1:2:3 with yerrorbars notitle
set xlabel "Number of values"
show xlabel
set ylabel "Value of integral"

