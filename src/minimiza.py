from .helpers import *

def eliminarInalcancaveis(afnd):
    visitados = set()

    def eliminar_alcancaveis(rule, state):
        if state in visitados:
            return
        
        visitados.add(state)

        for key in rule.keys():
            if key == '*':
                continue
            for i in rule[key]:
                eliminar_alcancaveis(afnd[i], i)

    eliminar_alcancaveis(afnd[0], 0)
    unreachable_states = set(afnd.keys()) - visitados
    for state in unreachable_states:
        del afnd[state]

def eliminarInuteis(afnd):
    visited = set()
    useful = set()
    
    for rule in afnd:
        if '*' in afnd[rule].keys():
            useful.add(rule)
    
    def find_useful(rule, rule_index):
        if rule_index in useful:
            return True
        
        visited.add(rule_index)
        
        for key in rule.keys():
            for r in rule[key]:
                if r not in visited:
                    if find_useful(afnd[r], r):
                        return True
        return False

    all_rules = list(afnd.keys())

    for rule_index in all_rules:
        if find_useful(afnd[rule_index], rule_index):
            useful.add(rule_index)
        visited = set()
    
    unused_states = set(all_rules) - useful
    for state in unused_states:
        del afnd[state]
    
    for rule_index in afnd.keys():
        keys_to_delete = []
        for key in afnd[rule_index].keys():
            if key == '*':
                continue
            
            afnd[rule_index][key] = [r for r in afnd[rule_index][key] if r in useful]
            if not afnd[rule_index][key]:
                keys_to_delete.append(key)
        
        for key in keys_to_delete:
            del afnd[rule_index][key]
