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



class MyModelVGGDataAugmentation:
    @staticmethod
    def get_model() -> Model:

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
        print(ROOT_PATH.absolute())
        model_path = MODELS_PATH/Path('vgg_250_epochs_data_aumen')
        print(model_path.absolute())
        model = keras.models.load_model(model_path, custom_objects=metrics)

        return Model(model, 'VGG16 com Data Augmentation')

