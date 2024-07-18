import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._cromosomi = DAO.getAllCromosomi()
        self._grafo = nx.DiGraph()
        self._grafo.add_nodes_from(self._cromosomi)
        self._idMap = {}


    def creaGrafo(self):
        pass
