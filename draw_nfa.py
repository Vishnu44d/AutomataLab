from graphviz import Digraph
import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

file_name = 'Example-3'
dot = Digraph('finite_state_machine')
dot.attr(rankdir='LR', size='8,5')
dot.format = 'png'


nfa = {
    0: {'a': 1},
    1: {'$': (0, 3)},
    2: {'$': (0, 3)},
    3: {}
}
nfa = {0: {'a': 1}, 1: {'$': 5}, 2: {'b': 3},
       3: {'$': 5}, 4: {'$': (0, 2)}, 5: {}}


nfa = {0: {'a': 1}, 1: {'$': 2}, 2: {'b': 3}, 3: {}}
final = [3]
start = 0


def draw_fa(fa, final, start, file_name="my_first"):
    edges_ls = []
    for n in fa:
        if n in final:
            dot.attr('node', shape='doublecircle')
            dot.node(str(n))
        elif n == start:
            dot.attr('node', shape="Mcircle")
            dot.node(str(n))
        else:
            dot.attr('node', shape="ellipse")
            dot.node(str(n))
    for node in fa:
        if len(fa[node]) == 0:
            pass
        else:
            for symbol in fa[node]:
                try:
                    for s in fa[node][symbol]:
                        edges_ls.append([str(node), str(s), str(symbol)])
                except:
                    edges_ls.append(
                        [str(node), str(fa[node][symbol]), str(symbol)])

    for e in edges_ls:
        dot.edge(e[0], e[1], label=e[2])
    dot.render('output/'+file_name, view=True)


draw_fa(nfa, final, start)
