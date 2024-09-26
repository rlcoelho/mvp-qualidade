import pandas as pd

def preparar_data_frame(features, original_columns):
    # Criar um DataFrame com os dados recebidos
    new_data = pd.DataFrame(features, columns=['CourseCategory', 
                                               'TimeSpentOnCourse', 
                                               'NumberOfVideosWatched', 
                                               'NumberOfQuizzesTaken', 
                                               'QuizScores',
                                               'CompletionRate', 
                                               'DeviceType'
                                               ])

    # Aplicar get_dummies à coluna 'CourseCategory'
    new_data_dummies = pd.get_dummies(new_data, columns=['CourseCategory'])

    # Adicionar colunas faltantes com valor 0
    for col in original_columns:
        if col not in new_data_dummies:
            new_data_dummies[col] = 0

    # Reordenar as colunas para garantir a mesma ordem
    new_data_dummies = new_data_dummies[original_columns]

    return new_data_dummies
