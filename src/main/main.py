from pathlib import Path
import argparse
import os

from dao.adapter import Adapter
from solvers.Model import MyModelVGGDataAugmentation, MyModelVGG
from solvers.Solver import Solver
from view.view import View

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve some image.')
    parser.add_argument('-i', '--image', required=True, type=Path, help='image path to solve')

    args = parser.parse_args()

    path_img = args.image

    x = Adapter.get_data(path_img)

    print('Entre com um numero para escolher o modelo:')
    print('0 - VGG16 com aumentacao,                    MSE: 0.04256')
    print('1 - VGG16 sem aumentacao,                    MSE: 0.04856')
    print('2 - SVR com VGG16 para extracao de features, MSE: 0.10056')

    option = int(input())

    model = None
    if option == 0:
        model = MyModelVGGDataAugmentation.get_model()
    elif option == 1:
        model = MyModelVGG.get_model()
    elif option == 2:
        print('ainda nao incluido')
        exit(1)
    else:
        print('opcao nao suportada')
        exit(1)

    print(f'Usando model {model.get_name()}')
    model.summary()

    solver = Solver(model)

    p = solver.predict(x)

    View.show(p)




