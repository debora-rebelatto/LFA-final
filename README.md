# Construção de aplicação para gerar Automato Finito Determinístico.

## ⚙️ Setup

Primeiro, instale o Python:

```bash
sudo apt-get update
sudo apt-get install python3.6
```

Caso tenha sido instalado corretamente, rode o seguinte comando para verificar qual versão foi instalada:

```bash
python3 --version
```

Para inicializar a aplicação, rode o seguinte comando na raíz do projeto:

```bash
python3 main.py
```

## Descrição

Objetivo:

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

| delta | s   | e   | n   | t   | a   | o   | i   | u   |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| S     | A,H | C,M |     |     | M   | M   | M   | M   |
| A     |     | B   |     |     |     |     |     |     |
| \*B   |     |     |     |     |     |     |     |     |
| C     |     |     | D   |     |     |     |     |     |
| D     |     |     |     | E   |     |     |     |     |
| E     |     |     |     |     | F   |     |     |     |
| F     |     |     |     |     |     | G   |     |     |
| \*G   |     |     |     |     |     |     |     |     |
| H     |     | I   |     |     |     |     |     |     |
| I     |     |     | J   |     |     |     |     |     |
| J     |     |     |     |     | K   |     |     |     |
| K     |     |     |     |     |     | L   |     |     |
| \*L   |     |     |     |     |     |     |     |     |
| \*M   |     | M   |     |     | M   | M   | M   | M   |

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
