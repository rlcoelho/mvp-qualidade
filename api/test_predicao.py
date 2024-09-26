import pytest
import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from utils.pre_processamento import preparar_data_frame

# Para rodar: pytest -s test_predicao.py

@pytest.fixture
def golden_dataset():
    # Carregar o dataset a partir do arquivo CSV
    df = pd.read_csv('ml_data/golden_dataset.csv')

    # Dropar a coluna 'UserID'
    df = df.drop('UserID', axis=1)

    # Separar as features e o target
    X = df.drop('CourseCompletion', axis=1)
    y = df['CourseCompletion']

    return X, y


def test_pipeline_accuracy(golden_dataset):
    X_test, y_test = golden_dataset

    # Colunas originais do DataFrame após aplicar get_dummies
    original_columns = [
        'TimeSpentOnCourse', 'NumberOfVideosWatched', 'NumberOfQuizzesTaken', 'QuizScores',
        'CompletionRate', 'DeviceType', 'CourseCategory_Arts', 'CourseCategory_Business',
        'CourseCategory_Health', 'CourseCategory_Programming', 'CourseCategory_Science'
    ]

    # Preparar os dados de teste
    X_test_prepared = preparar_data_frame(X_test, original_columns)
    X_test_prepared = X_test_prepared.to_numpy()

    # Carregar o pipeline a partir do arquivo .pkl
    pipeline_path = 'ml_model/pipeline-online-course-cart-norm.pkl'
    with open(pipeline_path, 'rb') as file:
        pipeline = pickle.load(file)

    # Realizar as predições
    y_pred = pipeline.predict(X_test_prepared)

    # Calcular a acurácia
    accuracy = accuracy_score(y_test, y_pred)

    # Verificar se a acurácia é maior do que 0.9
    assert accuracy > 0.9, f"Acurácia esperada > 0.9 e o resultado foi de: {accuracy}"
    print(f"Acurácia esperada > 0.9 e o resultado foi de: {accuracy}")