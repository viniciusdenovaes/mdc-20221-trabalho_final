from abc import ABC, abstractmethod
from pathlib import Path
from config import MODELS_PATH, ROOT_PATH
import keras
import os

class Model:
    def __init__(self, model, name):
        self.model = model
        self.name = name

    def predict(self, x):
        return self.model.predict(x)

    def summary(self):
        self.model.summary()

    def get_name(self):
        return self.name


def get_my_vgg_model(model_path: Path, model_name):
    def f1(y_true, y_pred):
        return 1

    def precision(y_true, y_pred):
        return 1

    def recall(y_true, y_pred):
        return 1

    def coeff_determination(y_true, y_pred):
        return 1

    metrics = {
        'f1': f1,
        'precision': precision,
        'recall': recall,
        'coeff_determination': coeff_determination,
    }
    model = keras.models.load_model(model_path, custom_objects=metrics)

    return Model(model, model_name)


class MyModelVGGDataAugmentation:
    @staticmethod
    def get_model() -> Model:
        model_path = MODELS_PATH/Path('vgg_250_epochs_data_aumen')
        return get_my_vgg_model(model_path, 'VGG16 com Data Augmentation')


class MyModelVGG:
    @staticmethod
    def get_model() -> Model:
        model_path = MODELS_PATH/Path('vgg_250_epochs')
        return get_my_vgg_model(model_path, 'VGG16 sem Data Augmentation')


