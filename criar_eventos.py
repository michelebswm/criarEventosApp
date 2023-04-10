import json
import requests

import sys


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

def criar_evento270(codigo_evento_copiado, codigo_novo_evento, token, lista_motivos):
    hasNext = True
    offset = 0
    limit = 100
    page = 1

    # Importando formula do evento 270-HORAS NORMAIS NA RESCISAO
    with open('270-HORASNORMAISNARESCISAO.groovy', 'r') as f:
        evento270 = f.read()

    while hasNext:
        url = f'https://pessoal.cloud.betha.com.br/service-layer/v1/api/configuracao-evento?offset={offset}&limit={limit}'
        headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            print('Erro: ', response.text)
        response = response.json()
        offset = limit * page
        page += 1
        hasNext = response['hasNext']
        for item in response['content']:
            if item['codigo'] == codigo_evento_copiado:
                print(item)
                del item['id']
                del item['version']
                item['codigo'] = codigo_novo_evento
                item['descricao'] = 'HORAS NORMAIS NA RESCISÃO'
                item['inicioVigencia'] = '2022-08'
                item['naturezaRubrica'] = 'SALDO_SALARIO_RESCISAO'
                item['codigoEsocial'] = codigo_novo_evento
                item['observacao'] = 'HORAS NORMAIS NA RESCISÃO'
                del item['script']['id']
                item['script']['content'] = formata_texto(evento270)
                # Verifica se existe as configurações de processamento
                configuracaoProcessamentos = item['configuracaoProcessamentos']
                if 'MENSAL' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['MENSAL']['subTipos'] = []
                    item['configuracaoProcessamentos']['MENSAL']['motivosRescisao'] = []
                if 'DECIMO_TERCEIRO_SALARIO' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['DECIMO_TERCEIRO_SALARIO']['subTipos'] = []
                    item['configuracaoProcessamentos']['DECIMO_TERCEIRO_SALARIO']['motivosRescisao'] = []
                if 'FERIAS' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['FERIAS']['subTipos'] = []
                    item['configuracaoProcessamentos']['FERIAS']['motivosRescisao'] = []
                if 'RESCISAO' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['RESCISAO']['subTipos'] = ['INTEGRAL']
                    item['configuracaoProcessamentos']['RESCISAO']['motivosRescisao'] = lista_motivos
                else:
                    # Se não possuir a Key RESCISAO inclui
                    configuracaoProcessamentos['RESCISAO'] = {'tipoProcessamento': 'RESCISAO',
                                                              'subTipos': ['INTEGRAL'],
                                                              'motivosRescisao': lista_motivos}
                item['historicos'] = []
                item['camposAdicionais'] = []
                item['formula'] = formata_texto(evento270)

                payloadPostEvento = json.dumps([
                    {
                        "conteudo": item
                    }
                ])
                print('-'*25,'POST','-'*25)
                print(payloadPostEvento)
                print('-'*56)

                envia_verifica_lote(operacao='POST', bearer=token, payload=payloadPostEvento, api='configuracao-evento')

def criar_evento274(codigo_evento_copiado, codigo_novo_evento, token, lista_motivos):
    hasNext = True
    offset = 0
    limit = 100
    page = 1

    # Importando formula do evento 274-13 SALARIO INTEGRAL NA RESCISAO
    with open('274-13SALARIOINTEGRALNARESCISAO.groovy', 'r') as f:
        evento274 = f.read()

    while hasNext:
        url = f'https://pessoal.cloud.betha.com.br/service-layer/v1/api/configuracao-evento?offset={offset}&limit={limit}'
        headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            print('Erro: ', response.text)
        response = response.json()
        offset = limit * page
        page += 1
        hasNext = response['hasNext']
        for item in response['content']:
            if item['codigo'] == codigo_evento_copiado:
                print(item)
                del item['id']
                del item['version']
                item['codigo'] = codigo_novo_evento
                item['descricao'] = '13ª SALÁRIO INTEGRAL NA RESCISÃO'
                item['inicioVigencia'] = '2022-08'
                item['naturezaRubrica'] = 'DECIMO_TERCEIRO_SALARIO_PROPORCIONAL_RESCISAO'
                item['codigoEsocial'] = codigo_novo_evento
                item['observacao'] = '13º SALÁRIO INTEGRAL NA RESCISÃO'
                del item['script']['id']
                item['script']['content'] = formata_texto(evento274)
                # Verifica se existe as configurações de processamento
                configuracaoProcessamentos = item['configuracaoProcessamentos']
                if 'MENSAL' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['MENSAL']['subTipos'] = []
                    item['configuracaoProcessamentos']['MENSAL']['motivosRescisao'] = []
                if 'DECIMO_TERCEIRO_SALARIO' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['DECIMO_TERCEIRO_SALARIO']['subTipos'] = []
                    item['configuracaoProcessamentos']['DECIMO_TERCEIRO_SALARIO']['motivosRescisao'] = []
                if 'FERIAS' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['FERIAS']['subTipos'] = []
                    item['configuracaoProcessamentos']['FERIAS']['motivosRescisao'] = []
                if 'RESCISAO' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['RESCISAO']['subTipos'] = ['INTEGRAL']
                    item['configuracaoProcessamentos']['RESCISAO']['motivosRescisao'] = lista_motivos
                else:
                    # Se não possuir a Key RESCISAO inclui
                    configuracaoProcessamentos['RESCISAO'] = {'tipoProcessamento': 'RESCISAO',
                                                              'subTipos': ['INTEGRAL'],
                                                              'motivosRescisao': lista_motivos}
                item['historicos'] = []
                item['camposAdicionais'] = []
                item['formula'] = formata_texto(evento274)

                payloadPostEvento = json.dumps([
                    {
                        "conteudo": item
                    }
                ])
                print('-'*25,'POST','-'*25)
                print(payloadPostEvento)
                print('-'*56)

                envia_verifica_lote(operacao='POST', bearer=token, payload=payloadPostEvento, api='configuracao-evento')

def criar_evento275(codigo_evento_copiado, codigo_novo_evento, token, lista_motivos):
    hasNext = True
    offset = 0
    limit = 100
    page = 1

    # Importando formula do evento 275-MEDIA HORAS 13 SALARIO NA RESCISAO
    with open('275-MEDIAHORAS13SALARIONARESCISAO.groovy', 'r') as f:
        evento275 = f.read()

    while hasNext:
        url = f'https://pessoal.cloud.betha.com.br/service-layer/v1/api/configuracao-evento?offset={offset}&limit={limit}'
        headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            print('Erro: ', response.text)
        response = response.json()
        offset = limit * page
        page += 1
        hasNext = response['hasNext']
        for item in response['content']:
            if item['codigo'] == codigo_evento_copiado:
                print(item)
                del item['id']
                del item['version']
                item['codigo'] = codigo_novo_evento
                item['descricao'] = 'MÉDIA HORAS 13º SALÁRIO RESCISÃO'
                item['inicioVigencia'] = '2022-08'
                item['naturezaRubrica'] = 'DECIMO_TERCEIRO_SALARIO_PROPORCIONAL_RESCISAO'
                item['codigoEsocial'] = codigo_novo_evento
                item['observacao'] = 'MÉDIA HORAS 13º SALÁRIO RESCISÃO'
                del item['script']['id']
                item['script']['content'] = formata_texto(evento275)
                # Verifica se existe as configurações de processamento
                configuracaoProcessamentos = item['configuracaoProcessamentos']
                if 'MENSAL' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['MENSAL']['subTipos'] = []
                    item['configuracaoProcessamentos']['MENSAL']['motivosRescisao'] = []
                if 'DECIMO_TERCEIRO_SALARIO' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['DECIMO_TERCEIRO_SALARIO']['subTipos'] = []
                    item['configuracaoProcessamentos']['DECIMO_TERCEIRO_SALARIO']['motivosRescisao'] = []
                if 'FERIAS' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['FERIAS']['subTipos'] = []
                    item['configuracaoProcessamentos']['FERIAS']['motivosRescisao'] = []
                if 'RESCISAO' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['RESCISAO']['subTipos'] = ['INTEGRAL']
                    item['configuracaoProcessamentos']['RESCISAO']['motivosRescisao'] = lista_motivos
                else:
                    # Se não possuir a Key RESCISAO inclui
                    configuracaoProcessamentos['RESCISAO'] = {'tipoProcessamento': 'RESCISAO',
                    'subTipos': ['INTEGRAL'], 'motivosRescisao': lista_motivos}
                item['historicos'] = []
                item['camposAdicionais'] = []
                item['formula'] = formata_texto(evento275)

                payloadPostEvento = json.dumps([
                    {
                        "conteudo": item
                    }
                ])
                print('-'*25,'POST','-'*25)
                print(payloadPostEvento)
                print('-'*56)

                envia_verifica_lote(operacao='POST', bearer=token, payload=payloadPostEvento, api='configuracao-evento')

def criar_evento276(codigo_evento_copiado, codigo_novo_evento, token, lista_motivos):
    hasNext = True
    offset = 0
    limit = 100
    page = 1

    # Importando formula do evento 276 - MÉDIA VALOR 13º SALÁRIO  NA RESCISÃO
    with open('276-MEDIAVALOR13SALARIONARESCISAO.groovy', 'r') as f:
        evento276 = f.read()

    while hasNext:
        url = f'https://pessoal.cloud.betha.com.br/service-layer/v1/api/configuracao-evento?offset={offset}&limit={limit}'
        headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            print('Erro: ', response.text)
        response = response.json()
        offset = limit * page
        page += 1
        hasNext = response['hasNext']
        for item in response['content']:
            if item['codigo'] == codigo_evento_copiado:
                print(item)
                del item['id']
                del item['version']
                item['codigo'] = codigo_novo_evento
                item['descricao'] = 'MÉDIA VALOR 13º SALÁRIO  NA RESCISÃO'
                item['inicioVigencia'] = '2022-08'
                item['naturezaRubrica'] = 'DECIMO_TERCEIRO_SALARIO_PROPORCIONAL_RESCISAO'
                item['codigoEsocial'] = codigo_novo_evento
                item['observacao'] = 'MÉDIA VALOR 13º SALÁRIO  NA RESCISÃO'
                del item['script']['id']
                item['script']['content'] = formata_texto(evento276)
                # Verifica se existe as configurações de processamento
                configuracaoProcessamentos = item['configuracaoProcessamentos']
                if 'MENSAL' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['MENSAL']['subTipos'] = []
                    item['configuracaoProcessamentos']['MENSAL']['motivosRescisao'] = []
                if 'DECIMO_TERCEIRO_SALARIO' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['DECIMO_TERCEIRO_SALARIO']['subTipos'] = []
                    item['configuracaoProcessamentos']['DECIMO_TERCEIRO_SALARIO']['motivosRescisao'] = []
                if 'FERIAS' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['FERIAS']['subTipos'] = []
                    item['configuracaoProcessamentos']['FERIAS']['motivosRescisao'] = []
                if 'RESCISAO' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['RESCISAO']['subTipos'] = ['INTEGRAL']
                    item['configuracaoProcessamentos']['RESCISAO']['motivosRescisao'] = lista_motivos
                else:
                    # Se não possuir a Key RESCISAO inclui
                    configuracaoProcessamentos['RESCISAO'] = {'tipoProcessamento': 'RESCISAO',
                    'subTipos': ['INTEGRAL'], 'motivosRescisao': lista_motivos}
                item['historicos'] = []
                item['camposAdicionais'] = []
                item['formula'] = formata_texto(evento276)

                payloadPostEvento = json.dumps([
                    {
                        "conteudo": item
                    }
                ])
                print('-'*25,'POST','-'*25)
                print(payloadPostEvento)
                print('-'*56)

                envia_verifica_lote(operacao='POST', bearer=token, payload=payloadPostEvento, api='configuracao-evento')

def criar_evento277(codigo_evento_copiado, codigo_novo_evento, token, lista_motivos):
    hasNext = True
    offset = 0
    limit = 100
    page = 1

    # Importando formula do evento 277-VANTAGENS 13º SALÁRIO NA RESCISÃO
    with open('277-VANTAGENS13SALARIONARESCISAO.groovy', 'r') as f:
        evento277 = f.read()

    while hasNext:
        url = f'https://pessoal.cloud.betha.com.br/service-layer/v1/api/configuracao-evento?offset={offset}&limit={limit}'
        headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            print('Erro: ', response.text)
        response = response.json()
        offset = limit * page
        page += 1
        hasNext = response['hasNext']
        for item in response['content']:
            if item['codigo'] == codigo_evento_copiado:
                print(item)
                del item['id']
                del item['version']
                item['codigo'] = codigo_novo_evento
                item['descricao'] = 'VANTAGENS 13º SALÁRIO NA RESCISÃO'
                item['inicioVigencia'] = '2022-08'
                item['naturezaRubrica'] = 'DECIMO_TERCEIRO_SALARIO_PROPORCIONAL_RESCISAO'
                item['codigoEsocial'] = codigo_novo_evento
                item['observacao'] = 'VANTAGENS 13º SALÁRIO NA RESCISÃO'
                del item['script']['id']
                item['script']['content'] = formata_texto(evento277)
                # Verifica se existe as configurações de processamento
                configuracaoProcessamentos = item['configuracaoProcessamentos']
                if 'MENSAL' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['MENSAL']['subTipos'] = []
                    item['configuracaoProcessamentos']['MENSAL']['motivosRescisao'] = []
                if 'DECIMO_TERCEIRO_SALARIO' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['DECIMO_TERCEIRO_SALARIO']['subTipos'] = []
                    item['configuracaoProcessamentos']['DECIMO_TERCEIRO_SALARIO']['motivosRescisao'] = []
                if 'FERIAS' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['FERIAS']['subTipos'] = []
                    item['configuracaoProcessamentos']['FERIAS']['motivosRescisao'] = []
                if 'RESCISAO' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['RESCISAO']['subTipos'] = ['INTEGRAL']
                    item['configuracaoProcessamentos']['RESCISAO']['motivosRescisao'] = lista_motivos
                else:
                    # Se não possuir a Key RESCISAO inclui
                    configuracaoProcessamentos['RESCISAO'] = {'tipoProcessamento': 'RESCISAO',
                    'subTipos': ['INTEGRAL'], 'motivosRescisao': lista_motivos}
                item['historicos'] = []
                item['camposAdicionais'] = []
                item['formula'] = formata_texto(evento277)

                payloadPostEvento = json.dumps([
                    {
                        "conteudo": item
                    }
                ])
                print('-'*25,'POST','-'*25)
                print(payloadPostEvento)
                print('-'*56)

                envia_verifica_lote(operacao='POST', bearer=token, payload=payloadPostEvento, api='configuracao-evento')

def criar_evento278(codigo_evento_copiado, codigo_novo_evento, token, lista_motivos):
    hasNext = True
    offset = 0
    limit = 100
    page = 1

    # Importando formula do evento 278 – MÉDIA PERCENTUAL 13º SALÁRIO NA RESCISÃO
    with open('278-MEDIAPERCENTUAL13SALARIONARESCISAO.groovy', 'r') as f:
        evento278 = f.read()

    while hasNext:
        url = f'https://pessoal.cloud.betha.com.br/service-layer/v1/api/configuracao-evento?offset={offset}&limit={limit}'
        headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            print('Erro: ', response.text)
        response = response.json()
        offset = limit * page
        page += 1
        hasNext = response['hasNext']
        for item in response['content']:
            if item['codigo'] == codigo_evento_copiado:
                print(item)
                del item['id']
                del item['version']
                item['codigo'] = codigo_novo_evento
                item['descricao'] = 'VANTAGENS 13º SALÁRIO NA RESCISÃO'
                item['inicioVigencia'] = '2022-08'
                item['naturezaRubrica'] = 'DECIMO_TERCEIRO_SALARIO_PROPORCIONAL_RESCISAO'
                item['codigoEsocial'] = codigo_novo_evento
                item['observacao'] = 'VANTAGENS 13º SALÁRIO NA RESCISÃO'
                del item['script']['id']
                item['script']['content'] = formata_texto(evento278)
                # Verifica se existe as configurações de processamento
                configuracaoProcessamentos = item['configuracaoProcessamentos']
                if 'MENSAL' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['MENSAL']['subTipos'] = []
                    item['configuracaoProcessamentos']['MENSAL']['motivosRescisao'] = []
                if 'DECIMO_TERCEIRO_SALARIO' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['DECIMO_TERCEIRO_SALARIO']['subTipos'] = []
                    item['configuracaoProcessamentos']['DECIMO_TERCEIRO_SALARIO']['motivosRescisao'] = []
                if 'FERIAS' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['FERIAS']['subTipos'] = []
                    item['configuracaoProcessamentos']['FERIAS']['motivosRescisao'] = []
                if 'RESCISAO' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['RESCISAO']['subTipos'] = ['INTEGRAL']
                    item['configuracaoProcessamentos']['RESCISAO']['motivosRescisao'] = lista_motivos
                else:
                    # Se não possuir a Key RESCISAO inclui
                    configuracaoProcessamentos['RESCISAO'] = {'tipoProcessamento': 'RESCISAO',
                    'subTipos': ['INTEGRAL'], 'motivosRescisao': lista_motivos}
                item['historicos'] = []
                item['camposAdicionais'] = []
                item['formula'] = formata_texto(evento278)

                payloadPostEvento = json.dumps([
                    {
                        "conteudo": item
                    }
                ])
                print('-'*25,'POST','-'*25)
                print(payloadPostEvento)
                print('-'*56)

                envia_verifica_lote(operacao='POST', bearer=token, payload=payloadPostEvento, api='configuracao-evento')

def criar_evento279(codigo_evento_copiado, codigo_novo_evento, token, lista_motivos):
    hasNext = True
    offset = 0
    limit = 100
    page = 1

    # Importando formula do evento 279 – ADIANTAMENTO 13º SALÁRIO NA RESCISÃO
    with open('279-ADIANTAMENTO13SALARIONARESCISAO.groovy', 'r') as f:
        evento279 = f.read()

    while hasNext:
        url = f'https://pessoal.cloud.betha.com.br/service-layer/v1/api/configuracao-evento?offset={offset}&limit={limit}'
        headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            print('Erro: ', response.text)
        response = response.json()
        offset = limit * page
        page += 1
        hasNext = response['hasNext']
        for item in response['content']:
            if item['codigo'] == codigo_evento_copiado:
                print(item)
                del item['id']
                del item['version']
                item['codigo'] = codigo_novo_evento
                item['descricao'] = 'ADIANTAMENTO 13º SALÁRIO NA RESCISÃO'
                item['inicioVigencia'] = '2022-08'
                item['naturezaRubrica'] = 'DECIMO_TERCEIRO_SALARIO_PROPORCIONAL_RESCISAO'
                item['codigoEsocial'] = codigo_novo_evento
                item['observacao'] = 'ADIANTAMENTO 13º SALÁRIO NA RESCISÃO'
                del item['script']['id']
                item['script']['content'] = formata_texto(evento279)
                # Verifica se existe as configurações de processamento
                configuracaoProcessamentos = item['configuracaoProcessamentos']
                if 'MENSAL' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['MENSAL']['subTipos'] = []
                    item['configuracaoProcessamentos']['MENSAL']['motivosRescisao'] = []
                if 'DECIMO_TERCEIRO_SALARIO' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['DECIMO_TERCEIRO_SALARIO']['subTipos'] = []
                    item['configuracaoProcessamentos']['DECIMO_TERCEIRO_SALARIO']['motivosRescisao'] = []
                if 'FERIAS' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['FERIAS']['subTipos'] = []
                    item['configuracaoProcessamentos']['FERIAS']['motivosRescisao'] = []
                if 'RESCISAO' in configuracaoProcessamentos:
                    item['configuracaoProcessamentos']['RESCISAO']['subTipos'] = ['INTEGRAL']
                    item['configuracaoProcessamentos']['RESCISAO']['motivosRescisao'] = lista_motivos
                else:
                    # Se não possuir a Key RESCISAO inclui
                    configuracaoProcessamentos['RESCISAO'] = {'tipoProcessamento': 'RESCISAO',
                    'subTipos': ['INTEGRAL'], 'motivosRescisao': lista_motivos}
                item['historicos'] = []
                item['camposAdicionais'] = []
                item['formula'] = formata_texto(evento279)

                payloadPostEvento = json.dumps([
                    {
                        "conteudo": item
                    }
                ])
                print('-'*25,'POST','-'*25)
                print(payloadPostEvento)
                print('-'*56)

                envia_verifica_lote(operacao='POST', bearer=token, payload=payloadPostEvento, api='configuracao-evento')

# Se refere ao Evento 270 – HORAS NORMAIS NA RESCISÃO - FORMULA PADRÃO
# Esse evento substitui o evento 1 – HORAS NORMAIS no processamento de rescisão.
# Desta forma no codigo_evento_copiado informe o código do evento antigo no banco do cliente que seria o 1
# E no campo codigo_novo_evento informe o código do novo evento a ser criado
# criar_evento270(codigo_evento_copiado=1, codigo_novo_evento=385)

# Se refere ao Evento 274 – 13º SALÁRIO INTEGRAL NA RESCISÃO - FORMULA PADRÃO
# Esse evento substitui o evento 25 – 13º SALÁRIO INTEGRAL no processamento de rescisão.
# Desta forma no codigo_evento_copiado informe o código do evento antigo no banco do cliente que seria o 25
# E no campo codigo_novo_evento informe o código do novo evento a ser criado
# criar_evento274(codigo_evento_copiado=25, codigo_novo_evento=386)

# Se refere ao Evento 275 – MÉDIA HORAS 13º SALÁRIO NA RESCISÃO
# Esse evento substitui o evento 28 – MÉDIA HORAS 13º SALÁRIO  no processamento de rescisão.
# Desta forma no codigo_evento_copiado informe o código do evento antigo no banco do cliente que seria o 28
# E no campo codigo_novo_evento informe o código do novo evento a ser criado
# criar_evento275(codigo_evento_copiado=28, codigo_novo_evento=387)

# Se refere ao Evento 276 – MÉDIA VALOR 13º SALÁRIO NA RESCISÃO
# Esse evento substitui o evento 29 – MÉDIA VALOR 13 SALÁRIO  no processamento de rescisão.
# Desta forma no codigo_evento_copiado informe o código do evento antigo no banco do cliente que seria o 29
# E no campo codigo_novo_evento informe o código do novo evento a ser criado
# criar_evento276(codigo_evento_copiado=29, codigo_novo_evento=388)

# Se refere ao Evento 277 – VANTAGENS 13º SALÁRIO NA RESCISÃO
# Esse evento substitui o evento 30 – VANTAGENS 13º SALÁRIO  no processamento de rescisão.
# Desta forma no codigo_evento_copiado informe o código do evento antigo no banco do cliente que seria o 30
# E no campo codigo_novo_evento informe o código do novo evento a ser criado
# criar_evento277(codigo_evento_copiado=30, codigo_novo_evento=389)

# Se refere ao Evento 278 – MÉDIA PERCENTUAL 13º SALÁRIO NA RESCISÃO
# Esse evento substitui o evento 233 – MÉDIA PERCENTUAL 13º SALÁRIO  no processamento de rescisão.
# Desta forma no codigo_evento_copiado informe o código do evento antigo no banco do cliente que seria o 233
# E no campo codigo_novo_evento informe o código do novo evento a ser criado
# criar_evento278(codigo_evento_copiado=320, codigo_novo_evento=390)

# Se refere ao Evento 279 – ADIANTAMENTO 13º SALÁRIO NA RESCISÃO
# Esse evento substitui o evento 43 – ADIANTAMENTO 13º SALÁRIO  no processamento de rescisão.
# Desta forma no codigo_evento_copiado informe o código do evento antigo no banco do cliente que seria o 43
# E no campo codigo_novo_evento informe o código do novo evento a ser criado
# criar_evento279(codigo_evento_copiado=43, codigo_novo_evento=391)