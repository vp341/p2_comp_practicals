cd 'C:\\Users\\Vandan\\Documents\\NST 2\\scicomp\\EX2'


set terminal wxt 1

set xlabel "Time /s"
show xlabel
set ylabel "Energy Loss / J"
show ylabel
plot 'CT1_results_1.dat' using 1:2 notitle with lines

set terminal wxt 2

set xlabel "Initial Angular Displacement /rad"
show xlabel
set ylabel "Period /s"
show ylabel
plot 'CT1_results_2.dat' using 1:2 notitle with lines

