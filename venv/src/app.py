# Importando as bibliotecas necessárias
import pandas as pd
from tkinter import *
from tkinter import filedialog

# Lendo as planilhas
extrato = pd.read_excel('venv/src/extrato_bancario.xlsx')
registros = pd.read_excel('venv/src/registros_contabeis.xlsx')

# Class onde tudo vai funcionar
class Janela():
    
    # Def onde a tela é carregada
    def __init__(self):
        self.root = Tk()
        self.config()
        self.widgets()
        self.extrato = None
        self.registro = None
        self.root.mainloop()
    
    # Def onde é configurado o tamnho e o título da página
    def config(self):
        self.root.title('Automação Reconciliação Bancária')
        self.root.geometry('800x600+500+80')

    # Def que pede pro usuário abrir o arquivo do extrato e o lê, assim como o mostra na tela
    def extrato(self):
        # Faz o usuário carregar o arquivo
        self.arquivo = filedialog.askopenfile(mode='r', initialdir='/Users/usuario/Documents/arqv')
        if self.arquivo:
            self.extrato = pd.read_excel(self.arquivo.name)
            self.texto.insert(END, 'Extrato Bancário Carregado: \n')
            self.texto.insert(END, self.extrato)
            self.texto.insert(END, '\n\n')

    # Def que pede pro usuário abrir o arquivo do registro e o lê, assim como o mostra na tela
    def registro(self):
        # Faz o usuário carregar o arquivo
        self.arquivo = filedialog.askopenfile(mode='r', initialdir='/Users/usuario/Documents/arqv')
        if self.arquivo:
            self.registro = pd.read_excel(self.arquivo.name)
            self.texto.insert(END, 'Registros Bancário Carregado: \n')
            self.texto.insert(END, self.registro)
            self.texto.insert(END, '\n\n')
        
    # Def que define os itens presentes na tela, como botões e os textos
    def widgets(self):
        self.btn1 = Button(text='Carregar Extrato Bancário', command=self.extrato)
        self.btn1.place(relx=0.45, rely=0.05)
        self.btn2 = Button(text='Carregar Registros Contábeis', command=self.registro)
        self.btn2.place(relx=0.44, rely=0.15)
        self.btn3 = Button(text='Reconciliar', command=self.reconciliar)
        self.btn3.place(relx=0.49, rely=0.25)
        self.texto = Text()
        self.texto.place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.6)

    # Def que faz a reconciliação dos  dados
    def reconciliar(self):
        # Pegando os dados em comum entre os dois
        df_registro_extrato = pd.merge(extrato, registros, on=['Data', 'Descrição', 'Valor'], how='inner', indicator=True)
        df_registro_extrato = df_registro_extrato.drop(columns=['_merge'])
        self.texto.insert(END, 'Transferências Encontradas na Reconciliação \n')
        self.texto.insert(END, df_registro_extrato)
        self.texto.insert(END, '\n\n')

        # Pegando os dados apenas do extrato
        df = pd.merge(extrato, registros, on=['Data', 'Descrição', 'Valor'], how='right', indicator=True)
        df_extrato = df[df['_merge'] == 'right_only'].copy()
        df_extrato = df_extrato.drop(columns=['_merge'])
        if not df_extrato.empty:
            print(df_extrato)
            self.texto.insert(END, 'Transferências Presentes nos Registros Contábeis e Ausentes no extrato Bancário \n')
            self.texto.insert(END, df_extrato)
            self.texto.insert(END, '\n\n')
            
        else:
            self.texto.insert(END, 'Não há Transferências Presentes nos Registros Contábeis e Ausentes no extrato Bancário')
            self.texto.insert(END, '\n\n')

        # Pegando os dados apenas do registro
        df = pd.merge(extrato, registros, on=['Data', 'Descrição', 'Valor'], how='left', indicator=True)
        df_registro = df[df['_merge'] == 'left_only'].copy()
        df_registro = df_registro.drop(columns=['_merge'])
        if not df_registro.empty:
            self.texto.insert(END, 'Transferências Presentes nos extrato Bancário e Ausentes no Registros Contábeis \n')
            self.texto.insert(END, df_registro)
            self.texto.insert(END, '\n\n')

        else:
            self.texto.insert(END, 'Não há Transferências Presentes nos extrato Bancário e Ausentes no Registros Contábeis')
            self.texto.insert(END, '\n\n')

# Executa todo o progrma
Janela()