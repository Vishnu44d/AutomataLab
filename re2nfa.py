from graphviz import Digraph
import os
import re

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


class Conversion:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
        self.output = []
        self.precedence = {'*': 3, '|': 1, '.': 2}

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    def push(self, op):
        self.top += 1
        self.array.append(op)

    def isOperand(self, ch):
        return ch.isalpha()

    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    def infixToPostfix(self, exp):
        for i in exp:
            if self.isOperand(i):
                self.output.append(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                while((not self.isEmpty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
        while not self.isEmpty():
            self.output.append(self.pop())
        res = "".join(self.output)
        # print(res)
        return res


def re2nfa(regex):
    sigma = list(set(re.sub('[^A-Za-z0-9]+', '', regex)+'$'))
    delta = []
    stack = []
    initial = 0
    final = 1
    initial_state = -1
    operand1_count = 0
    operand2_count = 0
    for i in regex:
        if i in sigma:
            initial_state = initial_state+1
            operand1_count = initial_state
            initial_state = initial_state+1
            operand2_count = initial_state
            delta.append({})
            delta.append({})
            stack.append([operand1_count, operand2_count])
            delta[operand1_count][i] = (operand2_count)
        elif i == '*':
            nfa1, nfa2 = stack.pop()
            initial_state = initial_state+1
            operand1_count = initial_state
            initial_state = initial_state+1
            operand2_count = initial_state
            delta.append({})
            delta.append({})
            stack.append([operand1_count, operand2_count])
            delta[nfa2]['$'] = (nfa1, operand2_count)
            delta[operand1_count]['$'] = (nfa1, operand2_count)
            if initial == nfa1:
                initial = operand1_count
            if final == nfa2:
                final = operand2_count
        elif i == '.':
            nfa11, nfa12 = stack.pop()
            nfa21, nfa22 = stack.pop()
            stack.append([nfa21, nfa12])
            delta[nfa22]['$'] = (nfa11)
            if initial == nfa11:
                initial = nfa21
            if final == nfa22:
                final = nfa12
        else:
            initial_state = initial_state+1
            operand1_count = initial_state
            initial_state = initial_state+1
            operand2_count = initial_state
            delta.append({})
            delta.append({})
            nfa11, nfa12 = stack.pop()
            nfa21, nfa22 = stack.pop()
            stack.append([operand1_count, operand2_count])
            delta[operand1_count]['$'] = (nfa21, nfa11)
            delta[nfa12]['$'] = operand2_count
            delta[nfa22]['$'] = operand2_count
            if initial == nfa11 or initial == nfa21:
                initial = operand1_count
            if final == nfa22 or final == nfa12:
                final = operand2_count
    return delta, initial, final, sigma


def print_table(d):
    for i in d:
        print(i, '\t', d[i])


def nfa_match(delta, initial, final, st):
    curr_states = delta[initial][st[0]]
    for symbol in st:
        next_sates = set()
        for curr_state in curr_states:
            for next_sate in delta[curr_state][symbol]:
                next_sates |= set(delta[next_sate][symbol])
            curr_states = next_sates
    for i in curr_states:
        if i in final:
            return True
    return False


def eps_closer(nfa, node_set):
    something_very_different = []
    try:
        for node in node_set:
            print(node)
            for s in nfa[node]:
                if s == '$':
                    cl = nfa[node][s]
                    something_very_different += [cl]
                    eps_closer(nfa, cl)
                else:
                    pass

    except:
        pass


def nfa2dfa(nfa, initial, final, sigma):
    eps_closer(nfa, initial)  # set of states


def draw_fa(fa, final, start, file_name="my_first"):
    dot = Digraph('finite_state_machine')
    dot.attr(rankdir='LR', size='8,5')
    dot.format = 'png'
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
        dot.node(str(node), str(node))
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
    dot.view()
    isSave = input("Do you want to save this[Y/N] ")
    if isSave == 'Y':
        f_name = input("Enter the file name to save the nfa in png ")
        dot.render('output/'+f_name, view=True)
        print("File saved at output/"+f_name+'.png')


def driver(exp, input_string):
    print("given expression", exp)
    result = {}
    p = Conversion(len(exp))
    postfixRe = p.infixToPostfix(exp)
    print("postfix expression", postfixRe)
    delta, initial, final, sigma = re2nfa(postfixRe)
    for i in range(len(delta)):
        result[i] = delta[i]
    #print("transion table")
    print_table(result)
    print(result)
    print("Initial state ", initial)
    print("Final state ", final)
    #f_name = input("Enter the file name to save the nfa in png ")
    draw_fa(result, [final], initial)
    #print(nfa_match(result, initial, {final}, input_string))
    #print(eps_closer(result, {1}))


print("Supproted operations are (|), (.), (*) ( $ is symbol for epsilon)")
exp = input("Enter the regular expression: ")
driver(exp, 'aaa')


test_nfa = {
    0: {'$': (1, 2)},
    1: {'$': (0)},
    2: {'a': 0},
    3: {'b': 1}
}
#print("before call", something_very_different)
# eps_closer(test_nfa,{0})
#print("after call", something_very_different)
