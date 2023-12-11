def merge_states(automaton, states):
    final_state = {}
    
    def merge(state):
        for s in state:
            if s in final_state:
                final_state[s] = merge_lists(final_state[s], state[s])
            else:
                final_state.update({s: state[s]})

    for state in states:
        merge(automaton[state])
    
    return final_state


def merge_lists(list1, list2):
    return list1 + list(set(list2) - set(list1))


def merge_automatons(afd, afnd_temp):
    new_state_mapping = {x: x + len(afd) for x in range(len(afnd_temp))}
    
    if '&' in afd[0].keys():
        afd[0]['&'].append(new_state_mapping[0])
    else:
        afd[0].update({'&': [new_state_mapping[0]]})
    
    for key in afnd_temp.keys():
        for ch in afnd_temp[key].keys():
            if ch == '*':
                continue
            new_states = [new_state_mapping[i] for i in afnd_temp[key][ch]]
            afnd_temp[key][ch] = new_states
    
    for key in afnd_temp.keys():
        afd.update({new_state_mapping[key]: afnd_temp[key]})


def display_deterministic_automaton(afnd, alphabet):
    alphabet.sort()
    print('     {}'.format('-----' * len(alphabet)))
    print('     |', end='')
    for i in alphabet:
        print('  {:2}|'.format(i), end='')
    print('\n     {}'.format('-----' * len(alphabet)))
    
    for i in afnd.keys():
        if '*' in afnd[i].keys():
            print('*', end='')
        else:
            print(' ', end='')
        print('{:3}:|'.format(i), end='')
        
        for j in alphabet:
            if j in afnd[i].keys():
                print(' {:2} |'.format(afnd[i][j][0]), end='')
            else:
                print(' {:2} |'.format('-'), end='')
        print('')
    print('     {}'.format('-----' * len(alphabet)))
