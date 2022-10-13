echo "" > results.txt
for num in 1 2 4 8 16
do 
    mpiexec -n $num --oversubscribe python lab2_sla\(v\)e.py $num >> results.txt
done 