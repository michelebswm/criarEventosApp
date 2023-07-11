import tkinter as tk
from criar_eventos import criar_evento270, criar_evento274, criar_evento275, criar_evento277, criar_evento278,\
    criar_evento276,criar_evento279, criar_evento271, criar_evento272, criar_evento273, criar_evento300, criar_evento301, \
    criar_evento302, criar_evento303, criar_evento304
import requests
import json
from motivoRescisao import motivo_rescisao


def formata_texto(texto):
    texto = texto.replace('Ã©', 'é').replace('Ã³', 'ó').replace('Ã­', 'í').replace('Ã£', 'ã').replace('Ã¡', 'á')\
        .replace('Ã§', 'ç').replace('\\', '').replace('Ãª', 'e')
    return texto


def envia_verifica_lote(operacao, bearer, payload, api):
    import requests
    import sys
    import colorama
    import time

    if operacao not in ('POST', 'PUT', 'DELETE'):
        print("Tipo de operação incorreto!")
        print("Utilize POST, PUT ou DELETE")
        sys.exit()

    idGerado = None
    headers = {
        'Authorization': f'Bearer {bearer}',
        'Content-Type': 'application/json'
    }
    try:
        urlPost = f"https://pessoal.cloud.betha.com.br/service-layer/v1/api/{api}"
        post = requests.request(f"{operacao}", urlPost, headers=headers, data=payload)
        post = post.json()
        print('-' * 25, 'IdLote', '-' * 25)
        print(post)
    except:
        print(colorama.Fore.RED, "Executando o envio novamente!", colorama.Style.RESET_ALL)
        time.sleep(2)
        urlPost = f"https://pessoal.betha.cloud/service-layer/v1/api/{api}"
        post = requests.request(f"{operacao}", urlPost, headers=headers, data=payload)
        post = post.json()
        print('-' * 25, 'IdLote', '-' * 25)
        print(post)

    loteExecutado = False
    while not loteExecutado:
        url = f"https://pessoal.cloud.betha.com.br/service-layer/v1/api/lote/lotes/{post['id']}"

        payload = {}
        try:
            lote = requests.request("GET", url, headers=headers, data=payload)
            lote = lote.json()

            if lote['situacao'] == 'EXECUTADO':

                for i in lote['retorno']:
                    if i['mensagem'] is not None:
                        print(colorama.Fore.RED, lote, colorama.Style.RESET_ALL)
                    else:
                        idGerado = i['idGerado']
                        print(lote)
                        print("-" * 100)

                break
            time.sleep(2)
        except:
            continue

    return idGerado


def cadastrar_eventos():
    token = entry_token.get()
    # Verificando se o Token Foi Preenchido
    label_semtoken.configure(text='')
    if token == "":
        label_semtoken.configure(text='Preencha o Token', fg='red')
    lista = motivo_rescisao(token)
    # Validação Evento 270
    cod270_antigo = entry_cod270_antigo.get()
    cod270novo = entry_cod270_novo.get()
    if cod270_antigo =='' or cod270novo =='':
        label_270result.configure(text='Preencha o Código', fg='red')
    else:
        cod270_antigo = int(cod270_antigo)
        cod270novo = int(cod270novo)
        criar_evento270(codigo_evento_copiado=cod270_antigo, codigo_novo_evento=cod270novo, token=token, lista_motivos=lista)
        label_270result.configure(text='Evento Cadastrado', fg='green')

    # Validação Evento 274
    cod274_antigo = entry_cod274_antigo.get()
    cod274novo = entry_cod274_novo.get()
    if cod274_antigo == '' or cod274novo == '':
        label_274result.configure(text='Preencha o Código', fg='red')
    else:
        cod274_antigo = int(cod274_antigo)
        cod274novo = int(cod274novo)
        criar_evento274(codigo_evento_copiado=cod274_antigo, codigo_novo_evento=cod274novo, token=token,
                        lista_motivos=lista)
        label_274result.configure(text='Evento Cadastrado', fg='green')

    # Validação Evento 275
    cod275_antigo = entry_cod275_antigo.get()
    cod275novo = entry_cod275_novo.get()
    if cod275_antigo == '' or cod275novo == '':
        label_275result.configure(text='Preencha o Código', fg='red')
    else:
        cod275_antigo = int(cod275_antigo)
        cod275novo = int(cod275novo)
        criar_evento275(codigo_evento_copiado=cod275_antigo, codigo_novo_evento=cod275novo, token=token,
                        lista_motivos=lista)
        label_275result.configure(text='Evento Cadastrado', fg='green')

    # Validação Evento 276
    cod276_antigo = entry_cod276_antigo.get()
    cod276novo = entry_cod276_novo.get()
    if cod276_antigo == '' or cod276novo == '':
        label_276result.configure(text='Preencha o Código', fg='red')
    else:
        cod276_antigo = int(cod276_antigo)
        cod276novo = int(cod276novo)
        criar_evento276(codigo_evento_copiado=cod276_antigo, codigo_novo_evento=cod276novo, token=token,
                        lista_motivos=lista)
        label_276result.configure(text='Evento Cadastrado', fg='green')

    # Validação Evento 277
    cod277_antigo = entry_cod277_antigo.get()
    cod277novo = entry_cod277_novo.get()
    if cod277_antigo == '' or cod277novo == '':
        label_277result.configure(text='Preencha o Código', fg='red')
    else:
        cod277_antigo = int(cod277_antigo)
        cod277novo = int(cod277novo)
        criar_evento277(codigo_evento_copiado=cod277_antigo, codigo_novo_evento=cod277novo, token=token,
                        lista_motivos=lista)
        label_277result.configure(text='Evento Cadastrado', fg='green')

    # Validação Evento 278
    cod278_antigo = entry_cod278_antigo.get()
    cod278novo = entry_cod278_novo.get()
    if cod278_antigo == '' or cod278novo == '':
        label_278result.configure(text='Preencha o Código', fg='red')
    else:
        cod278_antigo = int(cod278_antigo)
        cod278novo = int(cod278novo)
        criar_evento278(codigo_evento_copiado=cod278_antigo, codigo_novo_evento=cod278novo, token=token,
                        lista_motivos=lista)
        label_278result.configure(text='Evento Cadastrado', fg='green')

    # Validação Evento 279
    cod279_antigo = entry_cod279_antigo.get()
    cod279novo = entry_cod279_novo.get()
    if cod279_antigo == '' or cod279novo == '':
        label_279result.configure(text='Preencha o Código', fg='red')
    else:
        cod279_antigo = int(cod279_antigo)
        cod279novo = int(cod279novo)
        criar_evento279(codigo_evento_copiado=cod279_antigo, codigo_novo_evento=cod279novo, token=token,
                        lista_motivos=lista)
        label_279result.configure(text='Evento Cadastrado', fg='green')

    # Validação Evento 271
    cod271_antigo = entry_cod271_antigo.get()
    cod271novo = entry_cod271_novo.get()
    if cod271_antigo == '' or cod271novo == '':
        label_271result.configure(text='Preencha o Código', fg='red')
    else:
        cod271_antigo = int(cod271_antigo)
        cod271novo = int(cod271novo)
        criar_evento271(codigo_evento_copiado=cod271_antigo, codigo_novo_evento=cod271novo, token=token,
                        lista_motivos=lista)
        label_271result.configure(text='Evento Cadastrado', fg='green')

    # Validação Evento 272
    cod272_antigo = entry_cod272_antigo.get()
    cod272novo = entry_cod272_novo.get()
    if cod272_antigo == '' or cod272novo == '':
        label_272result.configure(text='Preencha o Código', fg='red')
    else:
        cod272_antigo = int(cod272_antigo)
        cod272novo = int(cod272novo)
        criar_evento272(codigo_evento_copiado=cod272_antigo, codigo_novo_evento=cod272novo, token=token,
                        lista_motivos=lista)
        label_272result.configure(text='Evento Cadastrado', fg='green')

    # Validação Evento 273
    cod273_antigo = entry_cod273_antigo.get()
    cod273novo = entry_cod273_novo.get()
    if cod273_antigo == '' or cod273novo == '':
        label_273result.configure(text='Preencha o Código', fg='red')
    else:
        cod273_antigo = int(cod273_antigo)
        cod273novo = int(cod273novo)
        criar_evento273(codigo_evento_copiado=cod273_antigo, codigo_novo_evento=cod273novo, token=token,
                        lista_motivos=lista)
        label_273result.configure(text='Evento Cadastrado', fg='green')

    # Validação Evento 300
    cod300_antigo = entry_cod300_antigo.get()
    cod300novo = entry_cod300_novo.get()
    if cod300_antigo == '' or cod300novo == '':
        label_300result.configure(text='Preencha o Código', fg='red')
    else:
        cod300_antigo = int(cod300_antigo)
        cod300novo = int(cod300novo)
        criar_evento300(codigo_evento_copiado=cod300_antigo, codigo_novo_evento=cod300novo, token=token,
                        lista_motivos=lista)
        label_300result.configure(text='Evento Cadastrado', fg='green')

    # Validação Evento 301
    cod301_antigo = entry_cod301_antigo.get()
    cod301novo = entry_cod301_novo.get()
    if cod301_antigo == '' or cod301novo == '':
        label_301result.configure(text='Preencha o Código', fg='red')
    else:
        cod301_antigo = int(cod301_antigo)
        cod301novo = int(cod301novo)
        criar_evento301(codigo_evento_copiado=cod301_antigo, codigo_novo_evento=cod301novo, token=token,
                        lista_motivos=lista)
        label_301result.configure(text='Evento Cadastrado', fg='green')

    # Validação Evento 302
    cod302_antigo = entry_cod302_antigo.get()
    cod302novo = entry_cod302_novo.get()
    if cod302_antigo == '' or cod302novo == '':
        label_302result.configure(text='Preencha o Código', fg='red')
    else:
        cod302_antigo = int(cod302_antigo)
        cod302novo = int(cod302novo)
        criar_evento302(codigo_evento_copiado=cod302_antigo, codigo_novo_evento=cod302novo, token=token,
                        lista_motivos=lista)
        label_302result.configure(text='Evento Cadastrado', fg='green')

    # Validação Evento 303
    cod303_antigo = entry_cod303_antigo.get()
    cod303novo = entry_cod303_novo.get()
    if cod303_antigo == '' or cod303novo == '':
        label_303result.configure(text='Preencha o Código', fg='red')
    else:
        cod303_antigo = int(cod303_antigo)
        cod303novo = int(cod303novo)
        criar_evento303(codigo_evento_copiado=cod303_antigo, codigo_novo_evento=cod303novo, token=token,
                        lista_motivos=lista)
        label_303result.configure(text='Evento Cadastrado', fg='green')

    # Validação Evento 304
    cod304_antigo = entry_cod304_antigo.get()
    cod304novo = entry_cod304_novo.get()
    if cod304_antigo == '' or cod304novo == '':
        label_304result.configure(text='Preencha o Código', fg='red')
    else:
        cod304_antigo = int(cod304_antigo)
        cod304novo = int(cod304novo)
        criar_evento304(codigo_evento_copiado=cod304_antigo, codigo_novo_evento=cod304novo, token=token,
                        lista_motivos=lista)
        label_304result.configure(text='Evento Cadastrado', fg='green')


FilialCriciuma = '916e40c6-29d7-4587-b067-d62ea54312e5'
# Programa
janela = tk.Tk()

janela.title('Ferramenta: Criar Eventos Padrões - Rescisão')

labal_titulo = tk.Label(text='Ferramenta para Criar novos eventos Padrões de Rescisão')
labal_titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

label_tk = tk.Label(text='Token da Entidade')
label_tk.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

entry_token = tk.Entry()
entry_token.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky='nsew')

label_semtoken = tk.Label(text='')
label_semtoken.grid(row=1, column=3, padx=10, pady=10, sticky='nsew')

label_padraoAntigo = tk.Label(text='Evento Padrão Antigo')
label_padraoAntigo.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

label_padraoNovo = tk.Label(text='Código Novo Evento')
label_padraoNovo.grid(row=2, column=2, padx=10, pady=10, sticky='nsew')

label_criar270 = tk.Label(text='Criar Evento Padrão 270')
label_criar270.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')
entry_cod270_antigo = tk.Entry()
entry_cod270_antigo.grid(row=3, column=1, padx=10, pady=10, sticky='nsew')
entry_cod270_novo = tk.Entry()
entry_cod270_novo.grid(row=3, column=2, padx=10, pady=10, sticky='nsew')
label_270result = tk.Label(text='')
label_270result.grid(row=3, column=3, padx=10, pady=10, sticky='nsew')

label_criar274 = tk.Label(text='Criar Evento Padrão 274')
label_criar274.grid(row=4, column=0, padx=10, pady=10, sticky='nsew')
entry_cod274_antigo = tk.Entry()
entry_cod274_antigo.grid(row=4, column=1, padx=10, pady=10, sticky='nsew')
entry_cod274_novo = tk.Entry()
entry_cod274_novo.grid(row=4, column=2, padx=10, pady=10, sticky='nsew')
label_274result = tk.Label(text='')
label_274result.grid(row=4, column=3, padx=10, pady=10, sticky='nsew')

label_criar275 = tk.Label(text='Criar Evento Padrão 275')
label_criar275.grid(row=5, column=0, padx=10, pady=10, sticky='nsew')
entry_cod275_antigo = tk.Entry()
entry_cod275_antigo.grid(row=5, column=1, padx=10, pady=10, sticky='nsew')
entry_cod275_novo = tk.Entry()
entry_cod275_novo.grid(row=5, column=2, padx=10, pady=10, sticky='nsew')
label_275result = tk.Label(text='')
label_275result.grid(row=5, column=3, padx=10, pady=10, sticky='nsew')

label_criar276 = tk.Label(text='Criar Evento Padrão 276')
label_criar276.grid(row=6, column=0, padx=10, pady=10, sticky='nsew')
entry_cod276_antigo = tk.Entry()
entry_cod276_antigo.grid(row=6, column=1, padx=10, pady=10, sticky='nsew')
entry_cod276_novo = tk.Entry()
entry_cod276_novo.grid(row=6, column=2, padx=10, pady=10, sticky='nsew')
label_276result = tk.Label(text='')
label_276result.grid(row=6, column=3, padx=10, pady=10, sticky='nsew')

label_criar277 = tk.Label(text='Criar Evento Padrão 277')
label_criar277.grid(row=7, column=0, padx=10, pady=10, sticky='nsew')
entry_cod277_antigo = tk.Entry()
entry_cod277_antigo.grid(row=7, column=1, padx=10, pady=10, sticky='nsew')
entry_cod277_novo = tk.Entry()
entry_cod277_novo.grid(row=7, column=2, padx=10, pady=10, sticky='nsew')
label_277result = tk.Label(text='')
label_277result.grid(row=7, column=3, padx=10, pady=10, sticky='nsew')

label_criar278 = tk.Label(text='Criar Evento Padrão 278')
label_criar278.grid(row=8, column=0, padx=10, pady=10, sticky='nsew')
entry_cod278_antigo = tk.Entry()
entry_cod278_antigo.grid(row=8, column=1, padx=10, pady=10, sticky='nsew')
entry_cod278_novo = tk.Entry()
entry_cod278_novo.grid(row=8, column=2, padx=10, pady=10, sticky='nsew')
label_278result = tk.Label(text='')
label_278result.grid(row=8, column=3, padx=10, pady=10, sticky='nsew')

label_criar279 = tk.Label(text='Criar Evento Padrão 279')
label_criar279.grid(row=9, column=0, padx=10, pady=10, sticky='nsew')
entry_cod279_antigo = tk.Entry()
entry_cod279_antigo.grid(row=9, column=1, padx=10, pady=10, sticky='nsew')
entry_cod279_novo = tk.Entry()
entry_cod279_novo.grid(row=9, column=2, padx=10, pady=10, sticky='nsew')
label_279result = tk.Label(text='')
label_279result.grid(row=9, column=3, padx=10, pady=10, sticky='nsew')

label_criar271 = tk.Label(text='Criar Evento Padrão 271')
label_criar271.grid(row=10, column=0, padx=10, pady=10, sticky='nsew')
entry_cod271_antigo = tk.Entry()
entry_cod271_antigo.grid(row=10, column=1, padx=10, pady=10, sticky='nsew')
entry_cod271_novo = tk.Entry()
entry_cod271_novo.grid(row=10, column=2, padx=10, pady=10, sticky='nsew')
label_271result = tk.Label(text='')
label_271result.grid(row=10, column=3, padx=10, pady=10, sticky='nsew')

label_criar272 = tk.Label(text='Criar Evento Padrão 272')
label_criar272.grid(row=11, column=0, padx=10, pady=10, sticky='nsew')
entry_cod272_antigo = tk.Entry()
entry_cod272_antigo.grid(row=11, column=1, padx=10, pady=10, sticky='nsew')
entry_cod272_novo = tk.Entry()
entry_cod272_novo.grid(row=11, column=2, padx=10, pady=10, sticky='nsew')
label_272result = tk.Label(text='')
label_272result.grid(row=11, column=3, padx=10, pady=10, sticky='nsew')

label_criar273 = tk.Label(text='Criar Evento Padrão 273')
label_criar273.grid(row=12, column=0, padx=10, pady=10, sticky='nsew')
entry_cod273_antigo = tk.Entry()
entry_cod273_antigo.grid(row=12, column=1, padx=10, pady=10, sticky='nsew')
entry_cod273_novo = tk.Entry()
entry_cod273_novo.grid(row=12, column=2, padx=10, pady=10, sticky='nsew')
label_273result = tk.Label(text='')
label_273result.grid(row=12, column=3, padx=10, pady=10, sticky='nsew')

label_criar300 = tk.Label(text='Criar Evento Padrão 300')
label_criar300.grid(row=13, column=0, padx=10, pady=10, sticky='nsew')
entry_cod300_antigo = tk.Entry()
entry_cod300_antigo.grid(row=13, column=1, padx=10, pady=10, sticky='nsew')
entry_cod300_novo = tk.Entry()
entry_cod300_novo.grid(row=13, column=2, padx=10, pady=10, sticky='nsew')
label_300result = tk.Label(text='')
label_300result.grid(row=13, column=3, padx=10, pady=10, sticky='nsew')

label_criar301 = tk.Label(text='Criar Evento Padrão 301')
label_criar301.grid(row=14, column=0, padx=10, pady=10, sticky='nsew')
entry_cod301_antigo = tk.Entry()
entry_cod301_antigo.grid(row=14, column=1, padx=10, pady=10, sticky='nsew')
entry_cod301_novo = tk.Entry()
entry_cod301_novo.grid(row=14, column=2, padx=10, pady=10, sticky='nsew')
label_301result = tk.Label(text='')
label_301result.grid(row=14, column=3, padx=10, pady=10, sticky='nsew')

label_criar302 = tk.Label(text='Criar Evento Padrão 302')
label_criar302.grid(row=15, column=0, padx=10, pady=10, sticky='nsew')
entry_cod302_antigo = tk.Entry()
entry_cod302_antigo.grid(row=15, column=1, padx=10, pady=10, sticky='nsew')
entry_cod302_novo = tk.Entry()
entry_cod302_novo.grid(row=15, column=2, padx=10, pady=10, sticky='nsew')
label_302result = tk.Label(text='')
label_302result.grid(row=15, column=3, padx=10, pady=10, sticky='nsew')

label_criar303 = tk.Label(text='Criar Evento Padrão 303')
label_criar303.grid(row=16, column=0, padx=10, pady=10, sticky='nsew')
entry_cod303_antigo = tk.Entry()
entry_cod303_antigo.grid(row=16, column=1, padx=10, pady=10, sticky='nsew')
entry_cod303_novo = tk.Entry()
entry_cod303_novo.grid(row=16, column=2, padx=10, pady=10, sticky='nsew')
label_303result = tk.Label(text='')
label_303result.grid(row=16, column=3, padx=10, pady=10, sticky='nsew')

label_criar304 = tk.Label(text='Criar Evento Padrão 304')
label_criar304.grid(row=17, column=0, padx=10, pady=10, sticky='nsew')
entry_cod304_antigo = tk.Entry()
entry_cod304_antigo.grid(row=17, column=1, padx=10, pady=10, sticky='nsew')
entry_cod304_novo = tk.Entry()
entry_cod304_novo.grid(row=17, column=2, padx=10, pady=10, sticky='nsew')
label_304result = tk.Label(text='')
label_304result.grid(row=17, column=3, padx=10, pady=10, sticky='nsew')

botao_cadastrarEventos = tk.Button(text='Cadastrar Eventos', command=cadastrar_eventos)
botao_cadastrarEventos.grid(row=17, column=4, padx=10, pady=10, sticky='nsew')

janela.mainloop()
