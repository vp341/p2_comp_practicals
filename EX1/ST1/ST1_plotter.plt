cd 'C:\\Users\\Vandan\\Documents\\NST 2\\scicomp\\ex1\\st1'


set xlabel "Difference between Monte Carlo and analytical value"
show xlabel
set ylabel "Standard Deviation of Points"
show ylabel
set title "Comparison of errors for different values of the integral"


plot 'ST1_results.dat' using 1:2 notitle
