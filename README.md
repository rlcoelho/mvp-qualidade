# MVP Sprint: Qualidade de Software, Segurança e Sistemas Inteligentes

Este projeto é parte integrante da Sprint Qualidade de Software, Segurança e Sistemas Inteligentes. PUC Rio, especialização em Engenharia de Software 2024.

## Prática de Machine Learning em Python

Problema de classificação. Saber se o aluno irá concluir o curso online, baseado no seu comportamento ao longo do curso. Criação do modelo de machine learning feito em um Notebook no Google Colab `MVP3_MeuColab.ipynb` utilizando a linguagem Python com a biblioteca Scikit-Learn e desenvolvimento de uma aplicação full-stack para interagir com o modelo criado.

### Créditos do DataSet utilizado

> Dataset Predict Online Course Engagement  
> Rabie El Kharoua. (2024).  
> 🎓 Predict Online Course Engagement Dataset [Data set]. Kaggle.  
> DOI 10.34740/kaggle/dsv/8725325  

---
## Instalação via Docker

Clonar as pastas `front` e `api` deste repositório, assim como o arquivo `docker-compose.yml`.

Em uma estrutura de pastas similar a esta: 

- /MVP3
- /api (onde você irá clonar o back-end da aplicação)
- /front (onde você irá clonar o front-end da aplicação)
- docker-compose.yml 

Se desejar outra estrutura de pastas, você pode editar o arquivo docker-compose.yml para os locais que desejar, apenas localize os termos "build" e substitua os contextos pelas suas pastas.

Com tudo pronto basta acessar a pasta onde está o docker-compose.yml via terminal e, com o docker desktop em execução, rodar o seguinte comando:

docker-compose up --build

O esperado é que o back-end rode em localhost na porta 5000: http://127.0.0.1:5000/ pois todas as rotas apontam para este destino. O front-end está configurado para rodar em localhost na porta 80, que é o padrão do servidor Nginx http://127.0.0.1/ mas você também pode ajustar para a sua necessidade.

## Instalação sem o Docker

Para o front-end basta executar o arquivo `index.html` que está na pasta `front` deste repositório.

Para o back-end, clonar a pasta `api` e seguir os passos abaixo:

Será necessário ter instaladas todas as libs Python listadas no arquivo `requirements.txt`.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

