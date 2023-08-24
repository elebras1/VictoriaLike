import pygame


class Menu(object):
    def __init__(self, screen, size, cursor, pays, main):
        self.size = size
        self.main = main
        self.pays = pays
        self.margin = 10
        self.screen_width = pygame.display.Info().current_w
        self.screen_height = pygame.display.Info().current_h
        self.background = pygame.transform.smoothscale(
            pygame.image.load("assets/menu/menu.jpg"), self.size
        )
        self.cursor = cursor
        self.button_size = [230, 50]
        self.screen = screen

        self.tab = 0

        self.button = {
            "play": pygame.transform.scale(
                pygame.image.load("assets/menu/button_play.png"),
                self.button_size,
            ),
            "settings": pygame.transform.scale(
                pygame.image.load("assets/menu/button_settings.png"),
                self.button_size,
            ),
            "exit": pygame.transform.scale(
                pygame.image.load("assets/menu/button_exit.png"),
                self.button_size,
            ),
            "previous": pygame.transform.scale(
                pygame.image.load("assets/menu/button_previous.png"),
                self.button_size,
            ),
        }

    def menu_interface(self, event):
        pos = pygame.mouse.get_pos()
        self.screen.blit(self.cursor, pos)
        self.screen.blit(self.background, (0, 0))
        if self.tab == 0:
            button_play = self.screen.blit(
                self.button["play"],
                (
                    self.screen_width / 2 - self.button["play"].get_width() / 2,
                    self.screen_height / 2,
                ),
            )

            button_settings = self.screen.blit(
                self.button["settings"],
                (
                    self.screen_width / 2 - self.button["settings"].get_width() / 2,
                    self.screen_height / 2
                    + self.button["play"].get_height()
                    + self.margin,
                ),
            )

            button_exit = self.screen.blit(
                self.button["exit"],
                (
                    self.screen_width / 2 - self.button["exit"].get_width() / 2,
                    self.screen_height / 2
                    + self.button["settings"].get_height() * 2
                    + self.margin * 2,
                ),
            )
            self.menu_event(button_play, button_settings, button_exit, event)

        elif self.tab == 1:
            total_width = (
                sum(
                    pygame.image.load("assets/flag/bigflag/" + pays[3]).get_width()
                    for pays in self.pays
                )
                + (len(self.pays) - 1) * self.margin
            )
            start_x = (self.screen_width - total_width) // 2
            pays_ls_img = []

            for pays in self.pays:
                pays_img = pygame.image.load("assets/flag/bigflag/" + pays[3])
                start_y = self.screen_height // 2 - pays_img.get_height() // 2
                pays_ls_img.append(
                    self.screen.blit(
                        pays_img,
                        (start_x, start_y),
                    )
                )
                start_x += pays_img.get_width() + self.margin

            button_previous = self.screen.blit(
                self.button["previous"],
                (
                    self.screen_width / 2 - self.button["previous"].get_width() / 2,
                    self.screen_height / 2 + 40,
                ),
            )

            self.play_event(pays_ls_img, button_previous, event)

    def menu_event(self, button_play, button_settings, button_exit, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_play.collidepoint(pygame.mouse.get_pos()):
                self.tab = 1
            if button_settings.collidepoint(pygame.mouse.get_pos()):
                print("settings")
            if button_exit.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()

    def play_event(self, pays_ls_img, button_previous, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_previous.collidepoint(pygame.mouse.get_pos()):
                self.tab = 0
            for val, pays_img in enumerate(pays_ls_img):
                if pays_img.collidepoint(pygame.mouse.get_pos()):
                    self.main.choice_country(val)

    def exit_event(self, button_exit):
        None

    def play(self):
        running = True
        pygame.mixer.music.play(-1)

        # self.createmap()
        while running:
            for event in pygame.event.get():
                self.menu_interface(event)
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.quit()
            self.main.custom_cursor()
            if self.main.get_user_pays() is not None:
                running = False
            pygame.display.update()
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
