from automata import nfa



def nfa2dfa(nfa, sigma, initial, finals):
    dfa = {}
    new_states = [[initial]]
    dfa_finals = []
    for nstates in new_states:
        for symbol in sigma:
            some_state = nfa[nstates[0]][str(symbol)]
            for i in nstates[1:]:
                some_state
            state = nfa[nstates][str(symbol)]
            dfa[nstates] = {symbol: state}
            if state not in new_states:
                new_states.append(state)
    

    print(dfa)


#print(nfa[0]['0'])
nfa2dfa(nfa, [0,1], 0, {1})