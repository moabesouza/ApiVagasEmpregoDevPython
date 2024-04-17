
<h4 align="center"> 
  Web Scraping de Vagas de Emprego
</h4>
<p align="center">
    <img alt="Status do Projeto" src="https://img.shields.io/badge/STATUS-CONCLU%C3%8DDO-brightgreen">
</p>
<p align="center">
 <a href="#-sobre-o-projeto">Sobre</a> •
 <a href="#-funcionalidades">Funcionalidades</a> •
 <a href="#-layout">Layout</a> • 
 <a href="#-endpoints-da-api">Endpoints da API</a> •
 <a href="#-como-executar-o-projeto">Como Executar</a> • 
 <a href="#-tecnologias-utilizadas">Tecnologias Utilizadas</a> • 
 <a href="#-contribuidores">Contribuidores</a> • 
 <a href="#-autor">Autor</a> • 
 <a href="#user-content--licença">Licença</a>
</p>

## 💻 Sobre o Projeto

📄 O projeto consiste em um web scraping para extrair vagas de emprego de um determinado site, fornecendo informações relevantes sobre as oportunidades disponíveis. Este projeto é desenvolvido para fins educacionais, visando a prática de web scraping e desenvolvimento de APIs simples.

## ⚙️ Funcionalidades
  - [x] Extração de vagas de emprego
  - [x] Filtros de pesquisa
  - [x] Visualização das informações das vagas


## 📤 Propiedades retornada:

- [x] Nome da vaga
- [x] Nome da empresa
- [x] ID da vaga
- [x] Localização
- [x] Tipo de contrato
- [x] Salário
- [x] Nível da vaga
- [x] Data de publicação
- [x] Link da vaga
- [x] Tipo de empresa

## 🔢 Parâmetros de consulta:
- [x] page: Número da página a ser consultada (opcional, padrão é 1).
- [x] expertise: Especialidade da vaga (opcional).
- [x] city: Cidade da vaga (opcional).


## 🔗 Endpoints da API
 - [x] Obter todas as vagas de emprego disponíveis
```bash
Método HTTP: GET
Endpoint: /vagas
```

- [x] Obter vagas de emprego disponíveis em uma cidade específica
```bash
Método HTTP: GET
Endpoint: /vagas?city={nome_da_cidade}
Exemplo de uso: /vagas?city=sao-paulo
```

- [x] Obter vagas de emprego disponíveis em uma área de expertise específica
```bash
Método HTTP: GET
Endpoint: /vagas?expertise={area_de_expertise}
Exemplo de uso: /vagas?expertise=python
```

- [x] Obter vagas de emprego disponíveis em uma página específica
```bash
Método HTTP: GET
Endpoint: /vagas?page={numero_da_pagina}
Exemplo de uso: /vagas?page=2
```

- [x] Obter vagas de emprego disponíveis com filtro de cidade e área de expertise
```bash
Método HTTP: GET
Endpoint: /vagas?city={nome_da_cidade}&expertise={area_de_expertise}
Exemplo de uso: /vagas?city=sao-paulo&expertise=python
```
## 🛣️ Como Executar o Projeto
Pré-requisitos
Antes de iniciar, verifique se você atende aos seguintes requisitos:
Python 3.x instalado em sua máquina.

## 🧭 Rodando o Projeto
```bash
#Clone este repositório:
$ git clone https://github.com/moabesouza/ApiVagasEmpregoDevPython

```
🛠 Tecnologias Utilizadas
As seguintes ferramentas foram usadas na construção do projeto:

  - [x] Python
  - [x] Beautiful Soup (biblioteca Python para web scraping)
  - [x] Flask (para a criação da API)

## 💪 Como contribuir para o projeto

1. Faça um **fork** do projeto.
2. Crie uma nova branch com as suas alterações: `git checkout -b my-feature`
3. Salve as alterações e crie uma mensagem de commit contando o que você fez: `git commit -m "feature: My new feature"`
4. Envie as suas alterações: `git push origin my-feature`
> Caso tenha alguma dúvida confira este [guia de como contribuir no GitHub](./CONTRIBUTING.md)
