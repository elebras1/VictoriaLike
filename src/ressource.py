class Ressource(object):
    def __init__(self, pays, market_economy):
        self.pays = pays
        self.market_economy = market_economy

        # level, title
        self.ressource = [
            [0, "Mines de charbon"],
            [0, "Puits de gaz"],
            [0, "Cultures"],
            [0, "Elevages de bétail"],
            [0, "Mines d'uranium"],
            [0, "Puits de pétrole"],
            [0, "Mines de fer"],
            [0, "Mines de matières premières statégiques"],
            [0, "Filière bois"],
        ]
        self.value = 50

    def get_ressource(self):
        return self.ressource

    def get_value(self):
        return self.value

    def set_charbon(self, value):
        self.ressource[0][0] += value
        self.market_economy.set_offer_charbon(value * self.value)
        self.market_economy.set_demand_vehicule(value * 10)
        self.market_economy.set_demand_electricity(value * 30)
        self.market_economy.set_demand_petrole(value * 5)
        self.market_economy.set_demand_administration(value * 3)
        self.market_economy.set_demand_transport(value * 5)

    def set_gaz(self, value):
        self.ressource[1][0] += value
        self.market_economy.set_offer_gaz(value * self.value)
        self.market_economy.set_demand_vehicule(value * 10)
        self.market_economy.set_demand_electricity(value * 30)
        self.market_economy.set_demand_petrole(value * 5)
        self.market_economy.set_demand_administration(value * 3)
        self.market_economy.set_demand_transport(value * 5)

    def set_culture(self, value):
        self.ressource[2][0] += value
        self.market_economy.set_offer_culture(value * self.value)
        self.market_economy.set_demand_vehicule(value * 10)
        self.market_economy.set_demand_produit_chimique(value * 15)
        self.market_economy.set_demand_petrole(value * 5)
        self.market_economy.set_demand_transport(value * 5)

    def set_elevage(self, value):
        self.ressource[3][0] += value
        self.market_economy.set_offer_elevage(value * self.value)
        self.market_economy.set_demand_culture(value * 20)
        self.market_economy.set_demand_electricity(value * 10)
        self.market_economy.set_demand_transport(value * 5)

    def set_uranium(self, value):
        self.ressource[4][0] += value
        self.market_economy.set_offer_uranium(value * self.value)
        self.market_economy.set_demand_vehicule(value * 10)
        self.market_economy.set_demand_electricity(value * 30)
        self.market_economy.set_demand_petrole(value * 5)
        self.market_economy.set_demand_administration(value * 3)
        self.market_economy.set_demand_transport(value * 5)

    def set_petrole(self, value):
        self.ressource[5][0] += value
        self.market_economy.set_offer_petrole(value * self.value)
        self.market_economy.set_demand_vehicule(value * 5)
        self.market_economy.set_demand_electricity(value * 20)
        self.market_economy.set_demand_petrole(value * 5)
        self.market_economy.set_demand_administration(value * 3)
        self.market_economy.set_demand_transport(value * 5)

    def set_fer(self, value):
        self.ressource[6][0] += value
        self.market_economy.set_offer_fer(value * self.value)
        self.market_economy.set_demand_vehicule(value * 5)
        self.market_economy.set_demand_electricity(value * 10)
        self.market_economy.set_demand_petrole(value * 10)
        self.market_economy.set_demand_administration(value * 3)
        self.market_economy.set_demand_transport(value * 5)

    def set_matieres_premieres_strategiques(self, value):
        self.ressource[7][0] += value
        self.market_economy.set_offer_matieres_premieres_strategiques(
            value * self.value
        )
        self.market_economy.set_demand_vehicule(value * 10)
        self.market_economy.set_demand_electricity(value * 20)
        self.market_economy.set_demand_petrole(value * 10)
        self.market_economy.set_demand_administration(value * 3)
        self.market_economy.set_demand_transport(value * 5)

    def set_bois(self, value):
        self.ressource[8][0] += value
        self.market_economy.set_offer_bois(value * self.value)
        self.market_economy.set_demand_vehicule(value * 10)
        self.market_economy.set_demand_electricity(value * 5)
        self.market_economy.set_demand_petrole(value * 5)
        self.market_economy.set_demand_transport(value * 5)
