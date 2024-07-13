# Automação de Reconciliação Bancária

## Descrição do Projeto
Este projeto tem como objetivo automatizar o processo de reconciliação bancária, comparando extratos bancários e registros contábeis para identificar discrepâncias. A aplicação oferece uma interface gráfica para facilitar o carregamento dos arquivos e a visualização dos resultados da reconciliação.

## Problema Resolvido
A reconciliação bancária manual é um processo demorado e suscetível a erros. Esta automação permite que as empresas realizem a reconciliação de maneira mais rápida e precisa, reduzindo a possibilidade de erros e economizando tempo.

## Funcionalidades
- Carregamento de extratos bancários.
- Carregamento de registros contábeis.
- Comparação automática dos dados para encontrar discrepâncias.
- Exibição dos resultados da reconciliação em uma interface gráfica.

## Stacks Utilizadas
- **Python**
- **Pandas**
- **Tkinter**

## Instalação

### Como clonar o repositório
```bash
git clone https://github.com/mat-cesconetto/SOLO-matheus-projeto-reconciliacao.git
cd SOLO-matheus-projeto-reconciliacao
```
### Como Criar e Ativar o Ambiente Virtual

```bash
python -m venv venv
```
#### No Linux
```bash
source venv/bin/activate 
```
 #### No Windows
 ```bash
 venv\Scripts\activate
```

### Como Instalar as Dependências
```bash
pip install pandas
```

## Como Usar

### Execute o Script
```bash
python app.py
```

## Como usar a interface gráfica
- Ao iniciar o programa, uma janela aparecerá.
- Clique em "Carregar Extrato Bancário" para selecionar e carregar o arquivo de extrato.
- Clique em "Carregar Registros Contábeis" para selecionar e carregar o arquivo de registros.
- Clique em "Reconciliar" para iniciar o processo de reconciliação e visualizar os resultados na interface.
