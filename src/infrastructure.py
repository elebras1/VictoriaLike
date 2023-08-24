class Infrastucture(object):
    def __init__(self, pays, market_economy):
        self.pays = pays
        self.market_economy = market_economy

        self.infrastructure = [
            [0, "Construction"],
            [0, "Transport"],
            [0, "Port"],
            [0, "Administration"],
        ]

        self.value = 5

    def get_liste_infrastructure(self):
        return self.infrastructure

    def get_value(self):
        return self.value

    def set_construction(self, value):
        self.infrastructure[0][0] += value
        self.market_economy.set_offer_construction(value)
        self.market_economy.set_demand_acier(value * 30)
        self.market_economy.set_demand_outil(value * 20)
        self.market_economy.set_demand_vehicule(value * 5)
        self.market_economy.set_demand_petrole(value * 5)
        self.market_economy.set_demand_administration(value * 3)
        self.market_economy.set_demand_transport(value * 5)

    def set_transport(self, value):
        self.infrastructure[1][0] += value
        self.market_economy.set_offer_transport(value * self.value)
        self.market_economy.set_demand_acier(value * 10)
        self.market_economy.set_demand_electricity(value * 20)
        self.market_economy.set_demand_vehicule(value * 15)
        self.market_economy.set_demand_petrole(value * 10)
        self.market_economy.set_demand_administration(value * 3)

    def set_port(self, value):
        self.infrastructure[2][0] += value
        self.market_economy.set_offer_port(value)
        self.market_economy.set_demand_electricity(value * 10)
        self.market_economy.set_demand_outil(value * 20)
        self.market_economy.set_demand_petrole(value * 10)
        self.market_economy.set_demand_administration(value * 10)

    def set_administration(self, value):
        self.infrastructure[3][0] += value
        self.market_economy.set_offer_transport(value * self.value)
        self.market_economy.set_demand_appareil_connecte(value * 10)
        self.market_economy.set_demand_electricity(value * 30)
        self.market_economy.set_demand_transport(value * 5)
