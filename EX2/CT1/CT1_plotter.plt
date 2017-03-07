cd 'C:\\Users\\Vandan\\Documents\\NST 2\\scicomp\\EX2\\ct1'


set terminal wxt 1

set xlabel "Time /s"
show xlabel
set ylabel "Energy Loss / J"
show ylabel
set title "Energy loss against Time for ode solution to simple pendulum"
plot 'CT1_results_1.dat' using 1:2 notitle with lines

set terminal wxt 2

set xlabel "Initial Angular Displacement /rad"
show xlabel
set ylabel "Period /s"
show ylabel
set title "Angle vs Period relationship for simple pendulum"
plot 'CT1_results_2.dat' using 1:2 notitle with lines

