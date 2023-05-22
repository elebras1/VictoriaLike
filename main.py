# objectif 4000!
import random
import pygame
import numpy as np
import threading
from math import floor
from pays import Pays
from interface import Interface
from date import Date

pygame.init()


class Main(object):
    def __init__(self):
        self.screen_width = pygame.display.Info().current_w
        self.screen_height = pygame.display.Info().current_h
        self.size = (self.screen_width, self.screen_height)
        self.screen = pygame.display.set_mode(self.size)
        self.background = pygame.transform.smoothscale(
            pygame.image.load("images\mapv1.0.jpg"), self.size
        )
        self.value_zoom = [0, 0]

        self.police = pygame.font.Font("fonts/AmerTypewriterITCbyBT-Medium.otf", 15)
        self.police2 = pygame.font.Font("fonts/aflfont.ttf", 25)
        self.light_grey = [130, 134, 131]
        self.dark_grey = [43, 42, 43]
        self.dark = [15, 15, 12]
        self.white = [255, 255, 255]
        self.dark_grey_opacity = [43, 42, 43, 128]
        self.icon_size = [[20, 20], [30, 30], [30, 60]]
        self.padding = [5, 30, 70]

        self.h_bar_pos = [5, self.screen_height - 5]
        self.h_bar_size = [floor(self.screen_width * 0.35), self.h_bar_pos[0]]

        self.v_bar_pos = [0, floor(self.screen_height * 0.20)]
        self.v_bar_size = [35, self.screen_height - self.v_bar_pos[1]]

        self.header_pos = [floor(self.screen_width * 0.60), 0]
        self.header_size = [floor(self.screen_width - self.header_pos[0]), 30]

        self.onglet_pos = [self.v_bar_size[0], self.screen_height - self.v_bar_size[1]]
        self.onglet_size = [self.h_bar_size[0], self.v_bar_size[1]]

        # self.pays = [['Afghanistan', 14786.86, 40099.46], ['Afrique du Sud', 419015.02, 59392.25], ['Albanie', 18255.79, 2811.67], ['Algérie', 163044.44, 44177.97], ['Allemagne', 4259934.91, 83196.08], ['Andorre', 3330.28, 79.03], ['Angola', 67404.29, 34503.77], ['Antigua-et-Barbuda', 1471.13, 93.22], ['Arabie saoudite', 833541.24, 35950.4], ['Argentine', 487227.34, 45808.75], ['Arménie', 13861.41, 2790.97], ['Aruba', 3126.02, 106.54], ['Australie', 1552667.36, 25688.08], ['Autriche', 480368.4, 8955.8], ['Azerbaïdjan', 54622.18, 10137.75], ['Bahamas', 11208.6, 407.91], ['Bahreïn', 38868.66, 1463.27], ['Bangladesh', 416264.94, 169356.25], ['Barbade', 4843.8, 281.2], ['Bélarus', 68205.38, 9340.31], ['Belgique', 594104.18, 11592.95], ['Belize', 2491.5, 400.03], ['Bénin', 17144.92, 12996.9], ['Bermudes', 7286.61, 63.87], ['Bhoutan', 2539.55, 777.49], ['Bolivie', 40408.21, 12079.47], ['Bosnie-Herzégovine', 23365.36, 3270.94], ['Botswana', 17614.79, 2588.42], ['Brésil', 1608981.46, 214326.22], ['Brunéi Darussalam', 14006.57, 445.37], ['Bulgarie', 84056.31, 6877.74], ['Burkina Faso', 19737.62, 22100.68], ['Burundi', 2779.81, 12551.21], ['Cabo Verde', 1936.17, 587.92], ['Cambodge', 26961.06, 16589.02], ['Cameroun', 45338.28, 27198.63], ['Canada', 1988336.33, 38246.11], ['Chili', 317058.51, 19493.18], ['Chine', 17734062.65, 1412360.0], ['Chine. RAS de Hong Kong', 369176.4, 7413.1], ['Chypre', 28407.87, 1244.19], ['Cisjordanie et Gaza', 18036.8, 4922.75], ['Colombie', 314464.14, 51516.56], ['Comores', 1296.09, 821.63], ['Congo. République démocratique du', 55350.97, 95894.12], ['Congo. République du', 13366.23, 5835.81], ['Corée. République de', 1810955.87, 51744.88], ['Corée. République démocratique de', 18350.97, 25971.91], ['Costa Rica', 64282.44, 5153.96], ["Côte d'Ivoire", 70043.19, 27478.25], ['Croatie', 68955.08, 3899.0], ['Cuba', 107352.0, 11256.37], ['Curacao', 2699.61, 152.37], ['Danemark', 398303.27, 5856.73], ['Djibouti', 3482.99, 1105.56], ['Dominique', 554.18, 72.41], ['Égypte. République arabe d’', 404142.77, 109262.18], ['El Salvador', 28736.94, 6314.17], ['El Salvador', 28736.94, 9365.15], ['Émirats arabes unis', 415021.59, 17797.74], ['Équateur', 106165.87, 3620.31], ['Érythrée', 2011, 2065.0, 47415.75], ['Espagne', 1427380.68, 1330.93], ['Estonie', 37191.17, 1192.27], ['Eswatini', 4743.34, 331893.74], ['États-Unis', 23315080.56, 120283.03], ['Éthiopie', 111271.11, 143449.29], ['Fédération de Russie', 1778782.63, 924.61], ['Fidji', 4296.3, 5541.02], ['Finlande', 297301.88, 67749.63], ['France', 2957879.76, 2341.18], ['Gabon', 20216.84, 2639.92], ['Gambie', 2038.42, 3708.61], ['Géorgie', 18629.37, 32833.03], ['Ghana', 77594.28, 10641.22], ['Grèce', 214873.88, 124.61], ['Grenade', 1122.81, 56.65], ['Groenland', 3076.02, 170.53], ['Guam', 6123.0, 17109.75], ['Guatemala', 85985.75, 13531.91], ['Guinée', 16091.82, 1634.47], ['Guinée équatoriale', 12269.39, 2060.72], ['Guinée-Bissau', 1638.52, 804.57], ['Guyana', 8044.5, 11447.57], ['Haïti', 20944.39, 10278.34], ['Honduras', 28488.67, 9709.89], ['Hongrie', 181848.02, 84.26], ['Île de Man', 7315.39, 172.68], ['Îles Anglo-Normandes', 11515.26, 68.14], ['Îles Caïmans', 5898.45, 52.89], ['Îles Féroé', 3649.89, 42.05], ['Îles Marshall', 259.54, 707.85], ['Îles Salomon', 1631.49, 45.11], ['Îles Turques-et-Caïques', 943.27, 105.87], ['Îles Vierges (EU)', 4204.0, 1407563.84], ['Inde', 3176295.07, 273753.19], ['Indonésie', 1186092.99, 87923.43], ['Iran. République islamique d’', 359713.15, 43533.59], ['Iraq', 207889.33, 5033.16], ['Irlande', 504182.6, 372.52], ['Islande', 25602.42, 9364.0], ['Israël', 488526.55, 59109.67], ['Italie', 2107702.84, 2827.7], ['Jamaïque', 14657.59, 125681.59], ['Japon', 4940877.78, 11148.28], ['Jordanie', 45744.27, 19000.99], ['Kazakhstan', 197112.26, 53005.61], ['Kenya', 110347.08, 128.87], ['Kiribati', 207.03, 1786.04], ['Kosovo', 9412.03, 4250.11], ['Koweït', 105960.23, 2281.45], ['Lesotho', 2496.13, 1884.49], ['Lettonie', 39853.5, 5592.63], ['Liban', 23131.94, 5193.42], ['Libéria', 3509.0, 6735.28], ['Libye', 42817.47, 39.04], ['Liechtenstein', 6113.95, 2800.84], ['Lituanie', 66445.26, 640.06], ['Luxembourg', 85506.24, 2065.09], ['Macédoine du Nord', 13825.05, 28915.65], ['Madagascar', 14472.6, 33573.87], ['Malaisie', 372980.96, 19889.74], ['Malawi', 12626.72, 521.46], ['Maldives', 5405.58, 21904.98], ['Mali', 19140.46, 518.54], ['Malte', 17364.04, 49.48], ['Mariannes', 1182.0, 37076.58], ['Maroc', 142866.33, 1266.06], ['Maurice', 11529.04, 4614.97], ['Mauritanie', 9996.25, 126705.14], ['Mexique', 1272839.33, 113.13], ['Micronésie. États fédérés de', 404.03, 2615.2], ['Moldova', 13679.22, 36.69], ['Monaco', 8596.1, 3347.78], ['Mongolie', 15286.44, 619.21], ['Monténégro', 5861.27, 32077.07], ['Mozambique', 15776.76, 53798.08], ['Myanmar', 65091.75, 2530.15], ['Namibie', 12310.6, 12.51], ['Nauru', 133.22, 30034.99], ['Népal', 36288.83, 6850.54], ['Nicaragua', 14013.02, 25252.72], ['Niger', 14915.0, 213401.32], ['Nigéria', 440833.58, 5408.32], ['Norvège', 482174.85, 271.03], ['Nouvelle-Calédonie', 10071.35, 5122.6], ['Nouvelle-Zélande', 249885.69, 4520.47], ['Oman', 88191.98, 45853.78], ['Ouganda', 40529.79, 34915.1], ['Ouzbékistan', 69238.9, 231402.12], ['Pakistan', 348262.54, 18.02], ['Palaos', 217.8, 4351.27], ['Panama', 63605.1, 9949.44], ['Papouasie-Nouvelle-Guinée', 26594.31, 6703.8], ['Paraguay', 39495.43, 17533.04], ['Pays-Bas', 1012846.76, 33715.47], ['Pérou', 223249.5, 113880.33], ['Philippines', 394086.4, 37747.12], ['Pologne', 679444.83, 304.03], ['Polynésie française', 6054.68, 3263.58], ['Porto Rico', 106525.7, 10325.15], ['Portugal', 253663.14, 2688.24], ['Qatar', 179677.21, 686.61], ['Région administrative spéciale de Macao. Chine', 30123.91, 21324.37], ['République arabe syrienne', 11079.8, 5457.15], ['République centrafricaine', 2516.5, 7425.06], ['République dominicaine', 94243.45, 11117.87], ['République kirghize', 8543.42, 6691.8], ['République slovaque', 116527.1, 5447.25], ['République tchèque', 281777.89, 10505.77], ['Roumanie', 284087.56, 19119.88], ['Royaume-Uni', 3131377.76, 67326.57], ['Rwanda', 11070.36, 13461.89], ['Saint-Kitts-et-Nevis', 860.84, 47.61], ['Saint-Marin', 1541.2, 33.74], ['Saint-Martin (fr)', 772.95, 31.95], ['Saint-Vincent-et-les Grenadines', 904.18, 104.33], ['Sainte-Lucie', 1691.28, 179.65], ['Samoa', 843.84, 218.76], ['Samoa américaines', 709.0, 45.03], ['Sao Tomé-et-Principe', 526.65, 223.11], ['Sénégal', 27625.39, 16876.72], ['Serbie', 63082.05, 6834.33], ['Seychelles', 1454.46, 99.26], ['Sierra Leone', 4042.24, 8420.64], ['Singapour', 396986.9, 5453.57], ['Sint Maarten (Dutch part)', 1185.47, 42.85], ['Slovénie', 61748.59, 2108.08], ['Somalie', 7628.0, 17065.58], ['Soudan', 34326.06, 45657.2], ['Soudan du Sud', 11997.8, 10748.27], ['Sri Lanka', 88927.26, 22156.0], ['Suède', 635663.8, 10415.81], ['Suisse', 800640.16, 8703.41], ['Suriname', 2984.71, 612.99], ['Tadjikistan', 8746.27, 9750.06], ['Tanzanie', 67841.05, 63588.33], ['Tchad', 11779.98, 17179.74], ['Thaïlande', 505947.04, 71601.1], ['Timor-Leste', 3621.22, 1320.94], ['Togo', 8413.2, 8644.83], ['Tonga', 469.23, 106.02], ['Trinité-et-Tobago', 24460.2, 1525.66], ['Tunisie', 46686.74, 12262.95], ['Turkménistan', 45231.43, 6341.85], ['Turquie', 819035.18, 84775.4], ['Tuvalu', 63.1, 11.2], ['Ukraine', 200085.54, 43792.86], ['Uruguay', 59319.48, 3426.26], ['Vanuatu', 956.33, 319.14], ['Venezuela', 482359.32, 28199.87], ['Viet Nam', 366137.59, 97468.03], ['Yémen. Rép. du', 21606.16, 32981.64], ['Zambie', 22147.63, 19473.13], ['Zimbabwe', 28371.24, 15993.52]]
        self.pays = [
            ["Russie", 1778782.63, 143449.29, "ru.png"],
            ["France", 2957879.76, 67749.63, "fr.png"],
            ["Chine", 17734062.65, 1412360.0, "cn.png"],
            ["États-Unis", 23315080.56, 331893.74, "us.png"],
            ["Iran", 359713.15, 87923.43, "ir.png"],
        ]
        self.user_interface = None
        self.user_pays = None
        self.etat_onglet = False
        self.id_onglet = None
        self.user_electricity = None
        self.user_manufacture = None
        self.user_ressource = None
        self.user_infrastructure = None
        self.user_market_economy = None
        self.game_date = Date()
        self.clock = pygame.time.Clock()

    # init all of country
    def set_id_onglet(self, value):
        self.id_onglet = value

    def createmap(self):
        for i in range(len(self.pays)):
            Pays(
                self.pays[i][0],
                self.pays[i][1],
                self.pays[i][2],
                self.pays[i][3],
                self.screen,
            )

    def interface(self, event):
        # horizontale bar
        h_bar = pygame.draw.rect(
            self.screen,
            self.dark_grey,
            (
                self.v_bar_size[0],
                self.h_bar_pos[1],
                self.h_bar_size[0],
                self.h_bar_size[1],
            ),
        )
        # vertical bar
        icon_politics = pygame.transform.smoothscale(
            pygame.image.load("images/icon/politics.png"), self.icon_size[1]
        )
        icon_money = pygame.transform.smoothscale(
            pygame.image.load("images/icon/money.png"), self.icon_size[1]
        )
        icon_industry = pygame.transform.smoothscale(
            pygame.image.load("images/icon/industry.png"), self.icon_size[1]
        )
        icon_container = pygame.transform.smoothscale(
            pygame.image.load("images/icon/container.png"), self.icon_size[1]
        )
        icon_world = pygame.transform.smoothscale(
            pygame.image.load("images/icon/world.png"), self.icon_size[1]
        )

        v_bar = pygame.draw.rect(
            self.screen,
            self.dark_grey,
            (
                self.v_bar_pos[0],
                self.v_bar_pos[1],
                self.v_bar_size[0],
                self.v_bar_size[1],
            ),
        )

        pygame.draw.rect(
            self.screen,
            self.light_grey,
            (
                0,
                self.v_bar_pos[1] + self.padding[1] - self.padding[0],
                self.icon_size[1][1] + self.padding[0] + self.padding[0],
                self.icon_size[1][1] + self.padding[0] + self.padding[0],
            ),
        )

        v_bar_p = self.screen.blit(
            icon_politics, (self.padding[0], self.v_bar_pos[1] + self.padding[1])
        )

        pygame.draw.rect(
            self.screen,
            self.light_grey,
            (
                0,
                self.v_bar_pos[1] + self.padding[1] + self.padding[2] - self.padding[0],
                self.icon_size[1][1] + self.padding[0] + self.padding[0],
                self.icon_size[1][1] + self.padding[0] + self.padding[0],
            ),
        )

        v_bar_m = self.screen.blit(
            icon_money,
            (self.padding[0], self.v_bar_pos[1] + self.padding[1] + self.padding[2]),
        )

        pygame.draw.rect(
            self.screen,
            self.light_grey,
            (
                0,
                self.v_bar_pos[1]
                + self.padding[1]
                + self.padding[2] * 2
                - self.padding[0],
                self.icon_size[1][1] + self.padding[0] + self.padding[0],
                self.icon_size[1][1] + self.padding[0] + self.padding[0],
            ),
        )

        v_bar_i = self.screen.blit(
            icon_industry,
            (
                self.padding[0],
                self.v_bar_pos[1] + self.padding[1] + self.padding[2] * 2,
            ),
        )

        pygame.draw.rect(
            self.screen,
            self.light_grey,
            (
                0,
                self.v_bar_pos[1]
                + self.padding[1]
                + self.padding[2] * 3
                - self.padding[0],
                self.icon_size[1][1] + self.padding[0] + self.padding[0],
                self.icon_size[1][1] + self.padding[0] + self.padding[0],
            ),
        )

        v_bar_c = self.screen.blit(
            icon_container,
            (
                self.padding[0],
                self.v_bar_pos[1] + self.padding[1] + self.padding[2] * 3,
            ),
        )

        pygame.draw.rect(
            self.screen,
            self.light_grey,
            (
                0,
                self.v_bar_pos[1]
                + self.padding[1]
                + self.padding[2] * 4
                - self.padding[0],
                self.icon_size[1][1] + self.padding[0] + self.padding[0],
                self.icon_size[1][1] + self.padding[0] + self.padding[0],
            ),
        )

        v_bar_w = self.screen.blit(
            icon_world,
            (
                self.padding[0],
                self.v_bar_pos[1] + self.padding[1] + self.padding[2] * 4,
            ),
        )

        # header
        flag = pygame.image.load("images/flag/bigflag/" + self.user_pays.get_flag())
        header = pygame.draw.rect(
            self.screen,
            self.dark_grey,
            (
                self.header_pos[0],
                self.header_pos[1],
                self.header_size[0],
                self.header_size[1],
            ),
        )
        header_flag = self.screen.blit(
            flag,
            (self.screen_width - flag.get_width() - self.padding[0], self.padding[0]),
        )
        text = self.police.render(
            "PIB : "
            + str(self.user_pays.get_pib())
            + "(millers)  Nbh : "
            + str(self.user_pays.get_nbh())
            + "(milliers) ",
            True,
            self.white,
        )
        self.screen.blit(text, (self.header_pos[0] + self.padding[2], self.padding[0]))

        # onglet event
        val = None
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if v_bar_i.collidepoint(pygame.mouse.get_pos()):
                self.etat_onglet = True
                self.id_onglet = 1

            elif v_bar_p.collidepoint(pygame.mouse.get_pos()):
                self.etat_onglet = True
                self.id_onglet = 2

            elif v_bar_m.collidepoint(pygame.mouse.get_pos()):
                self.etat_onglet = True
                self.id_onglet = 3

            elif v_bar_c.collidepoint(pygame.mouse.get_pos()):
                self.etat_onglet = True
                self.id_onglet = 4

            elif v_bar_w.collidepoint(pygame.mouse.get_pos()):
                self.etat_onglet = True
                self.id_onglet = 5
        self.onglet(event)
        self.date()

    def onglet(self, event):
        self.user_electricity = self.user_pays.get_electricty()
        self.user_manufacture = self.user_pays.get_manufacture()
        self.user_ressource = self.user_pays.get_ressource()
        self.user_infrastructure = self.user_pays.get_infrastructure()
        self.user_interface = Interface(
            self,
            self.screen,
            self.v_bar_size,
            self.v_bar_pos,
            self.h_bar_size,
            self.h_bar_pos,
            self.onglet_size,
            self.onglet_pos,
            self.padding,
            self.police,
            self.police2,
            self.icon_size,
            self.user_pays,
            self.user_electricity,
            self.user_manufacture,
            self.user_ressource,
            self.user_infrastructure,
            self.user_market_economy,
        )

        if self.etat_onglet == True:
            icon_cross = pygame.transform.smoothscale(
                pygame.image.load("images/icon/cross.png"), self.icon_size[0]
            )
            rect = pygame.Surface(
                (self.onglet_size[0], self.onglet_size[1]), pygame.SRCALPHA
            )
            rect.fill(self.dark_grey_opacity)
            draw_onglet = self.screen.blit(
                rect, (self.onglet_pos[0], self.onglet_pos[1])
            )
            onglet_cross = self.screen.blit(
                icon_cross,
                (
                    self.onglet_size[0] + self.v_bar_size[0] - self.icon_size[0][0] / 2,
                    self.onglet_pos[1] - self.icon_size[0][0] / 2,
                ),
            )
            self.etat_onglet = True
            if self.id_onglet == 1:
                self.user_interface.display_electricity(event)
            if self.id_onglet == 4:
                self.user_interface.display_market_economy(event, 0)
            if self.id_onglet == 6:
                self.user_interface.display_manufacture(event, 0)
            if self.id_onglet == 7:
                self.user_interface.display_manufacture(event, 6)
            if self.id_onglet == 8:
                self.user_interface.display_ressource(event, 0)
            if self.id_onglet == 9:
                self.user_interface.display_ressource(event, 6)
            if self.id_onglet == 10:
                self.user_interface.display_infrastructure(event)
            if self.id_onglet == 11:
                self.user_interface.display_market_economy(event, 11)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if onglet_cross.collidepoint(pygame.mouse.get_pos()):
                    icon_cross.fill(self.dark_grey)
                    icon_cross = icon_cross.convert_alpha()
                    del icon_cross
                    self.etat_onglet = False
                    self.id_onglet = 0

    def date(self):
        icon_date = pygame.transform.smoothscale(
            pygame.image.load("images/icon/date.png"), (160, 60)
        )
        draw_date = self.screen.blit(icon_date, (30, -13))
        text = self.police.render(str(self.game_date.get_date()), True, self.dark_grey)
        self.screen.blit(text, (70, 8))

    def choice_country(self):
        print("Entre 0, 1, 2, 3 ou 4 pour choisir un pays")
        for i in range(len(self.pays)):
            print(" Pays : " + self.pays[i][0] + " numero : " + str(i))
        val = int(input("Choix numero :"))
        for i in range(len(self.pays)):
            if i == val:
                self.user_pays = Pays(
                    self.pays[i][0],
                    self.pays[i][1],
                    self.pays[i][2],
                    self.pays[i][3],
                    self.screen,
                )

    def move_background(self):
        bg_w, bg_h = self.size
        pos_x = 0
        speed = 10
        done = False

        while not done:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            allKeys = pygame.key.get_pressed()
            pos_x += (
                speed
                if allKeys[pygame.K_LEFT]
                else -speed
                if allKeys[pygame.K_RIGHT]
                else 0
            )

            x_rel = pos_x % bg_w
            x_part2 = x_rel - bg_w if x_rel > 0 else x_rel + bg_w
            self.screen.blit(self.background, (x_rel, 0))
            self.screen.blit(self.background, (x_part2, 0))
            pygame.display.flip()

    def play(self):
        running = True
        self.choice_country()
        print(self.user_pays)

        self.move_background()

        # self.createmap()
        while running:
            for event in pygame.event.get():
                self.screen.blit(self.background, (0, 0))
                self.interface(event)
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            pygame.display.update()
        pygame.quit()


Main().play()
