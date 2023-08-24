class Market_economy(object):
    def __init__(self, pays):
        self.pays = pays

        # value offer, value demand, title
        self.offer_demand = [
            [0, 0, "Electricite"],
            [0, 0, "Charbon"],
            [0, 0, "Gaz"],
            [0, 0, "Uranium"],
            [0, 0, "Fioul"],
            [0, 0, "Culture"],
            [0, 0, "Viande"],
            [0, 0, "Fer"],
            [0, 0, "Matières premières statégiques"],
            [0, 0, "Bois"],
            [0, 0, "Produit chimique"],
            [0, 0, "Vehicule"],
            [0, 0, "Textile"],
            [0, 0, "Meuble"],
            [0, 0, "Outil"],
            [0, 0, "Semi-conducteur"],
            [0, 0, "Appareil connecté"],
            [0, 0, "Acier"],
            [0, 0, "Construction"],
            [0, 0, "Port"],
            [0, 0, "Transport"],
            [0, 0, "Administration"],
        ]

    def get_offer_demand(self):
        return self.offer_demand

    # Electricity demand and offer
    def get_demand_electricity(self):
        return self.offer_demand[0][1]

    def set_demand_electricity(self, value):
        self.offer_demand[0][1] += value

    def set_offer_electricity(self, value):
        self.offer_demand[0][0] += value

    def get_offer_electricity(self):
        return self.offer_demand[0][0]

    # Ressource demand and offer
    def get_demand_charbon(self):
        return self.offer_demand[1][1]

    def set_demand_charbon(self, value):
        self.offer_demand[1][1] += value

    def get_demand_gaz(self):
        return self.offer_demand[2][1]

    def set_demand_gaz(self, value):
        self.offer_demand[2][1] += value

    def get_demand_uranium(self):
        return self.offer_demand[3][1]

    def set_demand_uranium(self, value):
        self.offer_demand[3][1] += value

    def get_demand_petrole(self):
        return self.offer_demand[4][1]

    def set_demand_petrole(self, value):
        self.offer_demand[4][1] += value

    def get_demand_culture(self):
        return self.offer_demand[5][1]

    def set_demand_culture(self, value):
        self.offer_demand[5][1] += value

    def get_demand_elevage(self):
        return self.offer_demand[6][1]

    def set_demand_elevage(self, value):
        self.offer_demand[6][1] += value

    def get_demand_fer(self):
        return self.offer_demand[7][1]

    def set_demand_fer(self, value):
        self.offer_demand[7][1] += value

    def get_demand_matieres_premieres_strategiques(self):
        return self.offer_demand[8][1]

    def set_demand_matieres_premieres_strategiques(self, value):
        self.offer_demand[8][1] += value

    def get_demand_bois(self):
        return self.offer_demand[9][1]

    def set_demand_bois(self, value):
        self.offer_demand[9][1] += value

    def get_demand_produit_chimique(self):
        return self.offer_demand[10][1]

    def set_demand_produit_chimique(self, value):
        self.offer_demand[10][1] += value

    def get_demand_vehicule(self):
        return self.offer_demand[11][1]

    def set_demand_vehicule(self, value):
        self.offer_demand[11][1] += value

    def set_offer_charbon(self, value):
        self.offer_demand[1][0] += value

    def get_offer_charbon(self):
        return self.offer_demand[1][0]

    def set_offer_gaz(self, value):
        self.offer_demand[2][0] += value

    def get_offer_gaz(self):
        return self.offer_demand[2][0]

    def set_offer_uranium(self, value):
        self.offer_demand[3][0] += value

    def get_offer_uranium(self):
        return self.offer_demand[3][0]

    def set_offer_petrole(self, value):
        self.offer_demand[4][0] += value

    def get_offer_petrole(self):
        return self.offer_demand[4][0]

    def set_offer_culture(self, value):
        self.offer_demand[5][0] += value

    def get_offer_culture(self):
        return self.offer_demand[5][0]

    def set_offer_elevage(self, value):
        self.offer_demand[6][0] += value

    def get_offer_elevage(self):
        return self.offer_demand[6][0]

    def set_offer_fer(self, value):
        self.offer_demand[7][0] += value

    def get_offer_fer(self):
        return self.offer_demand[7][0]

    def set_offer_matieres_premieres_strategiques(self, value):
        self.offer_demand[8][0] += value

    def get_offer_matieres_premieres_strategiques(self):
        return self.offer_demand[8][0]

    def set_offer_bois(self, value):
        self.offer_demand[9][0] += value

    def get_offer_bois(self):
        return self.offer_demand[9][0]

    def set_offer_produit_chimique(self, value):
        self.offer_demand[10][0] += value

    def get_offer_produit_chimique(self):
        return self.offer_demand[10][0]

    def set_offer_vehicule(self, value):
        self.offer_demand[11][0] += value

    def get_offer_vehicule(self):
        return self.offer_demand[11][0]

    # manufacture demand offer

    def get_demand_vetement(self):
        return self.offer_demand[12][1]

    def set_demand_vetement(self, value):
        self.offer_demand[12][1] += value

    def get_demand_meuble(self):
        return self.offer_demand[13][1]

    def set_demand_meuble(self, value):
        self.offer_demand[13][1] += value

    def get_demand_outil(self):
        return self.offer_demand[14][1]

    def set_demand_outil(self, value):
        self.offer_demand[14][1] += value

    def get_demand_semi_conducteur(self):
        return self.offer_demand[15][1]

    def set_demand_semi_conducteur(self, value):
        self.offer_demand[15][1] += value

    def get_demand_appareil_connecte(self):
        return self.offer_demand[16][1]

    def set_demand_appareil_connecte(self, value):
        self.offer_demand[16][1] += value

    def get_demand_acier(self):
        return self.offer_demand[17][1]

    def set_demand_acier(self, value):
        self.offer_demand[17][1] += value

    def set_offer_vetement(self, value):
        self.offer_demand[12][0] += value

    def get_offer_vetement(self):
        return self.offer_demand[12][0]

    def set_offer_meuble(self, value):
        self.offer_demand[13][0] += value

    def get_offer_meuble(self):
        return self.offer_demand[13][0]

    def set_offer_outil(self, value):
        self.offer_demand[14][0] += value

    def get_offer_outil(self):
        return self.offer_demand[14][0]

    def set_offer_semi_conducteur(self, value):
        self.offer_demand[15][0] += value

    def get_offer_semi_conducteur(self):
        return self.offer_demand[15][0]

    def set_offer_appareil_connecte(self, value):
        self.offer_demand[16][0] += value

    def get_offer_appareil_connecte(self):
        return self.offer_demand[16][0]

    def set_offer_acier(self, value):
        self.offer_demand[17][0] += value

    def get_offer_acier(self):
        return self.offer_demand[17][0]

    # Infrastructure offer demand
    def get_construction(self):
        return self.offer_demand[18][1]

    def set_construction(self, value):
        self.offer_demand[18][1] += value

    def get_demand_port(self):
        return self.offer_demand[19][1]

    def set_demand_port(self, value):
        self.offer_demand[19][1] += value

    def get_demand_transport(self):
        return self.offer_demand[20][1]

    def set_demand_transport(self, value):
        self.offer_demand[20][1] += value

    def get_demand_administration(self):
        return self.offer_demand[21][1]

    def set_demand_administration(self, value):
        self.offer_demand[21][1] += value

    def get_offer_construction(self):
        return self.offer_demand[18][0]

    def set_offer_construction(self, value):
        self.offer_demand[18][0] += value

    def get_offer_port(self):
        return self.offer_demand[19][0]

    def set_offer_port(self, value):
        self.offer_demand[19][0] += value

    def get_offer_transport(self):
        return self.offer_demand[20][0]

    def set_offer_transport(self, value):
        self.offer_demand[20][0] += value

    def get_offer_administration(self):
        return self.offer_demand[21][0]

    def set_offer_administration(self, value):
        self.offer_demand[21][0] += value
