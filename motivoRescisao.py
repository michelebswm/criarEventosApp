import requests


def motivo_rescisao(token):
    hasNext = True
    offset = 0
    limit = 100
    page = 1
    lista_motivos = []
    while hasNext:
        url = f'https://pessoal.cloud.betha.com.br/service-layer/v1/api/motivo-rescisao?offset={offset}&limit={limit}'
        headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            print('Erro: ', response.text)
        response = response.json()
        offset = limit * page
        page += 1
        hasNext = response['hasNext']

        for item in response['content']:
            dic_id_motivo = {
                'id': item['id']
            }
            lista_motivos.append(dic_id_motivo)
    return lista_motivos

# print('Motivos Rescisão {}'.format(lista_motivos))