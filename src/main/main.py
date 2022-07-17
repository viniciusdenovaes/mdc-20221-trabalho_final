from pathlib import Path
import argparse
import os

from dao.adapter import Adapter
from solvers import Annotations
from solvers.Model import MyModelVGGDataAugmentation, MyModelVGG
from solvers.Solver import Solver
from view.view import View

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve some image.')
    parser.add_argument('-i', '--image', required=True, type=Path, help='image path to solve')

    args = parser.parse_args()

    path_img = args.image

    print('Entre com um numero para escolher o modelo:')
    print('0 - VGG16 com aumentacao,                    MSE: 0.04256')
    print('1 - VGG16 sem aumentacao,                    MSE: 0.04856')
    print('2 - Ver os atributos anotados (se disponivel)')
    print('NA- media dos atributos de treino,           MSE: 0.07531')
    print('NA- SVR com VGG16 para extracao de features, MSE: 0.10056')

    option = int(input())

    model = None
    if option == 0:
        model = MyModelVGGDataAugmentation.get_model()
    elif option == 1:
        model = MyModelVGG.get_model()
    elif option == 2:
        head, tail = os.path.split(path_img)
        _, tail2 = os.path.split(head)
        img_name = os.path.join(tail2, tail)
        p = Annotations.get_annotation(img_name)
        View.show(p)
        exit(0)
    else:
        print('opcao nao suportada')
        exit(1)

    x = Adapter.get_data(path_img)

    print(f'Usando model {model.get_name()}')
    model.summary()

    solver = Solver(model)

    p = solver.predict(x)

    View.show(p)




