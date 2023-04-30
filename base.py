import requests
import json
import pandas as pd

# Define as informações que você precisa coletar
info = ['Nome', 'Telefone', 'Fonte', 'Cidade', 'Email', 'Modalidade', 'Responsavel']

# Cria uma lista vazia para cada coluna do DataFrame
ids = []
nomes = []
emails = []

def crm_b_id_nome_email():
    
    for pages in range(1, 537):
        
        # Faz a requisição GET para o CRM B
        url_b = f'https://sisweb-api.azurewebsites.net/api/corretores?Pagina={pages}&RegistrosPorPagina=515&SomenteAtivos=true&IncluirPessoaJuridica=true&IncluirPessoaFisica=true'

        headers_b = {
        'accept': 'application/json',
        'ApiKey': '50e50157-3ed1-458c-9bf3-787ada1af378'
        }
        response_b = requests.get(url_b, headers=headers_b)

        json_response_b = response_b.json()
        data = json.dumps(json_response_b)
        data = json.loads(data)

        result = data['result']['collection']

        for i in result:
            
            _id = i['id']
            _nome = i['nome']
            #_telefone = i['telefones']
            #_endereco = i['enderecos']
            _email = i['email']
            #_modalidade = i['detalhes']
            
            #print(f'Id: {_id} | Nome: {_nome}  | E-mail: {_email} ')
            
            # Adiciona os valores às listas correspondentes
            ids.append(_id)
            nomes.append(_nome)
            emails.append(_email)
            
    # Cria um DataFrame com as listas criadas anteriormente
    df = pd.DataFrame({'ID Assistente Corretor': ids, 'Nome': nomes, 'E-mail': emails})

    # Salva o DataFrame em um arquivo Excel
    df.to_excel('corretores_painel_do_corretor.xlsx', index=False)

def get_producoes():
    
    data_inicial = 1
    data_final = 3
    
    for pages_corretores in range(1,100):
        
        # Faz a requisição GET para o CRM B
        producoes_url_b = f'https://sisweb-api.azurewebsites.net/api/producoes?Pagina=1&RegistrosPorPagina=100&dtInicio={data_final}%2F01%2F2023&dtFinal={data_final}%2F01%2F2023'

        headers_b = {
        'accept': 'application/json',
        'ApiKey': '50e50157-3ed1-458c-9bf3-787ada1af378'
        }
        response_b = requests.get(producoes_url_b, headers=headers_b)

        json_response_b = response_b.json()
        data_producoes = json.dumps(json_response_b)
        data_producoes = json.loads(data_producoes)
        
        result_producoes = data_producoes['result']['collection']
        result_corretores = data_producoes['result']['collection']['corretor']
        
        for data, id_corretor in result_producoes, result_corretores:
            
            _id_corretor = id_corretor['id']
            _nome_corretor = id_corretor['nome']
            
            
            _id_ = data['id']
            segurado = data['segurado']
            modalidade = data['modalidade']
            
            
            print(f'Resultado porduções: id{_id_} Nome: {segurado} Modalidade: {modalidade}')
            print(f'Informacoes corretor: Id corretor: {_id_corretor} Nome do corretor: {_nome_corretor}')
        
        data_inicial += 3
        data_final += 3
            

#crm_b_id_nome_email()
get_producoes()

'''
# Compartilha as informações coletadas com o CRM A
url_a = 'https://sisweb-api.azurewebsites.net/api/indicacoes'
headers = {
    'accept': 'application/json',
    'ApiKey': '50e50157-3ed1-458c-9bf3-787ada1af378'
    }
for item in info_b:
    payload = json.dumps(item)
    response_a = requests.post(url_a, headers=headers_a, data=payload)
    print(response_a.status_code)

'''
