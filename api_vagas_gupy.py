from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import re

app = Flask(__name__)

def extrair_vagas_programa_thor(page_number=1, expertise=None, city=None):
    base_url = f'https://programathor.com.br/jobs/page/{page_number}'
    if expertise:
        base_url += f'?expertise={expertise}'
    if city:
        base_url = f'https://programathor.com.br/jobs-city/{city}'
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    vagas = soup.find_all('div', class_='cell-list')

    lista_vagas = []

    for vaga in vagas:
        nome_vaga_element = vaga.find('h3', class_='text-24')
        if nome_vaga_element:
            # Remover qualquer elemento filho com a classe 'new-label'
            for span in nome_vaga_element.find_all('span', class_='new-label'):
                span.extract()
            nome_vaga = nome_vaga_element.get_text(strip=True)
        else:
            continue  

        outras_informacoes_element = vaga.find('div', class_='cell-list-content-icon')
        if outras_informacoes_element:
            outras_informacoes = outras_informacoes_element.find_all('span')
            empresa = outras_informacoes[0].get_text(strip=True)
            localizacao = outras_informacoes[1].get_text(strip=True)
            tipo_empresa = outras_informacoes[2].get_text(strip=True)
            salario = outras_informacoes[3].get_text(strip=True)      
            nivel = outras_informacoes[4].get_text(strip=True)

            # Procurar por qualquer texto que identifique o tipo de contrato
            tipo_contrato = ""
            for span in outras_informacoes:
                if "PJ" in span.get_text(strip=True) or "CLT" in span.get_text(strip=True):
                    tipo_contrato = span.get_text(strip=True)
                    break

            link_vaga_element = vaga.find('a')
            link_vaga = "https://programathor.com.br" + link_vaga_element['href'] if link_vaga_element and 'href' in link_vaga_element.attrs else "Link indisponível"
            # Extrair o ID da empresa da URL
            vaga_id = re.search(r'/jobs/(\d+)', link_vaga).group(1) if link_vaga else "ID indisponível"
        else:
            empresa = "Informação indisponível"
            localizacao = "Informação indisponível"
            salario = "Informação indisponível"
            nivel = "Informação indisponível"
            tipo_contrato = "Informação indisponível"
            link_vaga = "Link indisponível"
            tipo_empresa = "Informação indisponível"
            vaga_id = "ID indisponível"

        data_publicacao_element = vaga.find('span', class_='new-label')
        data_publicacao = "Nova" if data_publicacao_element else "Informação indisponível"

        lista_vagas.append({
            "nome_vaga": nome_vaga,
            "empresa": empresa,
            "vaga_id": vaga_id,  # Adicionando o ID da empresa
            "localizacao": localizacao,
            "tipo_contrato": tipo_contrato,
            "salario": salario,
            "nivel": nivel,
            "data_publicacao": data_publicacao,
            "link_vaga": link_vaga,
            "tipo_empresa": tipo_empresa
        })

    return lista_vagas

@app.route('/vagas', methods=['GET'])
def obter_vagas():
    page_number = request.args.get('page', default=1, type=int)
    expertise = request.args.get('expertise')
    city = request.args.get('city')
    vagas = extrair_vagas_programa_thor(page_number, expertise, city)
    # Verificar se todas as informações de todas as vagas estão indisponíveis
    if all(vaga == {"data_publicacao": "Informação indisponível",
                    "empresa": "Informação indisponível",
                    "link_vaga": "Link indisponível",
                    "localizacao": "Informação indisponível",
                    "nivel": "Informação indisponível",
                    "nome_vaga": "Informação indisponível",
                    "salario": "Informação indisponível",
                    "tipo_contrato": "Informação indisponível",
                    "tipo_empresa": "Informação indisponível",
                    "vaga_id": "ID indisponível"} for vaga in vagas):
        return jsonify([])  # Se todas as informações estiverem indisponíveis, retornar uma lista vazia

    return jsonify(vagas)

if __name__ == '__main__':
    app.run(debug=True)
