Projeto criado durante o living code [Consumindo a API do Twitter com Python](https://docs.google.com/presentation/d/11DkkyQUIloVQLm8i6hN6w3xyUaP4WSRE/edit?usp=sharing&ouid=102662434190974209165&rtpof=true&sd=true).

## Visão Geral do Projeto 🚀

Este projeto é um exemplo de como consumir a API do Twitter usando Python para obter tópicos de tendência, armazená-los em um banco de dados MongoDB e exibi-los através de uma interface amigável.

## Tecnologias Utilizadas 📚

- Python 3.8.x
- FastAPI
- MongoDB

## Requisitos de Instalação ✋

Antes de começar, você precisará ter o Docker e o Docker Compose instalados no seu computador.

- [Docker](https://www.docker.com)
- [Docker Compose](https://docs.docker.com/compose/)

## Instalação 💽

1. Clone este repositório para o seu ambiente local.
2. Navegue até o diretório do projeto.

## Rodando a Aplicação 🛸

1. Abra um terminal e navegue até o diretório do projeto.
2. Execute o seguinte comando para iniciar a aplicação:


docker-compose up --build

## Acesse o Swagger UI para visualizar e testar os endpoints disponíveis.

Use Ctrl+C para finalizar o servidor quando necessário.

## Rodando os Testes 🧪
* Abra um terminal e navegue até o diretório do projeto.
* Execute o seguinte comando para rodar os testes:
*docker-compose run app poetry run pytest

##Estrutura do Projeto 📁
app/: Contém os arquivos relacionados à aplicação FastAPI.
main.py: Ponto de entrada da aplicação.
dashboard.py: Código para criar um painel interativo de tendências.
src/: Contém os arquivos de serviços e conexão com o Twitter e MongoDB.
connection.py: Configuração da conexão com o MongoDB.
responses.py: Definição de modelos de resposta.
services.py: Funções para interagir com a API do Twitter e o banco de dados.
Dockerfile: Arquivo de configuração do Docker para criar o container da aplicação.
docker-compose.yaml: Arquivo de configuração do Docker Compose.
requirements.txt: Lista de dependências do Python.

## Licença 📜
Este projeto está licenciado sob a MIT License.

Certifique-se de atualizar os detalhes do projeto, como a descrição geral, a estrutura de diretórios e qualquer outro detalhe específico do seu projeto. Isso deve fornecer uma base sólida para os usuários entenderem e usarem o seu projeto.
