dfa = {
    0: {'0': 0, '1': 1},
    1: {'0': 2, '1': 0},
    2: {'0': 1, '1': 2}
}


def dfa_match(delta, initial, final, st):
    curr_state = initial
    for symbol in st:
        curr_state = delta[curr_state][symbol]
    if curr_state in final:
        return True
    return False

nfa = {
    0: {'0': [1,0], '1': [1]},
    1: {'0': [2], '1': [0]},
    2: {'0': [1], '1': [2]},
}

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

if __name__ == "__main__":
    print(nfa_match(nfa, 0, {1}, '1010'))
    print(dfa_match(dfa,0,{0},'101'))
