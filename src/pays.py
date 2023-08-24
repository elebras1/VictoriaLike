from market_economy import Market_economy
from electricity import Electricity
from manufacture import Manufacture
from infrastructure import Infrastucture
from ressource import Ressource


class Pays(object):
    def __init__(self, nom, pib, nbh, flag, screen):
        self.screen = screen

        self.nom = nom
        self.pib = pib
        self.nbh = nbh
        self.flag = flag

        self.market_economy = Market_economy(self)
        self.elec = Electricity(self, self.market_economy)
        self.manu = Manufacture(self, self.market_economy)
        self.infra = Infrastucture(self, self.market_economy)
        self.rsc = Ressource(self, self.market_economy)
        salaire_classe_basse = 600
        salaire_classe_moyenne = 1000
        salaire_classe_haute = 2000

    def __str__(self):
        return (
            " le pays "
            + self.nom
            + " à un PIB de "
            + str(self.pib)
            + " millions $, un nombres d'habitants de "
            + str(self.nbh)
            + " milliers"
        )

    def get_pib(self):
        return self.pib

    def get_nbh(self):
        return self.nbh

    def get_nom(self):
        return self.nom

    def get_flag(self):
        return self.flag

    def get_market_economy(self):
        return self.market_economy

    def get_electricty(self):
        return self.elec

    def get_manufacture(self):
        return self.manu

    def get_ressource(self):
        return self.rsc

    def get_infrastructure(self):
        return self.infra
