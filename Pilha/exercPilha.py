# -*- coding: utf-8 -*-

from array_stack import ArrayStack  # array_stack.py eh o nome do arquivo(modulo) e ArrayStack eh a classe
from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import ListNode
from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import SinglyLinkedListIterator
from array_queue_new import ArrayQueue

class PilhaComLista:

    """Pilha implementada sobre Lista com iterador: topo eh o ultimo elemento da pilha"""

    def __init__(self):
        self._pilha = SinglyLinkedListIterator() # cria uma lista vazia ou seja uma pilha vazia

    def len(self):
        return self._pilha.size

    def is_empty(self):
        return (self._pilha.size == 0)

    def push(self, e): # topo eh o ultimo elemento da lista
        self._pilha.last_Node() # coloca o iterador no ultimo Node
        self._pilha.addNode(e) # adiciona depois do iterador(no topo da pilha)

    def top(self):  # topo eh o ultimo elemento da lista
        if(self._pilha.size == 0): # pilha Vazia
            print('pilha vazia')
            return None
        else:
            self._pilha.last_Node()  # coloca o iterador no ultimo Node
            return self._pilha.iterator.data

    def pop(self):
        if (self._pilha.size == 0):  # pilha Vazia
            print('pilha vazia')
            return None
        else:
            self._pilha.last_Node # poe o iterador no ultimo Node
            topo = self._pilha.iterator.data # salva quem esta no topo
            self._pilha.elimNode() # elimina o elemento do topo: ultimo elemento: iterador ficou indefinido
            self._pilha.lastNode # poe o iterador sobre o ultimo elemento (topo)
            return topo # retorna o elemento do topo


    def printPilha(self):
        self._pilha.first_Node()  # por o iterador sobre o primeiro elemento
        while not self._pilha.isUndefinedIterator():
            print(self._pilha.iterator.data, end=" ")
            self._pilha.nextNode()  # avanca iterador para proximo noh
        print('\n')


if __name__ == "__main__":

    def copia_stack(p: ArrayStack):  # ArrayStack eh TAD Pilha
        copia = ArrayStack()  # pilha a ser retornada
        copia_restaura = ArrayStack()  # pilha temporaria
        # percorrer a pilha original p
        while not p.is_empty():
            copia_restaura.push(p.pop())
        # ao sair do loop acima a pilha p esta vazia
        # e a pilha copia_restaura esta cheia na ordem inversa

        # percorrer a pilha copia_restaura
        # salvar o elemento removida numa variavel
        # empilhar este elemento na pilha original p, e na copia
        while not copia_restaura.is_empty():
            elem = copia_restaura.pop()
            p.push(elem)
            copia.push(elem)
        return copia

    def printStack(s):
        copia = copia_stack(s) # trabalhar so com a copia
        print("[ ")
        while not copia.is_empty():
            print(f"{copia.pop()} ")
        copia = None
        print(']\n')


    def printStack_2(s:ArrayStack):
        if s.is_empty(): # pilha/stack s esta vazia
            print("A pilha esta vazia")
        else:
            # a pilha/stack tem um ou mais elementos empilhados
            copia = ArrayStack() # instanciei a pilha copia
            # - vou usar copia para restaurar a pilha original s
            print("[")
            while not s.is_empty(): # loop para percorrer a pilha/stack
                print(f"{s.top()},") # poderia imprimir neste momento
                copia.push(s.pop())
            # ao sair do loop a pilha original esta vazia
            # e a pilha copia esta cheia, com os elementos de s na ordem inversa
            while not copia.is_empty():
                #empilhar o elemento do topo da pilha copia na pilha original s
                s.push(copia.pop())
            #ao sair do loop a pilha original s foi restaurada
            #e a pilha copia ficou vazia
            print("]")




    def copia_stack_queue(p: ArrayStack):
        copia = ArrayStack()
        # ... completar
        return copia

    # inverter a lista lst usando como apoio uma pilha/stack
    def invLista_2(lst):
        pilha = ArrayStack()
        lst.first_Node() # por o iterator sobre o primeiro elemento
        # enquanto o iterador nao ficar indefinido
        while lst.iterator:
            # empilhar o campo data (lst.iterator.data)
            pilha.push(lst.iterator.data)
            # remover o elemento sob o iterador
            lst.elimNode()
        # ao sair do loop acima a lista ficou vazia
        # e a pilha cheia mas na ordem inversa
        # enquanto a pilha p nao ficar vazia:
        while not pilha.is_empty():
            # remover o topo da pilha e adicionar na lista
            lst.addNode(pilha.pop())
        pilha = None
            

    def printLista(lista):
        lista.first_Node() # por o iterador sobre o primeiro elemento
        # ... completar

    """1) void invLista(Lista lst) 
    Inverter uma lista utilizando como apoio uma pilha. A complexidade desta 
    rotina é O(N), onde N é o número de elementos da lista. """
    def invLista(lst:SinglyLinkedListIterator):

        #se a lista estiver vazia ou so com um elemento ela ja esta invertida
        if lst.size <= 1:
            print("a lista ja esta invertida")
        #senao: a lista tem 2 ou mais elementos
        else:
            # alocar a pilha
            pilha = ArrayStack()
            # por o iterador na primeira posicao da lista
            lst.first_Node()  # lst.iterator = lst.firstNode
            #percorrer a lista: enquanto o iterador tiver um valor valido
            while lst.iterator:
                #empilhar na pilha o elemento do iterador
                pilha.push(lst.iterator.data)
                #remover o elemento do iterador: o iterador ja avanca o proximo elemento
                lst.elimNode()
            #ao sair do loop a lista esta vazia e pilha esta cheia com os elementos na ordem inversa
            # percorrer a pilha
            while not pilha.is_empty():
                #adicionar na lista o elemento do topo da pilha: basta fazer um pop e passar como
                #parametro para o metodo addNode da lista
                lst.addNode(pilha.pop())


    """
    2) Pilha copiarPilha( Pilha p ) 
    Fazer uma cópia de uma pilha, usando como apoio uma lista. Também é 
    possível usar como apoio uma pilha. A pilha original deve ser restaurada.
    """
    def copiarPilha(pilha):
        pilhaResgate = ArrayStack() # pilha auxiliar
        pilhaCopia = ArrayStack() # copia a ser retornada
        # ... completar
        return pilhaCopia

    """
    3) void invPilha( Pilha p) 
    Inverter o conteúdo de uma pilha. Usar uma lista como apoio 
    """
    def invPilha(pilha): # usando uma lista como apoio
        lista = SinglyLinkedListIterator()
        # ... completar
        lista = None

    """
    4) int iguaisPilhas( Pilha p1, Pilha p2) 
    Dizer se duas pilhas são iguais sem destruir seu conteúdo. 
    """
    def iguaisPilhas(pilha1: ArrayStack, pilha2: ArrayStack):
        pilhaAux1 = copia_stack(pilha1)
        pilhaAux2 = copia_stack(pilha2)

       #caso 2 pilhas vazias
        if pilhaAux1.is_empty() and pilhaAux2.is_empty():
            return True

        else:
            #loop para percorrer a pilha
            while not pilhaAux1.is_empty():
                #desempilha e compara
                elem1 = pilhaAux1.pop()
                elem2 = pilhaAux2.pop()
                if elem1 != elem2:
                    return  False

            #verifica se as pilhas estao vazias
            if pilhaAux1.is_empty() and pilhaAux2.is_empty():
                return True
            else:
                return False


    """7) void fundoPilha( Pilha p, TipoP elem) 
    Colocar no fundo da pilha o elemento elem
    """

    def fundoPilha(pilha:ArrayStack, elem):
       #usar como apoio uma outra pilha
       #pilha vazia pilha.isempty funciona tb
        if(len(pilha) == 0): # pilha vazia usando Classe ArrayStack
            pilha.push(elem)
        #pilha cheia
        else:
            # usar pilha de apoio para salvar os elementos
            stack = ArrayStack()
            #loop desempilhar e salvar
            while not pilha.is_empty():
                # dar pop na pilha e empilha na pilha de apoio
                stack.push(pilha.pop())
            #pilha esta vazia e pilha de apoio cheia mas invertida
            pilha.push(elem)
           #loop para desempilhar da pilha de apoio e empilhar na pilha original
            while not stack.is_empty():
                pilha.push(stack.pop())


    def fundoPilha_2(pilha: ArrayStack, elem):
        #usar como apoio lista SE
        pass


    def fundoPilha_(pilha: ArrayStack, elem):
        #usar como apoio lista python
        pass


    def elem_igual_fundoPilha(pilha: ArrayStack, elem):
        copia = copia_stack(pilha)

        if copia.is_empty():
            return False
        else:
            #ler possivel elemento do fundo
            fundo = copia.pop()
            #loop enquanto nao ficar vazia
            while not copia.is_empty():
                fundo = copia.pop()

            #sai do loop: fundo tem o elemento do fundo copia
        if fundo == elem:
            return True
        else:
            return False



    # pilha = PilhaComLista()
    # pilha.push(5)
    # pilha.printPilha()
    # pilha.push(3)
    # pilha.printPilha()
    # print(pilha.top())
    # topo = pilha.pop()
    # print('topo = {}'.format(topo))
    # pilha.printPilha()

    # lst = SinglyLinkedListIterator()
    # for i in range(5):
    #     lst.addNode(i)
    # printLista(lst)
    # # invertendo a lista
    # invLista(lst)
    # printLista(lst)



    print("====================================")
    S = ArrayStack()  # contents: [ ]
    printStack(S)
    print(S.top())
    S.push(5)  # contents: [5]
    printStack(S)
    S.push(3)  # contents: [5, 3]
    printStack(S)
    S.push(8)  # contents: [5, 3, 8]
    # fundoPilha(S, 100)
    printStack(S)
    print("==============================")
    copia = copia_stack(S)
    printStack(copia)
    print("============Print PIlha S [5, 3, 8]==================")
    printStack_2(S)
    print("============PILHA S == COPIA?==================")
    if iguaisPilhas(S, copia):
        print("pilha S == pilha copia")
    else:
        print("pilha S !=PILHA COPIA")
    print("============fundo == elem?==================")
    if elem_igual_fundoPilha(S, elem=6):
        print("elem == fundo")
    else:
        print("elem != fundo")


