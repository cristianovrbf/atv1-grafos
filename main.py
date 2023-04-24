import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.attributes('-fullscreen', True)
D = nx.DiGraph()
G = nx.Graph()

janela.title("Grafos")
titulo = Label(janela, text="")
label_direcionado = Label(janela, text="Seu grafo será direcionado?")
valor_direcionado = StringVar()
sim_direcionado = Radiobutton(janela, text="Sim", variable=valor_direcionado, value="sim")
nao_direcionado = Radiobutton(janela, text="Não", variable=valor_direcionado, value="nao")
label_valorado = Label(janela, text="Seu grafo será valorado?")
valor_valorado = StringVar()
titulo_vertice = Label(janela, text="Vertice")
label_rotulo = Label(janela, text="Digite o rótulo do seu vértice:")
entrada_rotulo = Entry(janela)
titulo_aresta = Label(janela, text="Aresta")
label_v1 = Label(janela, text="Digite o primeiro vértice:")
label_v2 = Label(janela, text="Digite o segundo vértice:")
label_peso = Label(janela, text="Digite o peso do vértice:")
entrada_v1 = Entry(janela)
entrada_v2 = Entry(janela)
entrada_peso = Entry(janela)
formato_entrada = Label(janela, text="")
entrada_lote = Entry(janela)
ordem = Label(janela)
tamanho = Label(janela)
lista_entrada = Label(janela)
lista_saida = Label(janela)
lista_label = Label(janela)
label_vertice = Label(janela, text="Vértice: ")
entrada_vertice = Entry(janela)
grau_saida = Label(janela)
grau_entrada = Label(janela)
grau_label = Label(janela)
label_par = Label(janela)
label_custo = Label(janela)
label_caminho = Label(janela)
label_raio = Label(janela)
label_diam = Label(janela)
frame = Frame(janela)
titulo_frame = Label(janela)

fig = Figure()
canvas = FigureCanvasTkAgg(fig, master=frame)


def verticeInGraph(vertice, direcionado):
    if(direcionado == "sim"):
        for v in D.nodes():
            if (vertice == v):
                return True
        return False
    elif(direcionado=="nao"):
        for v in G.nodes():
            if (vertice == v):
                return True
        return False

def addArestaValorada(peso, v1, v2, direcionado):
    if(verticeInGraph(v1, direcionado) == False or verticeInGraph(v2, direcionado) == False):
        message = "Um ou os dois vertices não existem!"
        messagebox.showerror("Alerta: ", message)
    else:
        if(direcionado=="sim"):
            D.add_edge(v1,v2)
            D[v1][v2]['peso'] = peso
        elif(direcionado=="nao"):
            G.add_edge(v1,v2)
            G[v1][v2]['peso'] = peso


def addAresta(v1, v2, direcionado):
    if(verticeInGraph(v1, direcionado) == False or verticeInGraph(v2, direcionado) == False):
        message = "Um ou os dois vertices não existem!"
        messagebox.showerror("Alerta: ", message)
    else:
        if(direcionado=="sim"):
            D.add_edge(v1,v2)
        elif(direcionado=="nao"):
            G.add_edge(v1,v2)

def addVertice(v, direcionado):
    if(verticeInGraph(v,direcionado) == False):
        if (direcionado == "sim"):
            D.add_node(v)
        elif (direcionado == "nao"):
            G.add_node(v)
    else:
        message = "Vertice já existe no grafo!"
        messagebox.showerror("Alerta: ", message)

def oneByOne(item, valorado, direcionado):
    item = item.split("-")
    if (item[0] == "V"):
        if (len(item) == 2):
            addVertice(item[1], direcionado)
        else:
            message = f'A entrada {item} não segue o padrão!'
            messagebox.showerror("Entrada inválida: ", message)
    elif (item[0] == "A"):
        if (valorado == 'sim' and len(item) == 4):
            addArestaValorada(item[1], item[2], item[3], direcionado)
        elif (valorado == 'nao' and len(item) == 3):
            addAresta(item[1], item[2], direcionado)
        else:
            message = f'A entrada {item} não segue o padrão!'
            messagebox.showerror("Entrada inválida: ", message)
    else:
        message = f'A entrada {item} não segue o padrão!'
        messagebox.showerror("Entrada inválida: ", message)

def grauVertice(vertice, direcionado):
    cont = 0
    if(verticeInGraph(vertice, direcionado)==True):
        for e in G.edges():
            if(e[0]==vertice or e[1]==vertice):
                cont = cont + 1
        grau_label["text"] = f'O grau do vértice ({vertice}) é: {cont}'
        grau_label.grid(column=0, row=2)
    else:
        message = "Vertice não encontrado no grafo!"
        messagebox.showerror("Alerta: ", message)

def grauAdjacencia(vertice, direcionado):
    saida = 0
    entrada = 0
    if(verticeInGraph(vertice, direcionado)==True):
        for e in D.edges():
            if(e[0]==vertice):
                saida = saida + 1
            elif(e[1]==vertice):
                entrada = entrada + 1
        grau_saida["text"] = f'Grau de adjacencia de saída do vertice ({vertice}) é: {saida}'
        grau_entrada["text"] = f'Grau de adjacencia de entrada do vertice ({vertice}) é: {entrada}'
        grau_saida.grid(column=0, row=2)
        grau_entrada.grid(column=0, row=3)
    else:
        message = "Vertice não encontrado no grafo!"
        messagebox.showerror("Alerta: ", message)

def grau():
    vertice = entrada_vertice.get()
    entrada_vertice.delete(0, END)
    direcionado = valor_direcionado.get()
    if(direcionado=="sim"):
        grauAdjacencia(vertice, direcionado)
    elif(direcionado=="nao"):
        grauVertice(vertice, direcionado)
    else:
        message = "Não existe grafo ainda!"
        messagebox.showerror("Alerta: ", message)

btn_grau_vertice = Button(janela, text="enviar", command=grau)

def listaAdja(vertice):
    lista = []
    for e in G.edges():
        if(e[0] == vertice):
            lista.append(e[1])
        elif(e[1]==vertice):
            lista.append(e[0])
    lista_label["text"] = f'Lista de vértices adjacentes a ({vertice}):  {lista}'
    lista_label.grid(column=0, row=2)

def listaAdjaDir(vertice):
    saida = []
    entrada = []
    for e in D.edges():
        if(e[0] == vertice):
            saida.append(e[1])
        elif(e[1]==vertice):
            entrada.append(e[0])
    lista_entrada["text"] = f'Lista de vértices adjacentes de entrade a ({vertice}): {entrada}'
    lista_saida["text"] = f'Lista de vértices adjacentes de saída a ({vertice}): {saida}'
    lista_entrada.grid(column=0, row=2)
    lista_saida.grid(column=0, row=3)

def adjacentes():
    vertice = entrada_vertice.get()
    direcionado = valor_direcionado.get()
    entrada_vertice.delete(0, END)
    if(vertice!=""):
        if(direcionado=="sim"):
            if(verticeInGraph(vertice,direcionado)==True):
                listaAdjaDir(vertice)
            else:
                message = "Não vértice não encontrado no grafo!"
                messagebox.showerror("Alerta: ", message)
        elif(direcionado=="nao"):
            if(verticeInGraph(vertice,direcionado)==True):
                listaAdja(vertice)
            else:
                message = "Não vértice não encontrado no grafo!"
                messagebox.showerror("Alerta: ", message)
        else:
            message = "Não existe grafo ainda!"
            messagebox.showerror("Alerta: ", message)
    else:
        message = "Digite um vertice existente!"
        messagebox.showerror("Alerta: ", message)

btn_lista_ad = Button(janela, text="enviar", command=adjacentes)

def parAdja():
    vertice1 = entrada_v1.get()
    vertice2 = entrada_v2.get()
    entrada_v1.delete(0, END)
    entrada_v2.delete(0, END)
    direcionado = valor_direcionado.get()
    flag = 0
    if(direcionado=="sim" and verticeInGraph(vertice1,direcionado)==True and verticeInGraph(vertice2,direcionado)==True):
        for e in D.edges():
            if(vertice1 == e[0] or vertice1 == e[1]):
                if(vertice2 == e[0] or vertice2 == e[1]):
                    flag = 1
    elif(direcionado=="nao" and  verticeInGraph(vertice1,direcionado)==True and verticeInGraph(vertice2,direcionado)==True):
        for e in G.edges():
            if(vertice1 == e[0] or vertice1 == e[1]):
                if(vertice2 == e[0] or vertice2 == e[1]):
                    flag = 1
    elif(direcionado==""):
        message = "Não existe grafo ainda!"
        messagebox.showerror("Alerta: ", message)
    elif(verticeInGraph(vertice1,direcionado)==False or verticeInGraph(vertice2,direcionado)==False):
        message = "Um ou os dois vertices não encontrado no grafo!"
        messagebox.showerror("Alerta: ", message)

    if(flag==1):
        label_par["text"] = "Sim, os vértices são adjacentes!"
        label_par["fg"] = "green"
    elif(flag==0):
        label_par["text"] = "Não, os vértices não são adjacentes!"
        label_par["fg"] = "red"
    label_par.grid(column=1, row=3)

btn_parAdj = Button(janela, text="enviar", command=parAdja)

def buscaDicionario(v, dic):
    for c in dic:
        if(v == c[0]):
            return True
    return False

def custoDijkstra(v, dic):
    for c in dic:
        if(v == c[0]):
            return c[1]
    return -1

def apagaCam(vFinal, dic):
    cont =  0
    for c in dic:
        if(vFinal==c[0]):
            dic.pop(cont)
            return 1
        cont = cont + 1
    return 0

def dijkstra(vInicio):
    caminhos = [(vInicio,0, vInicio)]
    nos = [vInicio]
    while(len(nos)!=0):
        for e in G.edges:
            if(nos[0]==e[0]):
                if(buscaDicionario(e[1], caminhos)==True):
                    custoVfinal = custoDijkstra(e[1], caminhos)
                    custoVinicial = custoDijkstra(e[0], caminhos)
                    novocusto = custoVinicial+ int(G[e[0]][e[1]]['peso'])
                    if(custoVfinal > novocusto):
                        apagaCam(e[1], caminhos)
                        caminhos.append((e[1], novocusto, e[0]))
                elif(buscaDicionario(e[1], caminhos)==False):
                    custoV1 = custoDijkstra(e[0], caminhos)
                    custo = custoV1+ int(G[e[0]][e[1]]['peso'])
                    caminhos.append((e[1], custo, e[0]))
                    nos.append(e[1])
            elif(nos[0]==e[1]):
                if (buscaDicionario(e[0], caminhos) == True):
                    custoVfinal = custoDijkstra(e[0], caminhos)
                    custoVinicial = custoDijkstra(e[1], caminhos)
                    novocusto = custoVinicial + int(G[e[0]][e[1]]['peso'])
                    if (custoVfinal > novocusto):
                        apagaCam(e[1], caminhos)
                        caminhos.append((e[1], novocusto, e[0]))
                elif (buscaDicionario(e[0], caminhos) == False):
                    custoV1 = custoDijkstra(e[1], caminhos)
                    custo = custoV1 + int(G[e[0]][e[1]]['peso'])
                    caminhos.append((e[0], custo, e[1]))
                    nos.append(e[0])
        nos.pop(0)
    return caminhos

def dijkstraDirecionado(vInicio):
    caminhos = [(vInicio,0, vInicio)]
    nos = [vInicio]
    while(len(nos)!=0):
        for e in D.edges:
            if(nos[0]==e[0]):
                if(buscaDicionario(e[1], caminhos)==True):
                    custoVfinal = custoDijkstra(e[1], caminhos)
                    custoVinicial = custoDijkstra(e[0], caminhos)
                    novocusto = custoVinicial+ int(D[e[0]][e[1]]['peso'])
                    if(custoVfinal > novocusto):
                        apagaCam(e[1], caminhos)
                        caminhos.append((e[1], novocusto, e[0]))
                elif(buscaDicionario(e[1], caminhos)==False):
                    custoV1 = custoDijkstra(e[0], caminhos)
                    custo = custoV1+ int(D[e[0]][e[1]]['peso'])
                    caminhos.append((e[1], custo, e[0]))
                    nos.append(e[1])
        nos.pop(0)
    return caminhos

def custoDijkstra(vFinal, lista):
    for x in lista:
        if(x[0]==vFinal):
            return x[1]
    return -1

def arestaParaV(vf, listaDijkstra):
    for c in listaDijkstra:
        if(c[0]==vf):
            return True
    return False

def caminhoDijkstra(vInicio, vFinal, direcionado):
    if(direcionado=="sim"):
        listaDijkstra = dijkstraDirecionado(vInicio)
        custo = custoDijkstra(vFinal, listaDijkstra)
    elif(direcionado=="nao"):
        listaDijkstra = dijkstra(vInicio)
        custo = custoDijkstra(vFinal, listaDijkstra)
    else:
        message = "Não existe grafo ainda!"
        messagebox.showerror("Alerta: ", message)
        return False
    if(arestaParaV(vFinal, listaDijkstra)==True):
        caminho = [vFinal]
        cont = 0
        while caminho[cont]!=vInicio:
            for c in listaDijkstra:
                if(c[0] == caminho[cont]):
                    caminho.append(c[2])
            cont = cont + 1
        caminho.reverse()
        label_custo["text"] = f'O custo será de: {custo}'
        label_caminho["text"] = f'E o caminho a ser percorrido deve ser: {caminho}'
    elif(arestaParaV(vFinal, listaDijkstra)==False):
        custo = -1
        caminho = []
        label_custo["text"] = f'O custo será de: Não existe'
        label_caminho["text"] = f'E o caminho a ser percorrido deve ser: Não existe'
    retorno = [custo, caminho]
    return retorno

def excentricidade():
    direcionado = valor_direcionado.get()
    lista_exc = []
    if(direcionado=="sim"):
        for n in D.nodes:
            for nn in D.nodes:
                if(n!=nn):
                    exc = caminhoDijkstra(n, nn, direcionado)
                    if(exc[0]!=-1):
                        lista_exc.append(exc[0])
        return lista_exc
    elif(direcionado=="nao"):
        for n in G.nodes:
            for nn in G.nodes:
                if(n!=nn):
                    exc = caminhoDijkstra(n,nn, direcionado)
                    if (exc[0] != -1):
                        lista_exc.append(exc[0])
        return lista_exc

def raioDiametro():
    direcionado = valor_direcionado.get()
    if(direcionado=="sim" or direcionado=="nao"):
        execentricidades = excentricidade()
        raio = min(execentricidades)
        diametro = max(execentricidades)
        label_raio["text"] = f'Raio do Grafo é: {raio}'
        label_diam["text"] = f'Diâmetro do Grafo é: {diametro}'
        label_raio.grid(column=0, row=1)
        label_diam.grid(column=0, row=2)
    else:
        label_raio["text"] = f'Raio do Grafo é: nulo'
        label_diam["text"] = f'Diâmetro do Grafo é: nulo'
        message = "Nenhum grafo existente ainda!"
        messagebox.showerror("Alerta: ", message)


def isValorado():
    if(titulo["text"]=="Criar grafo item a item"):
        if(valor_valorado.get()=="sim"):
            label_peso.grid(column=2, row=9)
            entrada_peso.grid(column=2, row=10)
            enviar_aresta.grid(column=3, row=10)
        elif(valor_valorado.get()=="nao"):
            label_peso.grid_forget()
            entrada_peso.grid_forget()
    else:
        if(valor_valorado.get()=="sim"):
            formato_entrada["text"] = f'''
            A entrada deve seguir o seguinte formato
            Para cada vértice: V-seuRotulo e Para cada aresta: A-seuPeso-vertice1-vertice2
            Exemplo: V-v1 V-v2 A-3-v1-v2 V-v3 A-1-v3-v2'''
        elif(valor_valorado.get()=="nao"):
            formato_entrada["text"] = f'''
            A entrada deve seguir o seguinte formato:
            Para cada vértice: V-seuRotulo e Para cada aresta: A-vertice1-vertice2
            Exemplo: V-v1 V-v2 A-v1-v2 V-v3 A-v3-v2'''

sim_valorado = Radiobutton(janela, text="Sim", variable=valor_valorado, value="sim", command=isValorado)
nao_valorado = Radiobutton(janela, text="Não", variable=valor_valorado, value="nao", command=isValorado)

def enviarVertice():
    if(valor_valorado.get()=="" or valor_direcionado.get()==""):
        message = "Escolha se seu grafo será direcionado e/ou valorado antes de enviar um vértice!"
        messagebox.showerror("Alerta: ", message)
    elif(entrada_rotulo.get()==""):
        message = "Digite o rotulo do vertice antes de enviar!"
        messagebox.showerror("Alerta: ", message)
    else:
        addVertice(entrada_rotulo.get(), valor_direcionado.get())
        entrada_rotulo.delete(0, END)

def enviarAresta():
    if (valor_valorado.get() == "" or valor_direcionado.get() == ""):
        message = "Escolha se seu grafo será direcionado e/ou valorado antes de enviar um vértice!"
        messagebox.showerror("Alerta: ", message)
    elif (entrada_v1.get() == ""):
        message = "Digite o primeiro vértice da aresta!"
        messagebox.showerror("Alerta: ", message)
    elif (entrada_v2.get() == ""):
        message = "Digite o segundo vértice da aresta!"
        messagebox.showerror("Alerta: ", message)
    elif (valor_valorado.get() == "sim" and entrada_peso.get()==""):
        message = "Digite o peso da aresta!"
        messagebox.showerror("Alerta: ", message)
    else:
        if(valor_valorado.get()=="sim"):
            addArestaValorada(entrada_peso.get(), entrada_v1.get(), entrada_v2.get(), valor_direcionado.get())
        elif(valor_valorado.get()=="nao"):
            addAresta(entrada_v1.get(), entrada_v2.get(), valor_direcionado.get())

def enviarLote():
    if (valor_valorado.get() == "" or valor_direcionado.get() == ""):
        message = "Escolha se seu grafo será direcionado e/ou valorado antes de enviar um vértice!"
        messagebox.showerror("Alerta: ", message)
    else:
        entrada = entrada_lote.get()
        entrada = entrada.replace('\n', '')
        entrada = entrada.split(" ")
        cont = 0
        while (cont < len(entrada)):
            oneByOne(entrada[cont], valor_valorado.get(), valor_direcionado.get())
            cont = cont + 1
        entrada_lote.delete(0, END)

def plotaImagem():
    if (valor_direcionado.get() == "sim"):
        fig = plt.figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        nx.draw_networkx(D, pos=nx.spring_layout(D), ax=ax, with_labels=True)
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().grid(column=1, row=3)
    elif (valor_direcionado.get() == "nao"):
        fig = plt.figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        nx.draw_networkx(G, pos=nx.spring_layout(G), ax=ax, with_labels=True)
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().grid(column=1, row=3)
    else:
        message = "Nenhum grafo existente ainda!"
        messagebox.showerror("Alerta: ", message)

def caminhoEcusto():
    if (entrada_v1.get() != "" and entrada_v2.get() != ""):
        if (verticeInGraph(entrada_v1.get(), valor_direcionado.get()) == True and verticeInGraph(entrada_v2.get(), valor_direcionado.get()) == True):
            caminhoDijkstra(entrada_v1.get(), entrada_v2.get(), valor_direcionado.get())
        else:
            message = "Vertice(s) não encontrado(s) no grafo!"
            messagebox.showerror("Alerta: ", message)
    else:
        message = "Digite os dois vértices antes de enviar!"
        messagebox.showerror("Alerta: ", message)
    entrada_v1.delete(0, END)
    entrada_v2.delete(0, END)

btn_caminho = Button(janela, text="enviar", command=caminhoEcusto)

enviar_lote = Button(janela, text="Enviar entrada em lote", command=enviarLote)
enviar_aresta = Button(janela, text="Enviar", command=enviarAresta)
enviar_vertice = Button(janela, text="Enviar", command=enviarVertice)


def startMenu():
    titulo["text"] = "Seu Grafo - Menu"
    titulo.grid(column=5, row=3)
    if(len(G.nodes())==0 and len(D.nodes())==0):
        valor_valorado.set("")
        valor_direcionado.set("")
    if(frame.winfo_ismapped()):
        frame.grid_forget()
    btnOpcao1.grid(column=5, row=5)
    btnOpcao2.grid(column=5, row=6)
    btnOpcao3.grid(column=5, row=7)
    btnOpcao4.grid(column=5, row=8)
    btnOpcao5.grid(column=5, row=9)
    btnOpcao6.grid(column=5, row=10)
    btnOpcao7.grid(column=5, row=11)
    btnOpcao8.grid(column=5, row=12)
    btnOpcao9.grid(column=5, row=13)
    label_direcionado.grid_forget()
    sim_direcionado.grid_forget()
    nao_direcionado.grid_forget()
    label_valorado.grid_forget()
    titulo_vertice.grid_forget()
    label_rotulo.grid_forget()
    entrada_rotulo.grid_forget()
    titulo_aresta.grid_forget()
    label_v1.grid_forget()
    label_v2.grid_forget()
    label_peso.grid_forget()
    entrada_peso.grid_forget()
    entrada_v1.grid_forget()
    entrada_v2.grid_forget()
    formato_entrada.grid_forget()
    entrada_lote.grid_forget()
    sim_valorado.grid_forget()
    nao_valorado.grid_forget()
    enviar_lote.grid_forget()
    enviar_aresta.grid_forget()
    enviar_vertice.grid_forget()
    voltar_menu.grid_forget()
    ordem.grid_forget()
    tamanho.grid_forget()
    lista_label.grid_forget()
    lista_entrada.grid_forget()
    lista_saida.grid_forget()
    label_vertice.grid_forget()
    entrada_vertice.grid_forget()
    btn_lista_ad.grid_forget()
    btn_grau_vertice.grid_forget()
    btn_parAdj.grid_forget()
    btn_caminho.grid_forget()
    label_raio.grid_forget()
    label_diam.grid_forget()
    grau_label.grid_forget()
    grau_saida.grid_forget()
    grau_entrada.grid_forget()
    label_par.grid_forget()
    label_custo.grid_forget()
    label_caminho.grid_forget()
    titulo_frame.grid_forget()
    voltar_menu_frame.grid_forget()

voltar_menu = Button(janela, text="Voltar ao menu", command=startMenu)
voltar_menu_frame = Button(frame, text="Voltar ao menu", command=startMenu)

def opcao1():
    closeMenu()
    titulo["text"] = "Criar grafo item a item"
    titulo.grid(column=0, row=0)
    label_direcionado.grid(column=0, row=1)
    sim_direcionado.grid(column=0, row=2)
    nao_direcionado.grid(column=1, row=2)
    label_valorado.grid(column=0, row=3)
    sim_valorado.grid(column=0, row=4)
    nao_valorado.grid(column=1, row=4)
    titulo_vertice.grid(column=0, row=5)
    label_rotulo.grid(column=0, row=6)
    entrada_rotulo.grid(column=0, row=7)
    enviar_vertice.grid(column=1, row=7)
    titulo_aresta.grid(column=0, row=8)
    label_v1.grid(column=0, row=9)
    label_v2.grid(column=1, row=9)
    entrada_v1.grid(column=0, row=10)
    entrada_v2.grid(column=1, row=10)
    enviar_aresta.grid(column=2, row=10)
    voltar_menu.grid(column=2, row=14)

def opcao2():
    closeMenu()
    titulo["text"] = "Criar grafo com String em lote"
    titulo.grid(column=0, row=0)
    label_direcionado.grid(column=0, row=1)
    sim_direcionado.grid(column=0, row=2)
    nao_direcionado.grid(column=1, row=2)
    label_valorado.grid(column=0, row=3)
    sim_valorado.grid(column=0, row=4)
    nao_valorado.grid(column=1, row=4)
    formato_entrada.grid(column=0, row=5)
    entrada_lote.grid(column=0, row=6)
    enviar_lote.grid(column=1, row=6)
    voltar_menu.grid(column=2, row=8)

def opcao3():
    closeMenu()
    titulo_frame["text"] = "Visualizar o grafo"
    titulo_frame.grid()
    frame.grid()
    plotaImagem()
    voltar_menu_frame.grid(column=2, row=5)

def opcao4():
    closeMenu()
    titulo["text"] = "Ordem e Tamanho"
    titulo.grid(column=0, row=0)
    if(valor_direcionado.get()=="sim"):
        ordem["text"] = f'Ordem: {len(D.nodes())}'
        tamanho["text"] = f'Tamanho: {len(D.edges())}'
        ordem.grid(column=0, row=1)
        tamanho.grid(column=0, row=2)
    elif(valor_direcionado.get()=="nao"):
        ordem["text"] = f'Ordem: {len(G.nodes())}'
        tamanho["text"] = f'Tamanho: {len(G.edges())}'
        ordem.grid(column=0, row=1)
        tamanho.grid(column=0, row=2)
    else:
        ordem["text"] = "Ordem: 0"
        tamanho["text"] = "Tamanho: 0"
        ordem.grid(column=0, row=1)
        tamanho.grid(column=0, row=2)
        message = "Não existe grafo ainda!"
        messagebox.showerror("Alerta: ", message)
    voltar_menu.grid(column=2, row=3)

def opcao5():
    closeMenu()
    titulo["text"] = "Lista de adjacencia do vertice"
    titulo.grid(column=0, row=0)
    label_vertice.grid(column=0, row=1)
    entrada_vertice.grid(column=1, row=1)
    btn_lista_ad.grid(column=2, row=1)
    voltar_menu.grid(column=0, row=4)

def opcao6():
    closeMenu()
    titulo["text"] = "Grau do vertice"
    titulo.grid(column=0, row=0)
    label_vertice.grid(column=0, row=1)
    entrada_vertice.grid(column=1, row=1)
    btn_grau_vertice.grid(column=2, row=1)
    voltar_menu.grid(column=0, row=4)

def opcao7():
    closeMenu()
    titulo["text"] = "Par de vértices adjacentes"
    titulo.grid(column=0, row=0)
    label_v1.grid(column=0, row=1)
    label_v2.grid(column=0, row=2)
    entrada_v1.grid(column=1, row=1)
    entrada_v2.grid(column=1, row=2)
    btn_parAdj.grid(column=1, row=4)
    voltar_menu.grid(column=1, row=5)

def opcao8():
    closeMenu()
    titulo["text"] = "O caminho mais curto entre 2 vértices"
    titulo.grid(column=0, row=0)
    label_v1.grid(column=0, row=1)
    label_v2.grid(column=0, row=2)
    entrada_v1.grid(column=1, row=1)
    entrada_v2.grid(column=1, row=2)
    label_custo.grid(column=1, row=3)
    label_caminho.grid(column=1, row=4)
    btn_caminho.grid(column=1, row=5)
    voltar_menu.grid(column=1, row=6)

def opcao9():
    closeMenu()
    titulo["text"] = "Raio e Diâmetro do Grafo"
    titulo.grid(column=0, row=0)
    voltar_menu.grid(column=1, row=3)
    raioDiametro()


btnOpcao1 = Button(janela, text="Criar grafo item a item", command=opcao1)
btnOpcao2 = Button(janela, text="Criar grafo com entrada em lote", command=opcao2)
btnOpcao3 = Button(janela, text="Visualizar o Grafo", command=opcao3)
btnOpcao4 = Button(janela, text="Ordem e tamanho do Grafo", command=opcao4)
btnOpcao5 = Button(janela, text="Lista de Adjencia do vertice", command=opcao5)
btnOpcao6 = Button(janela, text="Grau do vertice", command=opcao6)
btnOpcao7 = Button(janela, text="Par de vértices adjacentes", command=opcao7)
btnOpcao8 = Button(janela, text="O caminho mais curto entre 2 vértices", command=opcao8)
btnOpcao9 = Button(janela, text="Raio e Diâmetro do Grafo", command=opcao9)



def closeMenu():
    titulo.grid_forget()
    btnOpcao1.grid_forget()
    btnOpcao2.grid_forget()
    btnOpcao3.grid_forget()
    btnOpcao4.grid_forget()
    btnOpcao5.grid_forget()
    btnOpcao6.grid_forget()
    btnOpcao7.grid_forget()
    btnOpcao8.grid_forget()
    btnOpcao9.grid_forget()


titulo["text"] = "Seu Grafo - Menu"
titulo.grid(column=5, row=3)
btnOpcao1.grid(column=5, row=5)
btnOpcao2.grid(column=5, row=6)
btnOpcao3.grid(column=5, row=7)
btnOpcao4.grid(column=5, row=8)
btnOpcao5.grid(column=5, row=9)
btnOpcao6.grid(column=5, row=10)
btnOpcao7.grid(column=5, row=11)
btnOpcao8.grid(column=5, row=12)
btnOpcao9.grid(column=5, row=13)

try:
    janela.mainloop()
except KeyboardInterrupt:
    janela.destroy()