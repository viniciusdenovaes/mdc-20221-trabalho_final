from dao.adapter import Adapter
from view.view import View


class Controller:
    def __init__(self, dao: Adapter, view: View):
        self.dao = dao
        self.view = view
        