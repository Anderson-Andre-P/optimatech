<h1 align="center">Optimatech Challenge</h1>

<p align="center">
  <a href="https://github.com/Anderson-Andre-P/optimatech">
    <img alt="Made by Anderson André" src="https://img.shields.io/badge/-Github-3D7BF7?style=for-the-badge&logo=Github&logoColor=white&link=https://github.com/Anderson-Andre-P" />
  </a>
  <a href="https://www.linkedin.com/in/anderson-andre-pereira/">
      <img alt="Anderson André" src="https://img.shields.io/badge/-Anderson%20André-3D7BF7?style=for-the-badge&logo=Linkedin&logoColor=white" />
   </a>
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/Anderson-Andre-P/optimatech?style=for-the-badge&label=Repo%20Size:&labelColor=3D7BF7&color=3D7BF7">
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/optimatech-02.10.2024-3D7BF7?style=for-the-badge&labelColor=3D7BF7">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Anderson-Andre-P/optimatech?style=for-the-badge&label=last%20commit:&labelColor=3D7BF7&color=3D7BF7">
    <img alt="License" src="https://img.shields.io/badge/license-NONE-3D7BF7?style=for-the-badge&labelColor=3D7BF7&color=3D7BF7">
</p>

Este projeto foi desenvolvido como parte do desafio para a vaga de Desenvolvedor FullStack na OPTIMATECH. O desafio consiste em criar uma aplicação FullStack usando as tecnologias:

- ReactJs
- Material UI
- Python
- Fast API
- MySQL

## :link: Demo

<p>Uma demonstração do funcionamento da aplicação está disponível <a href="https://github.com/Anderson-Andre-P/optimatech/blob/master/apresenta%C3%A7%C3%A3o.40">AQUI</a></p>

## Funcionalidades Criadas

- Tela com o dashboard contendo dados da API
- Limpeza dos dados disponibilizados em arquivo XLSX
- Criação de endpoints para a API com Python e Fast API
- Banco de dados MySQL para armazenamento de dados

## Funcionalidades futuras

- Adição de paginação
- Melhorias na responsividades
- Melhoria no consumo de dados

## Como Executar o Projeto

### Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

- **Python 3.10+**
- **Node.js** (versão 16 ou superior)
- **npm** ou **yarn** (para gerenciar pacotes do Node.js)
- **MySQL** (para o banco de dados)
- **Git** (opcional, mas recomendado)

### Clonando o Repositório

Primeiro, clone o repositório do projeto para sua máquina:

```bash
git clone https://github.com/Anderson-Andre-P/optimatech
cd optimatech
```

### Configurando o Backend (API FastAPI)

1. **Crie um ambiente virtual Python**:
   No diretório raiz do backend, crie e ative um ambiente virtual:

   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```

2. **Instale as dependências**:
   Com o ambiente virtual ativado, instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configuração do Banco de Dados**:
   Crie um arquivo `.env` na raiz do diretório `backend` com base no arquivo `.env.example`, ajustando as variáveis de ambiente de acordo com sua configuração MySQL:

   ```bash
   cp .env.example .env
   ```

   Edite o arquivo `.env` com suas credenciais de banco de dados.

4. **Inicialize o Banco de Dados**:
   Certifique-se de que o MySQL está rodando e crie o banco de dados especificado no `.env` se ainda não existir:

   ```sql
   CREATE DATABASE <nome_do_banco>;
   ```

   (Opcional: Você pode importar os dados do arquivo `dados.sql` na pasta `dataset`.)

5. **Executando a API**:
   No diretório `backend`, execute a aplicação FastAPI:

   ```bash
   uvicorn API.main:app --reload
   ```

   A API estará disponível em: `http://127.0.0.1:8000`

### Configurando o Frontend (React)

1. **Instale as dependências do frontend**:
   No diretório `frontend/optimatech-challenge`, instale as dependências do projeto:

   ```bash
   cd ../frontend/optimatech-challenge
   npm install
   ```

   Ou, se preferir usar yarn:

   ```bash
   yarn install
   ```

2. **Executando o Frontend**:
   Ainda no diretório do frontend, inicie a aplicação React:

   ```bash
   npm start
   ```

   Ou, se estiver usando yarn:

   ```bash
   yarn start
   ```

   A aplicação estará disponível em: `http://localhost:3000`

(Observação: Talvez o projeto frontend abra em outro endereço).

### Considerações Finais

- Certifique-se de que tanto o backend quanto o frontend estejam rodando ao mesmo tempo.
- Se você encontrar problemas com permissões no MySQL, verifique suas credenciais no arquivo `.env` e certifique-se de que o banco de dados está rodando corretamente.
- A pasta `docker` contém arquivos de configuração para Docker, mas ainda não estão funcionais.

### Considerações Finais

Este projeto foi uma excelente oportunidade para aplicar conhecimentos de desenvolvimento FullStack e consumo de API's. Agradeço pela oportunidade e estou à disposição para quaisquer dúvidas ou esclarecimentos.

## Contato

Se você tiver alguma dúvida ou sugestão sobre o projeto, não hesite em me contatar. Você pode me encontrar no LinkedIN.

Obrigado pelo seu interesse e apoio ao projeto!

- Contate-me através do meu perfil pessoal no LinkedIn.

  <a href="https://www.linkedin.com/in/anderson-andre-pereira/">
  <img alt="Anderson André" src="https://img.shields.io/badge/-Anderson%20André-3D7BF7?style=for-the-badge&logo=Linkedin&logoColor=white" />
  </a>

<a href="#top">Voltar ao topo</a>
