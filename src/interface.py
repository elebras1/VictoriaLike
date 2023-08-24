import pygame
from math import floor


class Interface(object):
    def __init__(
        self,
        main,
        screen,
        user_electricity,
        user_manufacture,
        user_ressource,
        user_infrastructure,
        user_market_economy,
        screen_width,
        screen_height,
        police,
        police2,
    ):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen

        self.police = police
        self.police2 = police2
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

        self.main = main
        self.user_pays = self.main.get_user_pays()
        self.user_electricity = user_electricity
        self.user_manufacture = user_manufacture
        self.user_ressource = user_ressource
        self.user_infrastructure = user_infrastructure
        self.user_market_economy = user_market_economy

        self.etat_onglet = False
        self.id_onglet = None

        self.icon = {
            "plus": pygame.transform.smoothscale(
                pygame.image.load("assets/icon/plus.png"), self.icon_size[1]
            ),
            "next": pygame.transform.smoothscale(
                pygame.image.load("assets/icon/down_arrow.png"),
                self.icon_size[1],
            ),
            "politics": pygame.transform.smoothscale(
                pygame.image.load("assets/icon/politics.png"),
                self.icon_size[1],
            ),
            "money": pygame.transform.smoothscale(
                pygame.image.load("assets/icon/money.png"),
                self.icon_size[1],
            ),
            "industry": pygame.transform.smoothscale(
                pygame.image.load("assets/icon/industry.png"),
                self.icon_size[1],
            ),
            "container": pygame.transform.smoothscale(
                pygame.image.load("assets/icon/container.png"),
                self.icon_size[1],
            ),
            "world": pygame.transform.smoothscale(
                pygame.image.load("assets/icon/world.png"),
                self.icon_size[1],
            ),
            "industry2": pygame.transform.smoothscale(
                pygame.image.load("assets/icon/industry.png"), self.icon_size[2]
            ),
            "cross": pygame.transform.smoothscale(
                pygame.image.load("assets/icon/cross.png"), self.icon_size[0]
            ),
        }

    def interface(self, event):
        self.onglet(event)
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
            self.icon["politics"],
            (self.padding[0], self.v_bar_pos[1] + self.padding[1]),
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
            self.icon["money"],
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
            self.icon["industry"],
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
            self.icon["container"],
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
            self.icon["world"],
            (
                self.padding[0],
                self.v_bar_pos[1] + self.padding[1] + self.padding[2] * 4,
            ),
        )

        # header
        flag = pygame.image.load("assets/flag/bigflag/" + self.user_pays.get_flag())
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
            + "(milliers)  Nbh : "
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

    def onglet(self, event):
        self.user_electricity = self.user_pays.get_electricty()
        self.user_manufacture = self.user_pays.get_manufacture()
        self.user_ressource = self.user_pays.get_ressource()
        self.user_infrastructure = self.user_pays.get_infrastructure()

        if self.etat_onglet == True:
            icon_cross = pygame.transform.smoothscale(
                pygame.image.load("assets/icon/cross.png"), self.icon_size[0]
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
                self.display_electricity(event)
            if self.id_onglet == 4:
                self.display_market_economy(event, 0)
            if self.id_onglet == 6:
                self.display_manufacture(event, 0)
            if self.id_onglet == 7:
                self.display_manufacture(event, 6)
            if self.id_onglet == 8:
                self.display_ressource(event, 0)
            if self.id_onglet == 9:
                self.display_ressource(event, 6)
            if self.id_onglet == 10:
                self.display_infrastructure(event)
            if self.id_onglet == 11:
                self.display_market_economy(event, 11)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if onglet_cross.collidepoint(pygame.mouse.get_pos()):
                    icon_cross.fill(self.dark_grey)
                    icon_cross = icon_cross.convert_alpha()
                    del icon_cross
                    self.etat_onglet = False
                    self.id_onglet = 0

    def display_electricity(self, event):
        liste_icon_centrale = []
        x = self.v_bar_size[0] + self.padding[1]
        y = self.v_bar_pos[1] + self.padding[1]

        titre_onglet = self.police2.render("Batiments", True, self.white)
        self.screen.blit(titre_onglet, (x + self.icon_size[1][1] + self.padding[2], y))

        y += self.icon_size[2][1] + self.padding[1]
        # display electricity
        for centrale in self.user_electricity.get_liste_centrale():
            display_centrale_icon = self.screen.blit(self.icon["industry2"], (x, y))
            titre_centrale = self.police.render(centrale[2], True, self.white)
            valeur_centrale = self.police.render(str(centrale[0]), True, self.white)
            self.screen.blit(
                titre_centrale, (x + self.icon_size[1][1] + self.padding[2], y)
            )
            self.screen.blit(
                valeur_centrale,
                (x + self.icon_size[1][1] + self.padding[2], y + self.padding[1]),
            )
            liste_icon_centrale.append(
                self.screen.blit(
                    self.icon["plus"], (self.onglet_size[0] - self.padding[1], y)
                )
            )
            y += self.icon_size[2][1] + self.padding[1]
        txt_electricite = self.police.render("Électricité", True, self.white)
        onglet_electricite = self.screen.blit(
            txt_electricite,
            (self.v_bar_size[0] + self.padding[1], self.h_bar_pos[1] - self.padding[1]),
        )
        txt_manufacture = self.police.render("Manufacture", True, self.white)
        onglet_manufacture = self.screen.blit(
            txt_manufacture,
            (
                self.v_bar_size[0] + self.padding[1] * 2 + txt_electricite.get_width(),
                self.h_bar_pos[1] - self.padding[1],
            ),
        )
        txt_ressource = self.police.render("Ressource", True, self.white)
        onglet_ressource = self.screen.blit(
            txt_ressource,
            (
                self.v_bar_size[0]
                + self.padding[1] * 3
                + txt_electricite.get_width()
                + txt_manufacture.get_width(),
                self.h_bar_pos[1] - self.padding[1],
            ),
        )
        txt_infrastructure = self.police.render("Infrastructure", True, self.white)
        onglet_infrastructure = self.screen.blit(
            txt_infrastructure,
            (
                self.v_bar_size[0]
                + self.padding[1] * 4
                + txt_electricite.get_width()
                + txt_manufacture.get_width()
                + txt_ressource.get_width(),
                self.h_bar_pos[1] - self.padding[1],
            ),
        )

        self.event_electricity(
            event,
            liste_icon_centrale,
            onglet_manufacture,
            onglet_ressource,
            onglet_infrastructure,
        )

    def event_electricity(
        self,
        event,
        liste_icon_centrale,
        onglet_manufacture,
        onglet_ressource,
        onglet_infrastructure,
    ):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if onglet_manufacture.collidepoint(pygame.mouse.get_pos()):
                self.id_onglet = 6

            elif onglet_ressource.collidepoint(pygame.mouse.get_pos()):
                self.id_onglet = 8

            elif onglet_infrastructure.collidepoint(pygame.mouse.get_pos()):
                self.id_onglet = 10

            elif liste_icon_centrale[0].collidepoint(pygame.mouse.get_pos()):
                if pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_electricity.set_centrale_charbon(10)
                else:
                    self.user_electricity.set_centrale_charbon(1)

            elif liste_icon_centrale[1].collidepoint(pygame.mouse.get_pos()):
                if pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_electricity.set_centrale_gaz(10)
                else:
                    self.user_electricity.set_centrale_gaz(1)

            elif liste_icon_centrale[2].collidepoint(pygame.mouse.get_pos()):
                if pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_electricity.set_centrale_fioul(10)
                else:
                    self.user_electricity.set_centrale_fioul(1)

            elif liste_icon_centrale[3].collidepoint(pygame.mouse.get_pos()):
                if pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_electricity.set_centrale_nucleaire(10)
                else:
                    self.user_electricity.set_centrale_nucleaire(1)

            elif liste_icon_centrale[4].collidepoint(pygame.mouse.get_pos()):
                if pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_electricity.set_centrale_hydroelectrique(10)
                else:
                    self.user_electricity.set_centrale_hydroelectrique(1)

            elif liste_icon_centrale[5].collidepoint(pygame.mouse.get_pos()):
                if pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_electricity.set_energie_renouvelable(10)
                else:
                    self.user_electricity.set_energie_renouvelable(1)

    def display_manufacture(self, event, index):
        liste_icon_usines = [0, 0, 0, 0, 0, 0, 0, 0]
        x = self.v_bar_size[0] + self.padding[1]
        y = self.v_bar_pos[1] + self.padding[1]

        nbiter = index + 6
        i = index
        titre_onglet = self.police2.render("Batiments", True, self.white)
        self.screen.blit(titre_onglet, (x + self.icon_size[1][1] + self.padding[2], y))

        y += self.icon_size[2][1] + self.padding[1]
        # array manufacture
        while i < nbiter and i < len(self.user_manufacture.get_liste_usines()):
            display_usines_icon = self.screen.blit(self.icon["industry2"], (x, y))
            titre_centrale = self.police.render(
                self.user_manufacture.get_liste_usines()[i][1], True, self.white
            )
            valeur_centrale = self.police.render(
                str(self.user_manufacture.get_liste_usines()[i][0]), True, self.white
            )
            self.screen.blit(
                titre_centrale, (x + self.icon_size[1][1] + self.padding[2], y)
            )
            self.screen.blit(
                valeur_centrale,
                (x + self.icon_size[1][1] + self.padding[2], y + self.padding[1]),
            )
            liste_icon_usines[i] = self.screen.blit(
                self.icon["plus"], (self.onglet_size[0] - self.padding[1], y)
            )
            y += self.icon_size[2][1] + self.padding[1]
            i += 1
        txt_electricite = self.police.render("Électricité", True, self.white)
        onglet_electricite = self.screen.blit(
            txt_electricite,
            (self.v_bar_size[0] + self.padding[1], self.h_bar_pos[1] - self.padding[1]),
        )
        txt_manufacture = self.police.render("Manufacture", True, self.white)
        onglet_manufacture = self.screen.blit(
            txt_manufacture,
            (
                self.v_bar_size[0] + self.padding[1] * 2 + txt_electricite.get_width(),
                self.h_bar_pos[1] - self.padding[1],
            ),
        )
        next = self.screen.blit(
            self.icon["next"], (self.onglet_size[0] - self.padding[1], y)
        )
        txt_ressource = self.police.render("Ressource", True, self.white)
        onglet_ressource = self.screen.blit(
            txt_ressource,
            (
                self.v_bar_size[0]
                + self.padding[1] * 3
                + txt_electricite.get_width()
                + txt_manufacture.get_width(),
                self.h_bar_pos[1] - self.padding[1],
            ),
        )
        txt_infrastructure = self.police.render("Infrastructure", True, self.white)
        onglet_infrastructure = self.screen.blit(
            txt_infrastructure,
            (
                self.v_bar_size[0]
                + self.padding[1] * 4
                + txt_electricite.get_width()
                + txt_manufacture.get_width()
                + txt_ressource.get_width(),
                self.h_bar_pos[1] - self.padding[1],
            ),
        )

        self.event_manufacture(
            event,
            liste_icon_usines,
            onglet_electricite,
            onglet_ressource,
            onglet_infrastructure,
            next,
            i,
        )

    def event_manufacture(
        self,
        event,
        liste_icon_usines,
        onglet_electricite,
        onglet_ressource,
        onglet_infrastructure,
        next,
        i,
    ):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if next.collidepoint(pygame.mouse.get_pos()):
                if i < 7:
                    self.id_onglet = 7
                else:
                    self.id_onglet = 6

            elif onglet_electricite.collidepoint(pygame.mouse.get_pos()):
                self.id_onglet = 1

            elif onglet_ressource.collidepoint(pygame.mouse.get_pos()):
                self.id_onglet = 8

            elif onglet_infrastructure.collidepoint(pygame.mouse.get_pos()):
                self.id_onglet = 10

            elif i < 7:
                if liste_icon_usines[0].collidepoint(pygame.mouse.get_pos()):
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_manufacture.set_vetement(10)
                    else:
                        self.user_manufacture.set_vetement(1)

                elif liste_icon_usines[1].collidepoint(pygame.mouse.get_pos()):
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_manufacture.set_meuble(10)
                    else:
                        self.user_manufacture.set_meuble(1)

                elif liste_icon_usines[2].collidepoint(pygame.mouse.get_pos()):
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_manufacture.set_outil(10)
                    else:
                        self.user_manufacture.set_outil(1)

                elif liste_icon_usines[3].collidepoint(pygame.mouse.get_pos()):
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_manufacture.set_semi_conducteur(10)
                    else:
                        self.user_manufacture.set_semi_conducteur(1)

                elif liste_icon_usines[4].collidepoint(pygame.mouse.get_pos()):
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_manufacture.set_appareil_connecte(10)
                    else:
                        self.user_manufacture.set_appareil_connecte(1)

                elif liste_icon_usines[5].collidepoint(pygame.mouse.get_pos()):
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_manufacture.set_acier(10)
                    else:
                        self.user_manufacture.set_acier(1)
            else:
                if liste_icon_usines[6].collidepoint(pygame.mouse.get_pos()):
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_manufacture.set_produit_chimique(10)
                    else:
                        self.user_manufacture.set_produit_chimique(1)

                elif liste_icon_usines[7].collidepoint(pygame.mouse.get_pos()):
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_manufacture.set_vehicule(10)
                    else:
                        self.user_manufacture.set_vehicule(1)

    def display_ressource(self, event, index):
        liste_icon_ressources = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        x = self.v_bar_size[0] + self.padding[1]
        y = self.v_bar_pos[1] + self.padding[1]

        nbiter = index + 6
        i = index

        titre_onglet = self.police2.render("Batiments", True, self.white)
        self.screen.blit(titre_onglet, (x + self.icon_size[1][1] + self.padding[2], y))

        y += self.icon_size[2][1] + self.padding[1]
        # array ressource
        while i < nbiter and i < len(self.user_ressource.get_ressource()):
            display_usines_icon = self.screen.blit(self.icon["industry2"], (x, y))
            titre_centrale = self.police.render(
                self.user_ressource.get_ressource()[i][1], True, self.white
            )
            valeur_centrale = self.police.render(
                str(self.user_ressource.get_ressource()[i][0]), True, self.white
            )
            self.screen.blit(
                titre_centrale, (x + self.icon_size[1][1] + self.padding[2], y)
            )
            self.screen.blit(
                valeur_centrale,
                (x + self.icon_size[1][1] + self.padding[2], y + self.padding[1]),
            )
            liste_icon_ressources[i] = self.screen.blit(
                self.icon["plus"], (self.onglet_size[0] - self.padding[1], y)
            )

            y += self.icon_size[2][1] + self.padding[1]
            i += 1

        txt_electricite = self.police.render("Électricité", True, self.white)
        onglet_electricite = self.screen.blit(
            txt_electricite,
            (self.v_bar_size[0] + self.padding[1], self.h_bar_pos[1] - self.padding[1]),
        )
        txt_manufacture = self.police.render("Manufacture", True, self.white)
        onglet_manufacture = self.screen.blit(
            txt_manufacture,
            (
                self.v_bar_size[0] + self.padding[1] * 2 + txt_electricite.get_width(),
                self.h_bar_pos[1] - self.padding[1],
            ),
        )
        next = self.screen.blit(
            self.icon["next"], (self.onglet_size[0] - self.padding[1], y)
        )
        txt_ressource = self.police.render("Ressource", True, self.white)
        onglet_ressource = self.screen.blit(
            txt_ressource,
            (
                self.v_bar_size[0]
                + self.padding[1] * 3
                + txt_electricite.get_width()
                + txt_manufacture.get_width(),
                self.h_bar_pos[1] - self.padding[1],
            ),
        )
        txt_infrastructure = self.police.render("Infrastructure", True, self.white)
        onglet_infrastructure = self.screen.blit(
            txt_infrastructure,
            (
                self.v_bar_size[0]
                + self.padding[1] * 4
                + txt_electricite.get_width()
                + txt_manufacture.get_width()
                + txt_ressource.get_width(),
                self.h_bar_pos[1] - self.padding[1],
            ),
        )

        self.event_ressource(
            event,
            liste_icon_ressources,
            onglet_electricite,
            onglet_manufacture,
            onglet_infrastructure,
            next,
            i,
        )

    def event_ressource(
        self,
        event,
        liste_icon_ressources,
        onglet_electricite,
        onglet_manufacture,
        onglet_infrastructure,
        next,
        i,
    ):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if next.collidepoint(pygame.mouse.get_pos()):
                if i < 7:
                    self.id_onglet = 9
                else:
                    self.id_onglet = 8

            elif onglet_electricite.collidepoint(pygame.mouse.get_pos()):
                self.id_onglet = 1

            elif onglet_manufacture.collidepoint(pygame.mouse.get_pos()):
                self.id_onglet = 6

            elif onglet_infrastructure.collidepoint(pygame.mouse.get_pos()):
                self.id_onglet = 10

            elif i < 7:
                if liste_icon_ressources[0].collidepoint(pygame.mouse.get_pos()):
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_ressource.set_charbon(10)
                    else:
                        self.user_ressource.set_charbon(1)

                elif liste_icon_ressources[1].collidepoint(pygame.mouse.get_pos()):
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_ressource.set_gaz(10)
                    else:
                        self.user_ressource.set_gaz(1)

                elif liste_icon_ressources[2].collidepoint(pygame.mouse.get_pos()):
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_ressource.set_culture(10)
                    else:
                        self.user_ressource.set_culture(1)

                elif liste_icon_ressources[3].collidepoint(pygame.mouse.get_pos()):
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_ressource.set_elevage(10)
                    else:
                        self.user_ressource.set_elevage(1)

                elif liste_icon_ressources[4].collidepoint(pygame.mouse.get_pos()):
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_ressource.set_uranium(10)
                    else:
                        self.user_ressource.set_uranium(1)

                elif liste_icon_ressources[5].collidepoint(pygame.mouse.get_pos()):
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_ressource.set_petrole(10)
                    else:
                        self.user_ressource.set_petrole(1)
            else:
                if liste_icon_ressources[6].collidepoint(pygame.mouse.get_pos()):
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_ressource.set_fer(10)
                    else:
                        self.user_ressource.set_fer(1)

                elif liste_icon_ressources[7].collidepoint(pygame.mouse.get_pos()):
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_ressource.set_matieres_premieres_strategiques(10)
                    else:
                        self.user_ressource.set_matieres_premieres_strategiques(1)

                elif liste_icon_ressources[8].collidepoint(pygame.mouse.get_pos()):
                    if pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_ressource.set_bois(10)
                    else:
                        self.user_ressource.set_bois(1)

    def display_infrastructure(self, event):
        liste_icon_infrastructure = []
        x = self.v_bar_size[0] + self.padding[1]
        y = self.v_bar_pos[1] + self.padding[1]

        titre_onglet = self.police2.render("Batiments", True, self.white)
        self.screen.blit(titre_onglet, (x + self.icon_size[1][1] + self.padding[2], y))

        y += self.icon_size[2][1] + self.padding[1]
        # display electricity
        for infrastructure in self.user_infrastructure.get_liste_infrastructure():
            display_infrastructure_icon = self.screen.blit(
                self.icon["industry2"], (x, y)
            )
            titre_infrastructure = self.police.render(
                infrastructure[1], True, self.white
            )
            valeur_infrastructure = self.police.render(
                str(infrastructure[0]), True, self.white
            )
            self.screen.blit(
                titre_infrastructure, (x + self.icon_size[1][1] + self.padding[2], y)
            )
            self.screen.blit(
                valeur_infrastructure,
                (x + self.icon_size[1][1] + self.padding[2], y + self.padding[1]),
            )
            liste_icon_infrastructure.append(
                self.screen.blit(
                    self.icon["plus"], (self.onglet_size[0] - self.padding[1], y)
                )
            )
            y += self.icon_size[2][1] + self.padding[1]
        txt_electricite = self.police.render("Électricité", True, self.white)
        onglet_electricite = self.screen.blit(
            txt_electricite,
            (self.v_bar_size[0] + self.padding[1], self.h_bar_pos[1] - self.padding[1]),
        )
        txt_manufacture = self.police.render("Manufacture", True, self.white)
        onglet_manufacture = self.screen.blit(
            txt_manufacture,
            (
                self.v_bar_size[0] + self.padding[1] * 2 + txt_electricite.get_width(),
                self.h_bar_pos[1] - self.padding[1],
            ),
        )
        txt_ressource = self.police.render("Ressource", True, self.white)
        onglet_ressource = self.screen.blit(
            txt_ressource,
            (
                self.v_bar_size[0]
                + self.padding[1] * 3
                + txt_electricite.get_width()
                + txt_manufacture.get_width(),
                self.h_bar_pos[1] - self.padding[1],
            ),
        )
        txt_infrastructure = self.police.render("Infrastructure", True, self.white)
        onglet_infrastructure = self.screen.blit(
            txt_infrastructure,
            (
                self.v_bar_size[0]
                + self.padding[1] * 4
                + txt_electricite.get_width()
                + txt_manufacture.get_width()
                + txt_ressource.get_width(),
                self.h_bar_pos[1] - self.padding[1],
            ),
        )

        self.event_infrastructure(
            event,
            liste_icon_infrastructure,
            onglet_electricite,
            onglet_manufacture,
            onglet_ressource,
            onglet_infrastructure,
        )

    def event_infrastructure(
        self,
        event,
        liste_icon_infrastructure,
        onglet_electricite,
        onglet_manufacture,
        onglet_ressource,
        onglet_infrastructure,
    ):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if onglet_electricite.collidepoint(pygame.mouse.get_pos()):
                self.id_onglet = 1

            elif onglet_manufacture.collidepoint(pygame.mouse.get_pos()):
                self.id_onglet = 6

            elif onglet_ressource.collidepoint(pygame.mouse.get_pos()):
                self.id_onglet = 8

            elif onglet_infrastructure.collidepoint(pygame.mouse.get_pos()):
                self.id_onglet = 10

            elif liste_icon_infrastructure[0].collidepoint(pygame.mouse.get_pos()):
                if pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_infrastructure.set_construction(10)
                else:
                    self.user_infrastructure.set_construction(1)

            elif liste_icon_infrastructure[1].collidepoint(pygame.mouse.get_pos()):
                if pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_infrastructure.set_transport(10)
                else:
                    self.user_infrastructure.set_transport(1)

            elif liste_icon_infrastructure[2].collidepoint(pygame.mouse.get_pos()):
                if pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_infrastructure.set_port(10)
                else:
                    self.user_infrastructure.set_port(1)

            elif liste_icon_infrastructure[3].collidepoint(pygame.mouse.get_pos()):
                if pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_infrastructure.set_administration(10)
                else:
                    self.user_infrastructure.set_administration(1)

    def display_market_economy(self, event, index):
        self.user_market_economy = self.user_pays.get_market_economy()

        x = self.v_bar_size[0] + self.padding[1]
        y = self.v_bar_pos[1] + self.padding[1]

        titre_onglet = self.police2.render(
            self.user_pays.get_nom() + " : Marché", True, self.white
        )
        self.screen.blit(titre_onglet, (x + self.icon_size[1][1] + self.padding[2], y))
        nbiter = index + 11
        i = index
        y += self.icon_size[2][1] + self.padding[1]
        while i < nbiter and i < len(self.user_market_economy.get_offer_demand()):
            titre = self.police.render(
                self.user_market_economy.get_offer_demand()[i][2], True, self.white
            )
            self.screen.blit(titre, (x, y))
            y += floor(self.padding[1] * 0.7)
            offer = self.police.render(
                "Offre : " + str(self.user_market_economy.get_offer_demand()[i][0]),
                True,
                self.white,
            )
            demand = self.police.render(
                "Demande : " + str(self.user_market_economy.get_offer_demand()[i][1]),
                True,
                self.white,
            )
            self.screen.blit(offer, (x, y))
            self.screen.blit(demand, (x + self.padding[2] * 2.5, y))
            y += self.padding[1]
            i += 1

        next = self.screen.blit(
            self.icon["next"], (self.onglet_size[0] - self.padding[1], y)
        )

        self.event_market_economy(event, next, i)

    def event_market_economy(self, event, next, i):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if next.collidepoint(pygame.mouse.get_pos()):
                if i < 12:
                    self.id_onglet = 11
                else:
                    self.id_onglet = 4
