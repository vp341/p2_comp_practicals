cd 'C:\\Users\\Vandan\\Documents\\NST 2\\scicomp\\EX1\\CT1'


set xlabel "1/N^2"
set xrange [0:3e-15]
show xlabel
set ylabel "Standard Deviation of 50 integrals"
show ylabel
set title "Error variation with number of values per integral"
plot 'CT1_results.dat' using (1/($1**2)):3 notitle
