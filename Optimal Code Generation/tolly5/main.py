from parser import cfg
from ssa.ssa import SsaBuilder
import sys

if __name__ == '__main__':
    listener = cfg.create_and_process_tree()
    print(listener)
    blocks = listener.main

    ssab = SsaBuilder(blocks)
    # ssab.insert_all_phi()
    # ssab.update_variable_versions()
    ssab.print_blocks()

    graphname = f'results/prog{sys.argv[1]}.dot'
    with open(graphname, 'w') as f:
        f.write(ssab.to_graph())