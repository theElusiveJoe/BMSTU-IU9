python main.py $1
dot -Tjpg results/prog$1.dot > "results/graph$1.jpg"
# rm results/prog$1.dot
