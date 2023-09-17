import networkx as nx
from copy import deepcopy
from parser.myBB import *


def df_test():
    G = nx.DiGraph([
            (1,2),(1,5), (1,9), (2,3), (3,3), (3,4),
            (4,13), (5,6), (5,7), (6,8), (6,4), 
            (7,8), (7,12), (9,10), (9,11), (8,13), (3,3),
            (10,12), (11,12), (12,13), (8,5)
        ])
    df = nx.dominance_frontiers(G, 1)
    print(df)


class SsaBuilder:
    def __init__(self, blocks):
        self.blocks = blocks
        self.build_dom()
        self.build_df()
        self.build_changed_variables()

    # КОНСТРУКТОРЫ

    def build_dom(self):
        self.edges = set.union(*[x.get_edges() for x in self.blocks])
        G =  nx.DiGraph(self.edges)
        for x in self.blocks_to_nums(self.blocks):
            G.add_node(x)
        g = G.to_undirected()
        cc = nx.node_connected_component(g, 0)
        self.G = nx.DiGraph(G.subgraph(cc))
        self.blocks = set(filter(lambda x: x.block_num in self.G, self.blocks))

        imm_dom = nx.immediate_dominators(self.G, 0)
        print(imm_dom)
        dom = dict([(x, {imm_dom[x]}) for x in self.G])
        while True:
            old_dom = deepcopy(dom)
            for x, domsx in old_dom.items():
                for y in domsx:
                    dom[x].update(dom[y])
            if old_dom == dom:
                break
        self.dom_of = dom
        
        self.dom_scope = dict([(x, set()) for x in self.G])
        for x, ys in self.dom_of.items():
            for y in ys:
                self.dom_scope[y].add(x)

        # print('x <- dominators', self.dom_of)
        # print('x -> dominates', self.dom_scope)
    
    def build_df2(self):
        self.df =  nx.dominance_frontiers(self.G, 0)
        # print('x -> DF(x):', self.df)

    def build_df(self):
        self.df = dict([(bb, set()) for bb in self.G])
        idom = nx.immediate_dominators(self.G, 0)
        old  = dict()
        while old != self.df:
            old = deepcopy(self.df)
            for x in self.blocks_to_nums(self.blocks):
                for y in self.get_succ(x):
                    if x not in  self.dom_of[y]:
                        self.df[x].add(y)
                children = self.dom_scope[x]
                print(x, '->', children)
                for z in children:
                    for y in self.df[z]:
                        if y not in self.dom_scope[x]:
                            self.df[x].add(y) 
            
        assert self.df ==  nx.dominance_frontiers(self.G, 0)

    def build_changed_variables(self):
        for x in self.blocks:
            x.build_changing_variables()

    # UTILS

    def print_blocks(self):
        for bb in self.blocks:
            print(bb)
        
    def to_graph(self):
        ret = "digraph G{\nnode [shape=box nojustify=false]\n"
        for x in self.blocks:
            s = str(x).replace('    ', '').replace('{', '').replace('}', '').replace("\n", "\\l    ").strip()
            while s[-2: ] == '\\l':
                s = s[:-2].strip()
            ret += f'{x.block_num} [label=\"{s}\"]\n'
            last = x.instructions[-1]
            if last.typ == BR:
                ret += f'{x.block_num} -> {last.args["dest"]}\n'
            elif last.typ == CONDBR:
                ret += f'{x.block_num} -> {last.args["dest1"]} [label=true]\n'
                ret += f'{x.block_num} -> {last.args["dest2"]} [label=false]\n'
        ret += "}\n"
        return ret

    def get_block(self, n):
        return list(filter(lambda x: x.block_num == n, self.blocks))[0]

    def blocks_to_nums(self, s):
        return set(map(lambda bb: bb.block_num, s))

    def nums_to_bloks(self, nums):
        return set(filter(lambda bb: bb.block_num in nums, self.blocks))
    
    def get_all_vars_names(self):
        return set.union(*[set(bb.variables.keys()) for bb in self.blocks])

    def get_preds(self, node):
        if isinstance(node, BB):
            node = node.block_num
        return set(self.G.predecessors(node))

    def get_succ(self, node):
        if isinstance(node, BB):
            node = node.block_num
        return set(self.G.successors(node))

    def find_blocks_that_redefine_var(self, varname):
        s = set()
        for bb in self.blocks:
            for var in bb.changing_variables:
                if var.name == varname:
                    s.add(bb)
                    break
        return s

    # РАЗМЕЩЕНИЕ PHI-ФУНКЦИЙ

    def find_df(self, s):
        ret = set()
        for x in s:
            ret.update(self.df[x])
        return ret

    def find_df_plus(self, s):
        old = set()
        new = self.find_df(s)
        while True:
            old |= new
            new = self.find_df(new)
            if new.difference(old) == set():
                return old
    

    def find_j_plus(self, s):
        return self.find_df_plus(s)


    def insert_phi(self, varname):
        print('==========================')
        print('INSERTING PHI BY VAR', varname)
        S = self.find_blocks_that_redefine_var(varname)
        S_nums = self.blocks_to_nums(S)
        print(varname, 'IS REDEFINED IN S:', S_nums)
        Jplus_nums = self.find_j_plus(S_nums)
        Jplus = self.nums_to_bloks(Jplus_nums)
        print('J+ is', Jplus, 'here we place phi funcs for', varname)
        for bb in Jplus:
            bb.phi_var_blocks[varname] = set()
            JS = Jplus | S
            JS_nums = self.blocks_to_nums(JS)
            for phi_parent in JS:
                G = deepcopy(self.G)
                for rnode in JS_nums.difference({bb.block_num, phi_parent.block_num}):
                    G.remove_node(rnode)
                if (phi_parent.block_num != bb.block_num) and nx.has_path(G, phi_parent.block_num, bb.block_num):
                    bb.phi_var_blocks[varname].add(phi_parent.block_num)

    def insert_all_phi(self):
        all_variables = self.get_all_vars_names()
        for varname in all_variables:
            self.insert_phi(varname)
        
        for bb in self.blocks:
            # print('block', bb.block_num, '--->', bb.phi_var_blocks)
            for varname, phiblocks in bb.phi_var_blocks.items():
                instr = Instruction(PHI, {'to': Variable(varname, 0), 'from':list(phiblocks)})
                bb.instructions.insert(0, instr)
            # print(bb)

    # ОБНОВЛЕНИЕ ВЕРСИЙ ПЕРЕМЕННЫХ

    def update_variable_versions(self):
        self.variable_versions = dict([(x, 0) for x in self.get_all_vars_names()])

        for bb in self.blocks:
            bb.visited = False
        # self.traverse2(self.get_block(0), deepcopy(self.variable_versions))
        # self.upd_phi()
        self.traverse()


    def traverse2(self, bb, last_versions):
        '''
        self.variable_version содержит наименьшие "свободные" версии переменных
        last_versions содержит версии, на которых завершился блок
        '''
        if bb.visited:
            return
        bb.visited = True

        print("IN BLOCK", bb.block_num)
        bb.last_versions = last_versions
        for i, instr in enumerate(bb.instructions):
            print('--------------------')
            print('->', instr)
            for key, val in instr.args.items():
                if not isinstance(val, Variable) or val.is_temp:
                    continue
                name = val.name
                if key == 'to':
                    new_ver = self.variable_versions[name]
                    bb.instructions[i].args['to'] = Variable(name, new_ver)
                    bb.last_versions[name] = new_ver
                    self.variable_versions[name] += 1
                    print('    ', bb.block_num, 'NEW VERSION OF', name, ':', new_ver)
                else:
                    bb.instructions[i].args[key] = Variable(name, bb.last_versions[name])
                    print('    ', bb.block_num, 'SET VERSION TO', name, ':', val.version)
            print('->', instr)
        print(bb.last_versions)

        children = self.get_succ(bb)
        print('FROM', bb.block_num, 'to', children)
        for child_num in children:
            self.traverse2(self.get_block(child_num), deepcopy(bb.last_versions))
    
    def traverse(self):
        for target_var in self.get_all_vars_names():
            self.stack = []
            self.counter = 0
            self.traverse_rec(0, target_var)

    def which_pred(self, v, v1):
        preds = list(self.get_preds(v1))
        print('PREDS OF', v1, 'are', preds)
        preds.sort()
        return preds.index(v)

    def traverse_rec(self, bb, target_var):
        print("->>> IN BLOCK", bb)
        c = 0
        
        for i, instr in enumerate(self.get_block(bb).instructions):
            print('--------------------')
            print('->', instr)
            for key, val in instr.args.items():
                if not isinstance(val, Variable) or val.is_temp or val.name != target_var:
                    continue
                name = val.name
                if key == 'to':
                    new_ver = self.counter
                    self.stack.append(self.counter)
                    self.counter += 1
                    c+=1
                    self.get_block(bb).instructions[i].args['to'] = Variable(name, new_ver)
                    print('    ', bb, 'NEW VERSION OF', name, ':', new_ver)
                if key != 'to' and instr.typ != PHI:
                    self.get_block(bb).instructions[i].args[key] = Variable(name, self.stack[-1])
                    print('    ', self.get_block(bb).block_num, 'SET VERSION TO', name, ':', val.version)
            print('->', instr)


        children = self.get_succ(bb)
        print('FROM', bb, 'to', children)
        for v1 in children:
            j = self.which_pred(bb, v1)
            for instr in self.get_block(v1).instructions:
                if instr.typ != PHI or instr.args['to'].name != target_var:
                    continue
                instr.args['from'][j] = (Variable(target_var, self.stack[-1]))

        for v1 in (self.get_succ(bb)):
            if v1 < bb:
                continue
            self.traverse_rec(v1, target_var)

        for _ in range(c):
            self.stack.pop()

    def upd_phi(self):
        for bb in self.blocks:
            print('--->', bb.block_num)
            for instr in bb.instructions:
                if instr.typ != PHI:
                    continue
                name = instr.args['to'].name
                for i, x in enumerate(instr.args['from']):
                    instr.args['from'][i] = Variable(name, self.get_block(x).last_versions[name])
