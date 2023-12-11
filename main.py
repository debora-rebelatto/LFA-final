from src.afnd import *
from src.minimiza import *
from src.determiniza import *
from src.helpers import *

def process_input_file(file_path):
    with open(file_path, "r") as entrada:
        entrada_string = entrada.read()
        entrada_lista = entrada_string.split('\n')
    
    afd = {}
    alfabeto = []
    gramatica = []

    lista_auxiliar = entrada_lista.copy()

    for token_lido in lista_auxiliar:
        if not token_lido:
            entrada_lista.remove(token_lido)
            break
        gerarAfndToken(afd, token_lido, alfabeto)
        entrada_lista.remove(token_lido)

    lista_auxiliar = entrada_lista.copy()

    while entrada_lista:
        for regra_gramatica_lida in lista_auxiliar:
            if not regra_gramatica_lida:
                gerarAfndGramatica(afd, gramatica, alfabeto)
                gramatica.clear()
                entrada_lista.remove(regra_gramatica_lida)
            else:
                gramatica.append(regra_gramatica_lida)
                entrada_lista.remove(regra_gramatica_lida)

    eliminarEpsilonTransicoes(afd)
    determinizar(afd)
    
    print('Automato finito deterministico:')
    exibirAutomatoDeterministico(afd, alfabeto)
    
    eliminarInalcancaveis(afd)
    print('\n Após eliminar inalcançáveis:')
    exibirAutomatoDeterministico(afd, alfabeto)
    
    eliminarInuteis(afd)
    print('\n Após eliminar inúteis:')
    exibirAutomatoDeterministico(afd, alfabeto)

input_file_path = "entrada.txt"
process_input_file(input_file_path)
