# projectBiomedicSingularity

## 🤩 Menções Honrosas

1. Para o treinamento dos modelos usamos a arquitetura YoloV10
2. Para realizar as anotações usamos o site Roboflow
3. Nosso backend foi construído usando Python/Fastapi

## ☑️ Andamento do Projeto

- Em Desenvolvimento

## ☄️ Versão Atual

- 0.1.0

## 🕹️ Funcionalidades

...

## 🚀 Clonando Projeto

Nesta seção, explicaremos como você pode realizar o download e
rodar o projeto em sua máquina.

### 📋 Pré-requisitos

Antes de iniciar, verifique se você atende aos seguintes pré-requisitos:

- Python 3.11.2 ou superior
- Poetry
- Git
- Postgres
- Docker e Docker Compose

### 🔧 Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

1. Clonando o Repositório:

```bash
git clone https://github.com/lspraciano/projectBiomedicSingularity
```

2. No diretório raiz do projeto, instale as dependências com o comando:

```bash
cd projectBiomedicSingularity
poetry install --no-root
```

3. Ative o ambiente virtual com o comando:

```bash
poetry shell
```

4. Inicie a aplicação com o comando:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

9. Você pode acessar a documentação das rotas da API usando o seguinte endereço:

```
http://127.0.0.1:8000/docs
```

ou

clique [aqui](http://127.0.0.1:8000/docs) para abrir o endereço diretamente no navegador