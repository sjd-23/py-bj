import pygame

class Controller:
    def __init__(self, model, view):
        self.game_running = True
        self.model = model
        self.view = view
        self.player_turn = True
        self.dealer_turn = False
        self.player_bust = False

    def update(self):
        self._detect_input()

        # Initial deal
        if len(self.model.player.hand) < 2:
            self.model.deck.deal_into(self.model.player)
        if len(self.model.dealer.hand) < 1:
            self.model.deck.deal_into(self.model.dealer)

        if self.model.player.calculate_hand_value() >= 22:
            self.player_bust = True
            self.player_turn = False
            self.view.game_over_ui.player_won = False

        if not self.player_turn:
            self.view.hit_ui.color = (195, 82, 82)
            self.view.stay_ui.color = (192, 82, 82)
            if not self.player_bust:
                self._handle_dealer_turn()
            else:
                self._handle_game_over()

    def _detect_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
                return
            elif event.type == pygame.KEYDOWN:
                self._handle_key_down(event.key)
            elif event.type == pygame.MOUSEMOTION:
                self._handle_mouse_motion(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_mouse_down(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                self._handle_mouse_up(event)

    def _handle_key_down(self, key):
        pass

    def _handle_mouse_motion(self, event):
        for card in reversed(self.model.player.hand):
            if card.rect.collidepoint(event.pos):
                card.highlight = True
            else:
                card.highlight = False

        for card in reversed(self.model.dealer.hand):
            if card.rect.collidepoint(event.pos):
                card.highlight = True
            else:
                card.highlight = False

        if self.view.hit_ui.area.collidepoint(event.pos) and self.player_turn:
            self.view.hit_ui.color = "white"
        elif self.player_turn:
            self.view.hit_ui.color = "gray"

        if self.view.stay_ui.area.collidepoint(event.pos) and self.player_turn:
            self.view.stay_ui.color = "white"
        elif self.player_turn:
            self.view.stay_ui.color = "gray"

        if self.view.game_over_ui.again_area.collidepoint(event.pos):
            self.view.game_over_ui.again_color = "yellow"
        else:
            self.view.game_over_ui.again_color = "gray"

        if self.view.game_over_ui.quit_area.collidepoint(event.pos):
            self.view.game_over_ui.quit_color = "red"
        else:
            self.view.game_over_ui.quit_color = "gray"

    def _handle_mouse_down(self, event):
        if event.button == 1:
            if self.view.hit_ui.area.collidepoint(event.pos) and self.player_turn:
                self.model.deck.deal_into(self.model.player)
            elif self.view.stay_ui.area.collidepoint(event.pos) and self.player_turn:
                self.player_turn = False
            elif self.view.game_over_ui.quit_area.collidepoint(event.pos) and not self.view.game_over_ui.hidden:
                self.game_running = False
            elif self.view.game_over_ui.again_area.collidepoint(event.pos) and not self.view.game_over_ui.hidden:
                self.model.deck.reset()
                self.model.deck.shuffle()
                self.model.player.hand = []
                self.model.dealer.hand = []
                self.player_turn = True
                self.dealer_turn = False
                self.player_bust = False
                self.view.game_over_ui.hidden = True
                self.view.game_over_ui.player_won = True
                self.view.game_over_ui.push = False


    def _handle_mouse_up(self, event):
        if event.button == 1:
            pass

    def _handle_dealer_turn(self):

        while self.model.dealer.calculate_hand_value() < 17:
            self.model.deck.deal_into(self.model.dealer)
            self.view.draw()
            pygame.time.wait(850)

        if 21 >= self.model.dealer.calculate_hand_value() > self.model.player.calculate_hand_value():
            self.view.game_over_ui.player_won = False
        elif 21 >= self.model.dealer.calculate_hand_value() == self.model.player.calculate_hand_value():
            self.view.game_over_ui.push = True

        self._handle_game_over()

    def _handle_game_over(self):
        self.view.game_over_ui.hidden = False