import pygame
from math import floor


class Interface(object):
    def __init__(
        self,
        main,
        screen,
        v_bar_size,
        v_bar_pos,
        h_bar_size,
        h_bar_pos,
        onglet_size,
        onglet_pos,
        padding,
        police,
        police2,
        icon_size,
        user_pays,
        user_electricity,
        user_manufacture,
        user_ressource,
        user_infrastructure,
        user_market_economy,
    ):
        self.screen = screen

        self.v_bar_size = v_bar_size
        self.v_bar_pos = v_bar_pos

        self.h_bar_size = h_bar_size
        self.h_bar_pos = h_bar_pos

        self.onglet_size = onglet_size
        self.onglet_pos = onglet_pos

        self.padding = padding
        self.police = police
        self.police2 = police2
        self.icon_size = icon_size
        self.white = [255, 255, 255]

        self.main = main
        self.user_pays = user_pays
        self.user_electricity = user_electricity
        self.user_manufacture = user_manufacture
        self.user_ressource = user_ressource
        self.user_infrastructure = user_infrastructure
        self.user_market_economy = user_market_economy

        self.icon = {
            "plus": pygame.transform.scale(
                pygame.image.load("images/icon/plus.png"), self.icon_size[1]
            ),
            "next": pygame.transform.scale(
                pygame.image.load("images/icon/down_arrow.png"), self.icon_size[1]
            ),
            "industry": pygame.transform.scale(
                pygame.image.load("images/icon/industry.png"), self.icon_size[2]
            ),
        }

    def display_electricity(self, event):
        liste_icon_centrale = []
        x = self.v_bar_size[0] + self.padding[1]
        y = self.v_bar_pos[1] + self.padding[1]

        titre_onglet = self.police2.render("Batiments", True, self.white)
        self.screen.blit(titre_onglet, (x + self.icon_size[1][1] + self.padding[2], y))

        y += self.icon_size[2][1] + self.padding[1]
        # display electricity
        for centrale in self.user_electricity.get_liste_centrale():
            display_centrale_icon = self.screen.blit(self.icon["industry"], (x, y))
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if onglet_manufacture.collidepoint(pygame.mouse.get_pos()):
                if event.button == 1:
                    self.main.set_id_onglet(6)

            elif onglet_ressource.collidepoint(pygame.mouse.get_pos()):
                if event.button == 1:
                    self.main.set_id_onglet(8)

            elif onglet_infrastructure.collidepoint(pygame.mouse.get_pos()):
                if event.button == 1:
                    self.main.set_id_onglet(10)

            elif liste_icon_centrale[0].collidepoint(pygame.mouse.get_pos()):
                if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_electricity.set_centrale_charbon(10)
                elif event.button == 1:
                    self.user_electricity.set_centrale_charbon(1)

            elif liste_icon_centrale[1].collidepoint(pygame.mouse.get_pos()):
                if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_electricity.set_centrale_gaz(10)
                elif event.button == 1:
                    self.user_electricity.set_centrale_gaz(1)

            elif liste_icon_centrale[2].collidepoint(pygame.mouse.get_pos()):
                if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_electricity.set_centrale_fioul(10)
                elif event.button == 1:
                    self.user_electricity.set_centrale_fioul(1)

            elif liste_icon_centrale[3].collidepoint(pygame.mouse.get_pos()):
                if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_electricity.set_centrale_nucleaire(10)
                elif event.button == 1:
                    self.user_electricity.set_centrale_nucleaire(1)

            elif liste_icon_centrale[4].collidepoint(pygame.mouse.get_pos()):
                if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_electricity.set_centrale_hydroelectrique(10)
                elif event.button == 1:
                    self.user_electricity.set_centrale_hydroelectrique(1)

            elif liste_icon_centrale[5].collidepoint(pygame.mouse.get_pos()):
                if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_electricity.set_energie_renouvelable(10)
                elif event.button == 1:
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
            display_usines_icon = self.screen.blit(self.icon["industry"], (x, y))
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if next.collidepoint(pygame.mouse.get_pos()):
                if event.button == 1:
                    if i < 7:
                        self.main.set_id_onglet(7)
                    else:
                        self.main.set_id_onglet(6)

            elif onglet_electricite.collidepoint(pygame.mouse.get_pos()):
                if event.button == 1:
                    self.main.set_id_onglet(1)

            elif onglet_ressource.collidepoint(pygame.mouse.get_pos()):
                if event.button == 1:
                    self.main.set_id_onglet(8)

            elif onglet_infrastructure.collidepoint(pygame.mouse.get_pos()):
                if event.button == 1:
                    self.main.set_id_onglet(10)

            elif i < 7:
                if liste_icon_usines[0].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_manufacture.set_vetement(10)
                    elif event.button == 1:
                        self.user_manufacture.set_vetement(1)

                elif liste_icon_usines[1].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_manufacture.set_meuble(10)
                    elif event.button == 1:
                        self.user_manufacture.set_meuble(1)

                elif liste_icon_usines[2].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_manufacture.set_outil(10)
                    elif event.button == 1:
                        self.user_manufacture.set_outil(1)

                elif liste_icon_usines[3].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_manufacture.set_semi_conducteur(10)
                    elif event.button == 1:
                        self.user_manufacture.set_semi_conducteur(1)

                elif liste_icon_usines[4].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_manufacture.set_appareil_connecte(10)
                    elif event.button == 1:
                        self.user_manufacture.set_appareil_connecte(1)

                elif liste_icon_usines[5].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_manufacture.set_acier(10)
                    elif event.button == 1:
                        self.user_manufacture.set_acier(1)
            else:
                if liste_icon_usines[6].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_manufacture.set_produit_chimique(10)
                    elif event.button == 1:
                        self.user_manufacture.set_produit_chimique(1)

                elif liste_icon_usines[7].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_manufacture.set_vehicule(10)
                    elif event.button == 1:
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
            display_usines_icon = self.screen.blit(self.icon["industry"], (x, y))
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if next.collidepoint(pygame.mouse.get_pos()):
                if event.button == 1:
                    if i < 7:
                        self.main.set_id_onglet(9)
                    else:
                        self.main.set_id_onglet(8)

            elif onglet_electricite.collidepoint(pygame.mouse.get_pos()):
                if event.button == 1:
                    self.main.set_id_onglet(1)

            elif onglet_manufacture.collidepoint(pygame.mouse.get_pos()):
                if event.button == 1:
                    self.main.set_id_onglet(6)

            elif onglet_infrastructure.collidepoint(pygame.mouse.get_pos()):
                if event.button == 1:
                    self.main.set_id_onglet(10)

            elif i < 7:
                if liste_icon_ressources[0].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_ressource.set_charbon(10)
                    elif event.button == 1:
                        self.user_ressource.set_charbon(1)

                elif liste_icon_ressources[1].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_ressource.set_gaz(10)
                    elif event.button == 1:
                        self.user_ressource.set_gaz(1)

                elif liste_icon_ressources[2].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_ressource.set_culture(10)
                    elif event.button == 1:
                        self.user_ressource.set_culture(1)

                elif liste_icon_ressources[3].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_ressource.set_elevage(10)
                    elif event.button == 1:
                        self.user_ressource.set_elevage(1)

                elif liste_icon_ressources[4].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_ressource.set_uranium(10)
                    elif event.button == 1:
                        self.user_ressource.set_uranium(1)

                elif liste_icon_ressources[5].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_ressource.set_petrole(10)
                    elif event.button == 1:
                        self.user_ressource.set_petrole(1)
            else:
                if liste_icon_ressources[6].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_ressource.set_fer(10)
                    elif event.button == 1:
                        self.user_ressource.set_fer(1)

                elif liste_icon_ressources[7].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_ressource.set_matieres_premieres_strategiques(10)
                    elif event.button == 1:
                        self.user_ressource.set_matieres_premieres_strategiques(1)

                elif liste_icon_ressources[8].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        self.user_ressource.set_bois(10)
                    elif event.button == 1:
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
                self.icon["industry"], (x, y)
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if onglet_electricite.collidepoint(pygame.mouse.get_pos()):
                if event.button == 1:
                    self.main.set_id_onglet(1)

            elif onglet_manufacture.collidepoint(pygame.mouse.get_pos()):
                if event.button == 1:
                    self.main.set_id_onglet(6)

            elif onglet_ressource.collidepoint(pygame.mouse.get_pos()):
                if event.button == 1:
                    self.main.set_id_onglet(8)

            elif onglet_infrastructure.collidepoint(pygame.mouse.get_pos()):
                if event.button == 1:
                    self.main.set_id_onglet(10)

            elif liste_icon_infrastructure[0].collidepoint(pygame.mouse.get_pos()):
                if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_infrastructure.set_construction(10)
                elif event.button == 1:
                    self.user_infrastructure.set_construction(1)

            elif liste_icon_infrastructure[1].collidepoint(pygame.mouse.get_pos()):
                if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_infrastructure.set_transport(10)
                elif event.button == 1:
                    self.user_infrastructure.set_transport(1)

            elif liste_icon_infrastructure[2].collidepoint(pygame.mouse.get_pos()):
                if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_infrastructure.set_port(10)
                elif event.button == 1:
                    self.user_infrastructure.set_port(1)

            elif liste_icon_infrastructure[3].collidepoint(pygame.mouse.get_pos()):
                if event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.user_infrastructure.set_administration(10)
                elif event.button == 1:
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
            self.screen.blit(demand, (x + self.padding[2], y))
            y += self.padding[1]
            i += 1

        next = self.screen.blit(
            self.icon["next"], (self.onglet_size[0] - self.padding[1], y)
        )

        self.event_market_economy(event, next, i)

    def event_market_economy(self, event, next, i):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if next.collidepoint(pygame.mouse.get_pos()):
                if event.button == 1:
                    if i < 12:
                        self.main.set_id_onglet(11)
                    else:
                        self.main.set_id_onglet(4)
