from re import findall as find, match, split #biblioteca de expressões regulares
from .helpers import *

from re import findall as find

def gerarAfndToken(afnd, token, alfabeto):
    if not afnd:
        afnd[0] = {}  # Creating the initial state of AFND if it doesn't exist

    tokenInicial = True  # Flag to identify the first character
    
    for tk in token:
        if tk not in alfabeto:
            alfabeto.append(tk)  # Adding the token character to the alphabet if not present
            
        if tokenInicial:
            state = afnd[0]  # Pointer to the initial state

            if tk in state.keys():
                state[tk].append(len(afnd))  # Adding a transition to a new state if a rule already exists
            else:
                state.update({tk: [len(afnd)]})
            tokenInicial = False
        else:
            afnd[len(afnd)] = {tk: [len(afnd) + 1]}  # Creating a new state to transition to the next character
            
    afnd[len(afnd)] = {'*': [1]}  # Final state when reaching the end of the token


def gerarAfndGramatica(afnd, gramatica, alfabeto):
    if not afnd:
        afnd[0] = {}  # Creating the initial state of AFND if it doesn't exist
    
    afndTemporario = {}
    mapaRegras = {}
    
    for regra in gramatica:
        symbols = find(r'(\w*<\w+>|\w+|&)', regra)  # Separating rule and productions
        
        # Identifying or creating a rule in the temporary automaton
        if symbols[0] in mapaRegras:
            rule_index = mapaRegras[symbols[0]]
        else:
            rule_index = len(afndTemporario)
            afndTemporario[rule_index] = {}
            mapaRegras[symbols[0]] = rule_index
        
        for symbol in symbols[1:]:
            terminal = find(r'^\w+', symbol)
            non_terminal = find(r'<\w+>', symbol)
            terminal = '&' if not terminal else terminal[0]

            if terminal not in alfabeto:
                alfabeto.append(terminal)
            
            if not non_terminal:
                state = afndTemporario[rule_index]

                if terminal in state:
                    state[terminal].append(len(afndTemporario))
                else:
                    state.update({terminal: [len(afndTemporario)]})
                
                afndTemporario[len(afndTemporario)] = {'*': [1]}
            else:
                non_terminal = non_terminal[0]

                if non_terminal in mapaRegras:
                    state = mapaRegras[non_terminal]
                else:
                    state = len(afndTemporario)
                    mapaRegras[non_terminal] = state
                    afndTemporario[state] = {}

                pointer = afndTemporario[rule_index]

                if terminal in pointer:
                    pointer[terminal].append(state)
                else:
                    pointer.update({terminal: [state]})

    unirAutomatos(afnd, afndTemporario)
