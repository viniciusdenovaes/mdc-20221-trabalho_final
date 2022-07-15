import os
from pathlib import Path

ROOT_PATH = Path(os.path.dirname(os.path.abspath(__file__)))
MODELS_PATH = ROOT_PATH.parent/Path('data/models')

