
Web Scraping de Vagas de Emprego com Flask
Este projeto consiste em uma aplicação web desenvolvida em Flask para realizar web scraping no site Programa Thor (https://programathor.com.br/jobs) e extrair informações sobre vagas de emprego. A aplicação oferece endpoints para acessar essas informações de forma estruturada.

Funcionalidades
A aplicação oferece os seguintes endpoints:

1. /vagas
Este endpoint permite obter informações sobre as vagas de emprego disponíveis no Programa Thor. As informações retornadas incluem:

Nome da vaga
Nome da empresa
ID da vaga
Localização
Tipo de contrato
Salário
Nível da vaga
Data de publicação
Link da vaga
Tipo de empresa
Parâmetros de consulta:
page: Número da página a ser consultada (opcional, padrão é 1).
expertise: Especialidade da vaga (opcional).
city: Cidade da vaga (opcional).
Exemplos de Uso:
Obter todas as vagas:
bash
Copy code
GET /vagas
Obter vagas em uma determinada página:
bash
Copy code
GET /vagas?page=2
Filtrar vagas por expertise:
bash
Copy code
GET /vagas?expertise=Desenvolvimento%20Web
Filtrar vagas por cidade:
bash
Copy code
GET /vagas?city=São%20Paulo
Instalação e Execução
Para executar a aplicação localmente, siga os passos abaixo:

Clone este repositório:
bash
Copy code
git clone https://github.com/seu-usuario/nome-do-repositorio.git
Instale as dependências:
Copy code
pip install -r requirements.txt
Execute a aplicação:
Copy code
python app.py
A aplicação estará disponível em http://localhost:5000.

Observações
Certifique-se de estar em conformidade com os termos de uso do site Programa Thor ao usar este aplicativo para web scraping.
Este aplicativo é apenas um exemplo educacional e pode ser modificado para atender a diferentes necessidades ou integrado a outros sistemas.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests para melhorar este projeto.


Recursos Adicionais
Flask
Requests
Beautiful Soup
Urllib
Contato
Para mais informações, entre em contato via email: seu-email@example.com
