cd 'C:\\Users\\Vandan\\Documents\\NST 2\\scicomp\\EX1\\st2'

set terminal wxt 0

set xlabel 'x'
set ylabel 'Relative amplitude'
show xlabel
show ylabel
set title "Relative amplitude for varying screen, slit distances for Fresnel Single slit."
plot 'ST2_results.dat' using 1 title 'd = 30' with lines, \
	'ST2_results.dat' using 3 title 'd = 50' with lines, \
	'ST2_results.dat' using 5 title 'd = 100' with lines


set terminal wxt 1

set xlabel 'x'
set ylabel 'Relative phase'
show xlabel
show ylabel
set title "Relative phase for varying screen, slit distances for Fresnel Single slit."

plot 'ST2_results.dat' using 2 title 'd = 30' with lines, \
	'ST2_results.dat' using 4 title 'd = 50' with lines, \
	'ST2_results.dat' using 6 title 'd = 100' with lines
	
