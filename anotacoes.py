"""
Area Para anotacoes do Curso de Python da Geek University

Aula 1 - Recebendo dados do Usuario

# Para inprimir dados que estao em uma variavel e necessario utilizar %s, e apartir de duas variaveis e necessario inclui-las dentro de um parentese. (metodo antigo de printar informacoes)
Exemplo:
# Entrada de Dados do Sistema:
print("Favor Informar Seu Nome!")
nome = input()

print('Seja Bem-Vindo %s, informe sua idade' % nome)
idade = input()

# Saida dos Dados:
print('O %s Tem %s anos!' % (nome, idade))

---------------------------------------------------------------------------------------

# Para imprir dados que estao em uma variavel e necessario utulizar {numeroDaOrdem} no local aonde a variavel precisa aparecer, e .format(variavel) para informar qual variavel precisa ser formatada, a ordem corresponde a ordem que colocamos as variaveis dentro do print (metodo mais moderno)
Exemplo:
# Entrada de Dados do Sistema:
print("Favor Informar Seu Nome!")
nome = input()

print('Seja Bem-Vindo {0}, informe sua idade' .format(nome))
idade = input()

# Saida dos Dados:
print('O {0} Tem {1} anos!'.format(nome, idade))

---------------------------------------------------------------------------------------

# Para imprir dados que estao em uma variavel e necessario utulizar f'Texto {NomeDaVariavel}' no local aonde a variavel precisa aparecer(metodo mais moderno Ainda)
Exemplo:
# Entrada de Dados do Sistema:
print(f"Favor Informar Seu Nome!")
nome = input()

print(f'Seja Bem-Vindo {nome}, informe sua idade')
idade = input()

# Saida dos Dados:
print(f'O {nome} Tem {idade} anos!')

---------------------------------------------------------------------------------------

# Por padrao todo dado recebido por input sera reconhecido como String

Exemplos da Aula:

# Entrada de Dados do Sistema:
nome = input('Qual Seu nome: ')
idade = input('Informe sua idade: ')

# Saida dos Dados:
print(f'O {nome} Ribeiro Prestes da Silva Tem {idade} anos! E Nasceu no ano de {2021 - int(idade)}')


"""
#######################################################################################
""" 
Obs: O underline pode ser utilizado para separar as centenas
    Exemplo: 1_000_000_000

Obs: Pelo fato do Python ser uma linguagem de tipagem dinamica, nao precisamos colocar o tipo da variavel ao declara-la. O tipo e declarado ao atribuirmos o valor a variavel.

Aula 2 Variaveis e tipo de dados.
# Modulo tipo numerico
    soma : 1 + 1
    subtracao : 1 - 1
    multiplicacao : 1 * 1
    divisao : 1 /1
    divisao com resultadado de inteiro : 1 // 1 
    divisao para saber o resto da operacao : 1 % 1 
    potencia : 1 ** 1 

# Modulo tipo float. Float e um tipo dado para os numeros reais
    Exemplo:
        1.5
        2.3 

# Modulo tipo booleano. Boleano e um tipo de dado que consiste em duas constantes sendo elas verdadeiro ou falso, O valor sempre tem que ser descrito com a primeira letra maiuscula.
    Exemplo:
        True -> Verdadeiro
        False -> Falso

        # Operacoes basicas

            # NOT e uma operacao binaria, que inverte o resultado do valor recebido, se o valor for verdadeiro o resultado sera falso, e se o valor for falso o resultado sera verdadeiro
            ou seja sempre o valor sera ao contrario. 
            
            # Dentro do (not) e possivel negar a negacao dele com o (not) antes:
                Exemplo:
                    status = True

                    if status == True:
                        ativo = 'Ligado'
                    else: 
                        ativo = 'Desligado'

                    print(f'Agora o Computador esta {ativo}')

                    print(f'O Computador esta ligado na Fonte? {not not status}') #Aqui o NOT Nega a negacao no proximo NOT

            # OR e uma operacao binaria, que depende de dois valores, sendo que um deles precisa ser verdadeiro ou True.

            # AND e uma operacao binaria, que depende de dois valorees, ao contrario do OR o AND precisa que os dois valores sejam verdadeiros ou True

# Modulo tipo String. Em Python um dado e considerado String sempre que estiver entre aspas.
    Exemplo: 
        Aspas Simple -> ''
        Aspas Duplas -> ""
        Aspas Simples Triplas -> ''' '''
        Aspas duplas Triplas -> """ """

    # E utilizado na programacao o \n para pular a linha 
        Exemplo:
            print(f'meu nome e Augusto \n tenho 22 anos')
    
    # Para Acessar uma parte especifica da Sting e possivel utilizar o Colchetes [] e dentro dele infor a posicao que quer acessar ou o raio de acesso que quer acessar
        Exemplo:
            print(nome[0]) #Para acessar uma unica posicao dentro da String selecionada
            Slice de String -> print(nome[0:10]) # Para acessar um raio de possicoes dentro da String selecionada, nesse caso o ultimo numero selecionado sera um numero anterior ao informado na segunda posicao dentro do Colchetes
            Inverter a ordem da String -> print(nome[::-1]) # Para inverter a ordem das String e necessario utilizar esses sinais, que informam que vc quer que comece pelo ultimo va ate o primeiro mostrando de 1 
            Alterar String -> print(nome.replace('a', 'g')) # Para trocar as Strings informando a String antiga pela nova String. 
    
    # Funcoes para String:
        .split() -> Funcao utilizada para transformar trasnforma em uma lista de string com base no espaco que foi dado nas palavras ou letras ao introduzir no sistema 
            Tambem e posivel acessar a posicao de uma palavar Splitada pelo .split() utilizando o Colchetes [] e dentro o numero da posicao.

# Modulo de Escopo de variaveis.
    #Escopo de variaveis e a limitacao de uma variavel no caso, e aonde ela sera reconhecida dentro do programa:

    1 - Escopo das variaveis Globais:
        O escopo para essas variaveis se extende por todo o programa;

    2 - Escopo das Variaveis locais:
        O escopo para essas variaveis se extende apenas ao bloco aonde foram declaradas;

    # Para declarar uma variavel fazemos apenas:
        Exemplo:
            nome_da_variavel = valor_da_variavel 

"""
#######################################################################################
"""
Aula 3 - Estruturas logicas e condicionais:

    # Modulo - if, elif e else.

        Estruturas Condicionasis:
            If -> Corresponde ao Se.
                Exemplo: Se caso acontecer faca essa coisa.
            Elif -> Corresponde ao Senao Se, e uma juncao do if com o else tornando se mais uma opcao de entrada dentro da estrutura condicional, e sempre sera usado caso presice de uma nova condicao.
                Exemplo: Se nao entrar no if, faca essa coisa 
            ELse ->  Corresponde ao Senao.
                Exemplo: Se nao entrar no if ou no elif (que sempre vem antes do else na estrutura condicional), faca outra coisa.

    # Modulo - and, or, not e is.

        Estruturas Logicas:
            and -> Corresponde ao E. É uma operacao logica que depende de dois valores, sendo que os dois precisam ser verdadeiro ou no caso True.
            or-> Corresponde ao OU. É uma operacao logica que depende de dois valores, sendo que apenas um deles precisa ser verdadeiro ou no caso True
            not-> Corresponde ao NÃO (negacao). É uma operacao logica que nega o valor informado, de true para false e de false para true.
            is -> Corresponde ao É. É usado para checar se duas variaveis possuem o mesmo Objeto.
                Exemplo:
                    x = ["apple", "banana", "cherry"]
                    y = ["apple", "banana", "cherry"]
                    print(x is y)

"""
#######################################################################################
"""
OBs: Utilizamos loops para iterar sobre sequencias ou valores iteraveis.
    Exemplo:
    - String -> nome = 'Augusto'
    - Lista -> cont = [1, 2, 3, 4]
    - range -> numeros = range(1, 100)
    
    # Nesse exemplo utilizamos o "Letra para separar o interavel", Podemos tamber utilizar o underline, quando nao queremos utilizar um "valor" como o indice nesse exemplo: 
        for indice, letra in enumerate(nome):
            print(letra)
        for _, letra in enumerate(nome):
            print(letra)

Obs: E necessario colocar um breack poin dentro do while para que nao gere um loop infinito


Aula 4 - Estrutura de repeticao
    # Modulo - Loop for.
        Exemplos de for:
            # Exemplo com String
            for letra in nome:
                print(f'letra do nome: {letra}')

            # Exemplo com Range()
            for numero in numeros:
                if numero == 50:
                    print(numero, ':Metade da conta')
                else:
                    print(numero)
                
            # Exemplo Com Lista 
            for numero in lista:
                if numero == 50:
                    print(numero, ':Metade da conta')
                else:
                    print(numero)   

        Loop e uma estrutura de repeticao.
            for - > Corresponde ao para, no sentido de iteravel

    # Modulo  - Range(). O range e uma funcao que auxilia a contrucao das estruturas de repeticao, com o range podes informar quantas vezes queremos que o codigo rode. 
        Exemplo: 
            range(valor_de_inicio, valor_de_parada, contador)

    # Modulo - Loop While.
        while -> O While corresponde a, enquanto e serve para que possamos iterar sobre sequencias, de forma booleana, considerando que enquanto a condicao for verdadeira o codigo continuara sendo executado.

    # Modulo - Saindo de loops com break. 
        break -> E utilizado para sair de um loop de maneira projetada

"""
#######################################################################################
"""
Obs: As Lista em python funcionam com array ou vetores. Com a diferenca de serem dinamicos e possamos incluir qualquer tipo de dados em um so array
Obs: Tambem e possivel juntar a listas, utilizando o sinal de mais criando uma nova lista, ou adicionando uma lista a outra com o extend()

Aula 5 - Colecoes em Python.
    # Modulo - Listas.
        Lista -> E considerado dinamico por nao possuir limite de tamanho, o limite e a penas a memoria do computador. nao exites destincao dos dados ao inserilos na lista
            Exemplos de Listas:
                lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 31, 43, 65, 12]
                lista_str = ['Augusto', ' ', 'Ribeiro']
                lista_vaz = []
                lista_range = list(range(11))
                lista_str2 = list('Augusto Ribeiro')

        Funcoes para manipular as listas:
            sort() -> Funcao utilizada para ordenar a lista, normalmente urilizada para tratar numeros. Porem tbm e possivel utiliza-las com Strings.
                lista_num.sort()
            cont() -> Conta quantas vezes um determinado valor se repete dentro da lista.
                print(lista_num.count(valor_a_ser_contado))   
            append() -> Adiciona novo elemento a lista, Porem so e possivel adicionar um elemento por vez. Novo valor sempre sera mandado para o final da fila
                lista_num.append(1)
            extend() -> Adiciona novos elementos a lista, Porem nao possui limite de valores como o append e so aceita a insersao de mais de um valor por vez. Novo valor sempre sera mandado para o final da fila
                lista_num.extend([1, 2, 4, 5, 6, 00, 1, 3, 6])  
            insert() -> Adiciona um novo elemento a lista, Porem e possivel escolher o indice desse novo valor. E nao sera removido o valor anterior na possicao desejada
                lista_num.insert(index_da_lista, valor_a_ser_inserido)
            reverse() -> Invert a ordem da lista 
                lista_num.reverse()
            copy() -> Como o nome diz ele copia o valor da lista para outro lugar ou outra lista 
                lista_num = lista_test.copy()
            len() -> Len de length comprimento, para que possamos ver qual o tamanho total da lista, baseado na quantidade de elementos dentro da mesma.
                print(len(lista_num))
            pop() -> Deleta o ultimo valor inserido na lista, por padrao, porem e possivel escolher qual valor sera deletado informando o seu indice como paramentro.
                lista_num.pop()
            clear() -> Limpa todos os dados da lista de uma so vez. 
                lista_num.clear()
            split() -> Transforma String em uma lista, e por padrao separa os elementos considerando o espaco entre elas
                nome = 'Augusto Ribiro Prestes da Silva'
                nome = nome.split()
            
"""
nome = ''
lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 31, 43, 65, 12]
print(lista_num)
lista_num.clear()
print(lista_num)
