class Manufacture(object):
    def __init__(self, pays, market_economy):
        self.pays = pays

        # level, title
        self.usines = [
            [0, "Usines de textile"],
            [0, "Manufactures de meubles"],
            [0, "Fabriques d'outils"],
            [0, "Usines de semi-conducteur"],
            [0, "Usines d'appareils connecté"],
            [0, "Aciéries"],
            [0, "Usines chimique"],
            [0, "Usines de vehicule"],
        ]
        self.value = 50
        self.market_economy = market_economy

    def get_liste_usines(self):
        return self.usines

    def get_value(self):
        return self.value

    def set_vetement(self, value):
        self.usines[0][0] += value
        self.market_economy.set_offer_vetement(value * self.value)
        self.market_economy.set_demand_culture(value * 10)
        self.market_economy.set_demand_produit_chimique(value * 20)
        self.market_economy.set_demand_electricity(value * 10)
        self.market_economy.set_demand_outil(value * 10)
        self.market_economy.set_demand_administration(value * 3)
        self.market_economy.set_demand_transport(value * 5)

    def set_meuble(self, value):
        self.usines[1][0] += value
        self.market_economy.set_offer_meuble(value * self.value)
        self.market_economy.set_demand_bois(value * 20)
        self.market_economy.set_demand_produit_chimique(value * 10)
        self.market_economy.set_demand_electricity(value * 10)
        self.market_economy.set_demand_outil(value * 10)
        self.market_economy.set_demand_administration(value * 3)
        self.market_economy.set_demand_transport(value * 5)

    def set_outil(self, value):
        self.usines[2][0] += value
        self.market_economy.set_offer_outil(value * self.value)
        self.market_economy.set_demand_acier(value * 20)
        self.market_economy.set_demand_bois(value * 10)
        self.market_economy.set_demand_electricity(value * 10)
        self.market_economy.set_demand_semi_conducteur(value * 5)
        self.market_economy.set_demand_outil(value * 5)
        self.market_economy.set_demand_administration(value * 3)
        self.market_economy.set_demand_transport(value * 5)

    def set_semi_conducteur(self, value):
        self.usines[3][0] += value
        self.market_economy.set_offer_semi_conducteur(value * self.value)
        self.market_economy.set_demand_matieres_premieres_strategiques(value * 25)
        self.market_economy.set_demand_acier(value * 5)
        self.market_economy.set_demand_electricity(value * 10)
        self.market_economy.set_demand_gaz(value * 5)
        self.market_economy.set_demand_outil(value * 5)
        self.market_economy.set_demand_administration(value * 3)
        self.market_economy.set_demand_transport(value * 5)

    def set_appareil_connecte(self, value):
        self.usines[4][0] += value
        self.market_economy.set_offer_appareil_connecte(value * self.value)
        self.market_economy.set_demand_matieres_premieres_strategiques(value * 15)
        self.market_economy.set_demand_electricity(value * 15)
        self.market_economy.set_demand_semi_conducteur(value * 15)
        self.market_economy.set_demand_gaz(value * 5)
        self.market_economy.set_demand_outil(value * 5)
        self.market_economy.set_demand_administration(value * 3)
        self.market_economy.set_demand_transport(value * 5)

    def set_acier(self, value):
        self.usines[5][0] += value
        self.market_economy.set_offer_acier(value * self.value)
        self.market_economy.set_demand_fer(value * 40)
        self.market_economy.set_demand_electricity(value * 10)
        self.market_economy.set_demand_gaz(value * 5)
        self.market_economy.set_demand_outil(value * 5)
        self.market_economy.set_demand_produit_chimique(value * 5)
        self.market_economy.set_demand_administration(value * 3)
        self.market_economy.set_demand_transport(value * 5)

    def set_produit_chimique(self, value):
        self.usines[6][0] += value
        self.market_economy.set_offer_produit_chimique(value * self.value)
        self.market_economy.set_demand_culture(value * 15)
        self.market_economy.set_demand_electricity(value * 10)
        self.market_economy.set_demand_petrole(value * 10)
        self.market_economy.set_demand_administration(value * 3)
        self.market_economy.set_demand_transport(value * 5)

    def set_vehicule(self, value):
        self.usines[7][0] += value
        self.market_economy.set_offer_vehicule(value * self.value)
        self.market_economy.set_demand_culture(value * 15)
        self.market_economy.set_demand_electricity(value * 10)
        self.market_economy.set_demand_petrole(value * 10)
        self.market_economy.set_demand_administration(value * 3)
        self.market_economy.set_demand_transport(value * 5)
