
class Solver:

    def __init__(self, model):
        self.model = model

    def predict(self, x):
        return self.model.predict(x)

