cd 'C:\\Users\\Vandan\\Documents\\NST 2\\scicomp\\EX1\\CT1'


set xlabel "Number of values per integral"
show xlabel
set ylabel "Standard Deviation of 50 integrals"
show ylabel
plot 'CT1_results.dat' using 1:(1/sqrt($3)) notitle
