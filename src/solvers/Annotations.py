import numpy as np
import pandas as pd


def returnAnnotations(file_attributos, file_annotations):
    df_attributes = pd.read_csv(file_attributos, header=None)
    list_attributes = list()
    list_attributes.append(df_attributes[0].values)
    handle = open(file_annotations)
    scores = dict()
    confidence = dict()
    for line in handle:
        words = line.split()
        i=0
        for word in words:
            if i == 0:
                scores[word]=list()
                confidence[word] = list()
                i+=1
            else:
                values = word.split(',')
                scores[words[0]].append(float(values[0]))
                confidence[words[0]].append(float(values[1]))
                i+=1
    scores = pd.DataFrame(scores).T
    scores.columns = list_attributes
    confidence = pd.DataFrame(confidence).T
    confidence.columns = list_attributes
    return scores,confidence


file_attributos = '../../data/annotations/attributes.txt'
file_annotations = '../../data/annotations/annotations.tsv'
file_training = '../../data/training_test_splits/holdout_split/training.txt'
file_test = '../../data/training_test_splits/holdout_split/test.txt'
def returnTrainingTest(file_attributos, file_annotations, file_training, file_test):
    scores,confidence = returnAnnotations(file_attributos, file_annotations)
    df_training = pd.read_csv(file_training, header = None)
    df_test = pd.read_csv(file_test, header = None)
    scores_training = scores[scores.index.isin(df_training[0].values)]
    scores_test = scores[scores.index.isin(df_test[0].values)]
    confidence_training = confidence[confidence.index.isin(df_training[0].values)]
    confidence_test = confidence[confidence.index.isin(df_test[0].values)]
    return scores_training, scores_test, confidence_training, confidence_test

scores_training, scores_test, confidence_training, confidence_test = returnTrainingTest(file_attributos, file_annotations, file_training, file_test)

df_training = scores_training

df_test = scores_test

def get_annotation(nome: str) -> np.array:
    if nome in df_training.index:
        print(f'nome {nome} em conjunto de treino')
        return df_training.loc[[nome]].values
    if nome in df_test.index:
        print(f'nome {nome} em conjunto de teste')
        return df_test.loc[[nome]].values
    print(f'nome {nome} nao encontrada anotacao')
    return None
