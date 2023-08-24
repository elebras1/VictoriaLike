class Electricity(object):
    def __init__(self, pays, market_economy):
        self.pays = pays
        self.market_economy = market_economy

        # level, value, title
        self.centrale = [
            [0, 50, "Centrales à charbon"],
            [0, 50, "Centrales à gaz"],
            [0, 50, "Centrales au fioul"],
            [0, 120, "Centrales nucléaire"],
            [0, 70, "Centrales hydroelectrique"],
            [0, 25, "Energies renouvelable"],
        ]

    def get_liste_centrale(self):
        return self.centrale

    # set new value of an centrale
    def set_centrale_charbon(self, value):
        self.centrale[0][0] += value
        self.market_economy.set_offer_electricity(value * self.centrale[0][1])
        self.market_economy.set_demand_charbon(value * 30)
        self.market_economy.set_demand_outil(value * 10)
        self.market_economy.set_demand_administration(value * 3)

    def set_centrale_gaz(self, value):
        self.centrale[1][0] += value
        self.market_economy.set_offer_electricity(value * self.centrale[1][1])
        self.market_economy.set_demand_gaz(value * 30)
        self.market_economy.set_demand_outil(value * 10)
        self.market_economy.set_demand_administration(value * 3)

    def set_centrale_fioul(self, value):
        self.centrale[2][0] += value
        self.market_economy.set_offer_electricity(value * self.centrale[2][1])
        self.market_economy.set_demand_petrole(value * 30)
        self.market_economy.set_demand_outil(value * 10)
        self.market_economy.set_demand_administration(value * 3)

    def set_centrale_nucleaire(self, value):
        self.centrale[3][0] += value
        self.market_economy.set_offer_electricity(value * self.centrale[3][1])
        self.market_economy.set_demand_uranium(value * 20)
        self.market_economy.set_demand_outil(value * 10)
        self.market_economy.set_demand_administration(value * 3)

    def set_centrale_hydroelectrique(self, value):
        self.centrale[4][0] += value
        self.market_economy.set_offer_electricity(value * self.centrale[4][1])
        self.market_economy.set_demand_acier(value * 10)
        self.market_economy.set_demand_outil(value * 10)
        self.market_economy.set_demand_administration(value * 3)

    def set_energie_renouvelable(self, value):
        self.centrale[5][0] += value
        self.market_economy.set_offer_electricity(value * self.centrale[5][1])
        self.market_economy.set_demand_matieres_premieres_strategiques(value * 10)
        self.market_economy.set_demand_fer(value * 5)
        self.market_economy.set_demand_outil(value * 5)
        self.market_economy.set_demand_administration(value * 3)
