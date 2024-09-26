from schemas.error_schema import ErrorSchema
from schemas.predicao_schema import PredicaoSchema, PredicaoViewSchema
from utils.pre_processamento import preparar_data_frame
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, jsonify
from flask_cors import CORS

import pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
predicao_tag = Tag(name="Predição", description="Predição para saber se o aluno irá concluir um curso online")

# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de predição 
@app.post('/predicao', tags=[predicao_tag],
          responses={"200": PredicaoViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def realizar_predicao(form: PredicaoSchema):
    """Realiza a predição com base nos dados fornecidos pelo usuário."""
    try:
        # Extrair dados do formulário
        features = np.array([[
            form.ccateg,
            form.timesp,
            form.nvideo,
            form.nquizz,
            form.qscore,
            form.corate,
            form.device
        ]])

        # Colunas originais do DataFrame após aplicar get_dummies
        original_columns = ['TimeSpentOnCourse', 
                            'NumberOfVideosWatched', 
                            'NumberOfQuizzesTaken', 
                            'QuizScores',
                            'CompletionRate', 
                            'DeviceType', 
                            'CourseCategory_Arts', 
                            'CourseCategory_Business', 
                            'CourseCategory_Health', 
                            'CourseCategory_Programming', 
                            'CourseCategory_Science'
                            ]

        # Preparar o DataFrame
        features_prepared = preparar_data_frame(features, original_columns)

        # Converter para numpy array se necessário
        features_prepared = features_prepared.to_numpy()

        # Carregar o pipeline a partir do arquivo .pkl
        pipeline_path = 'ml_model/pipeline-online-course-cart-norm.pkl'
        with open(pipeline_path, 'rb') as file:
            pipeline = pickle.load(file)

        # Realizar a predição
        predicao = pipeline.predict(features_prepared)

        # Retornar o resultado da predição em formato JSON
        return jsonify({'predicao': int(predicao[0])})

    except Exception as e:
        return jsonify({'error': str(e)}), 400