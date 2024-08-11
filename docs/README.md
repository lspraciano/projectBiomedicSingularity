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

Esta aplicação possui duas rotas principais, que são: a Root e a White Blood Cells.

### 📌Root

Através dessa rota você pode obter os metadados da aplicação, como versão e autor,
por exemplo. Abaixo o path para acessar o único endpoint dela.

```
http://127.0.0.1:8000/v1/
```

### 📌White Blood Cells

Nesta rota temos dois principais endpoints um Http e outro WebSocket.

#### Http Predict

Neste endpoint temos a possibilidade de o usuário enviar uma imagem
para que a IA realizar detecções nela. Abaixo o path de acesso.

```
http://localhost:8000/v1/white-blood-cells/predict
```

#### WebSocket Track

Neste endpoint podemos nos conectar com backend para enviarmos imagem
no formato base64 e receber de voltar as detecções/rastreamento. É esperado
o seguinte esquema

```
{
    image_data: str
    reset_persist: bool
}
```

o path para realizar a conexão está listado abaixo

```
ws://localhost:8000/v1/white-blood-cells/track/ws
```

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

3. Defina a variável de ambiente "SINGULARITY_APP_RUNNING_MODE" para o modo
   de execução desejado. Por exemplo:

No Windows:

```bash
setx SINGULARITY_APP_RUNNING_MODE "development"
```

No Linux:

```bash
export SINGULARITY_APP_RUNNING_MODE=development
```

4. Ative o ambiente virtual com o comando:

```bash
poetry shell
```

5. Inicie a aplicação com o comando:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

6. Você pode acessar a documentação das rotas da API usando o seguinte endereço:

```
http://127.0.0.1:8000/docs
```

ou

clique [aqui](http://127.0.0.1:8000/docs) para abrir o endereço diretamente no navegador