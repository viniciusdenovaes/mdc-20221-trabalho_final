import numpy as np
import pandas as pd

col_order = [
    'sunrisesunset',
    'dawndusk',
    'night',
    'dark',
    'stressful',
    'dirty',
    'boring',
    'dull',
    'gloomy',
    'fog',
    'clouds',
    'storm',
    'windy',
    'rain',
    'moist',
    'snow',
    'ice',
    'cold',
    'autumn',
    'spring',
    'winter',
    'lush',
    'summer',
    'warm',
    'dry',
    'sunny',
    'midday',
    'daylight',
    'bright',
    'flowers',
    'colorful',
    'beautiful',
    'exciting',
    'glowing',
    'rugged',
    'cluttered',
    'busy',
    'soothing',
    'sentimental',
    'mysterious',
]


class View:
    @staticmethod
    def show(x: np.array):
        x = x[0]
        atributes80 = []
        atributes60 = []
        atributes40 = []
        atributes20 = []
        atributes00 = []
        for a, v in zip(col_order, x):
            print(f'{a:15}|{int(100*round(v, 2)):3d}%')
            if v > .8:
                atributes80.append(a)
            elif v > .6:
                atributes60.append(a)
            elif v > .4:
                atributes40.append(a)
            elif v > .2:
                atributes20.append(a)
            else:
                atributes00.append(a)

        print(f'A imagem eh fortemente (80-100%) {atributes80}')
        print(f'A imagem eh (60-80%) {atributes60}')
        print(f'A imagem (40-60%) {atributes40}')
        print(f'A imagem nao eh (20-40%) {atributes20}')
        print(f'A imagem fortemente nao eh (00-20%) {atributes00}')



