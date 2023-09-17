go run main.go $1
# opt -dot-cfg "emlangResults/prog$1.ll"
# rm "emlangResults/prog$1.ll"
# dot -Tjpg .main.dot > "emlangResults/prog$1graph.jpg"
# rm .main.dot
dot -Tjpg emlangResults/prog$1.dot > "emlangResults/prog$1mygraph.jpg"
