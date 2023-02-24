# Descrição do PROJETO:
## UNIVERSIDADE FEDERAL DA FRONTEIRA SUL
## CIÊNCIA DA COMPUTAÇÃO - Campus Chapecó CCR: Linguagens Formais e Autômatos
## Construção de aplicação para gerar Automato Finito Determinístico.

Data limite de apresentação regular: até a penúltima semana letiva de aula.

Na última semana é permitida a apresentação, com correções, para recuperação de rendimento.

Objetivo:

class State {
  constructor(label, isAccepting) {
    this.label = label;
    this.isAccepting = isAccepting;
    this.transitions = new Map();
  }

  addTransition(symbol, state) {
    if (!this.transitions.has(symbol)) {
      this.transitions.set(symbol, []);
    }
    this.transitions.get(symbol).push(state);
  }

  getTransitions(symbol) {
    return this.transitions.get(symbol) || [];
  }
}

class Automaton {
  constructor() {
    this.states = [];
    this.startState = null;
  }

  addState(state) {
    this.states.push(state);
  }

  setStartState(state) {
    this.startState = state;
  }

  minimize() {
    const partition = this.partitionStates();
    const stateClasses = [];
    for (const classStates of partition) {
      const representative = classStates[0];
      const stateClass = new State(representative.label, representative.isAccepting);
      stateClasses.push(stateClass);
      if (representative === this.startState) {
        this.startState = stateClass;
      }
    }
    for (const classStates of partition) {
      const representative = classStates[0];
      const stateClass = stateClasses.find(s => s.label === representative.label);
      for (const [symbol, transitions] of representative.transitions) {
        const targetState = transitions[0];
        const targetClass = stateClasses.find(s => s.label === targetState.label);
        stateClass.addTransition(symbol, targetClass);
      }
    }
    this.states = stateClasses;
  }

  partitionStates() {
    const acceptingStates = this.states.filter(s => s.isAccepting);
    const nonAcceptingStates = this.states.filter(s => !s.isAccepting);
    let partitions = [acceptingStates, nonAcceptingStates];
    while (true) {
      let newPartitions = [];
      let hasChanges = false;
      for (const partition of partitions) {
        if (partition.length < 2) {
          newPartitions.push(partition);
          continue;
        }
        const firstState = partition[0];
        const equivalenceClasses = [[firstState]];
        for (let i = 1; i < partition.length; i++) {
          const state = partition[i];
          let addedToClass = false;
          for (const eqClass of equivalenceClasses) {
            const eqState = eqClass[0];
            if (this.statesAreEquivalent(state, eqState, partitions)) {
              eqClass.push(state);
              addedToClass = true;
              break;
            }
          }
          if (!addedToClass) {
            equivalenceClasses.push([state]);
          }
        }
        if (equivalenceClasses.length === 1) {
          newPartitions.push(partition);
        } else {
          hasChanges = true;
          newPartitions = newPartitions.concat(equivalenceClasses);
        }
      }
      if (!hasChanges) {
        return partitions;
      }
      partitions = newPartitions;
    }
  }

  statesAreEquivalent(state1, state2, partitions) {
    for (const symbol of this.getAlphabet()) {
      const state1Targets = state1.getTransitions(symbol);
      const state2Targets = state2.getTransitions(symbol);
      const targetPartition1 = partitions.find(p => state1Targets.every(s => p.includes(s)));
      const targetPartition2 = partitions.find(p => state2Targets.every(s => p.includes(s)));
      if (targetPartition1 !== targetPartition2) {
        return false;
      }
    }
Saída: Automato Finito Determinístico (AFD), livre de épsilon transições, e mínimo sem a aplicação de classes de equivalência entre estados.

Descrição:
A aplicação realiza a carga de tokens (palavras reservadas, operadores, símbolos especiais, ...) e Gramáticas Regulares (GR) a partir de um arquivo fonte (texto), gerando o AFND.
Por exemplo, se o arquivo de entrada tem as seguintes informações:

se  
entao  
senao  

```
<S> ::= a<A> | <A> | <A> | o<A> | <A>
<A> ::= a<A> |
<A> | i<A> | o<A> | u<A> | ɛ
```

Então, a ação de carga destas informações gera o AFND ilustrado na tabela a seguir.



Neste AF exemplo, os estados finais e respectivos tokens são:

B: se  
G: entao  
L: senao  
M: variavel  

No arquivo de carga, usar notação BNF para as Grs.

Para cada token e gramática, a aplicação gera o conjunto de transições rotuladas em um único AF durante o procedimento de carga. No AF, apenas o estado inicial é compartilhado entre diferentes tokens/gramáricas. Os demais estados são exclusivos para as transições dos demais símbolos dos tokens e/ou estados das GRS.

O AF será indeterminístico quando ocorrer uma ou mais situações em que dois tokens ou sentenças definidas por GR iniciam pelo mesmo símbolo.

**Determinização:**
Aplicar o teorema de determinização para obter o AFD.
Minimização:

O AFD resultante deve ser submetido ao processo de minimização, contudo, sem aplicar Classe de Equivalência. No AFD final os estados podem ser representados por números. Os símbolos podem ser representados pelo correspondente numérico de acordo com a tabela ASCII.

**Estado de erro:**
Ao final da minimização, acrescentar um último estado final. Este será o estado de erro. Todas as células da tabela de transição (AFD) não mapeadas devem ser ajustadas para levar (transição) ao estado de erro. Todas as transições a partir do estado de erro permanecem no estado de erro.

**Entrega (até penúltima semana letiva de aula):**
- Código fonte da aplicação
- Relatório, em formato de artigo, contendo: identificação autores, resumo, introdução, referencial teórico básico (conceitos essenciais para compreensão do trabalho e trabalhos correlatos),
especificação e implementação da solução para gerar AFDs, conclusão e referencial bibliográfico. -upload no moodle em arquivo único antes da apresentação
- a penúltima semana letiva de aula é a data limite, não a data de apresentação. O trabalho pode ser apresentado assim que estiver pronto no decorrer do semestre.

**Apresentação e avaliação:**
- Trabalho individual ou em duplas
- Aplicação em funcionamento: 50% da nota
- Apresentação (demonstração da aplicação e arguição): 50% da nota
- Resultados mínimos para que o trabalho possa ser apresentado: composição do AFND,
determinização e relatório no formato de artigo.
- Qualidade da solução, requisitos contemplados, domínio do processo de especificação e implantação da aplicação, teor/clareza/conteúdo do artigo são os principais referenciais para composição da nota.

Avaliação:  
AFD: 9,0  
Eliminar inalcançáveis e mortos (minimização): 1,0