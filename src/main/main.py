from pathlib import Path
import argparse
import os

from dao.adapter import Adapter
from solvers.Model import MyModelVGGDataAugmentation
from solvers.Solver import Solver
from view.view import View

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve some image.')
    parser.add_argument('-i', '--image', required=True, type=Path, help='image path to solve')

    args = parser.parse_args()

    path_img = args.image

    x = Adapter.get_data(path_img)

    model = MyModelVGGDataAugmentation.get_model()

    print(f'Usando model {model.get_name()}')
    model.summary()

    solver = Solver(model)

    p = solver.predict(x)

    View.show(p)




