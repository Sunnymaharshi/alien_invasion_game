class GameStats():
    """Track statistics for Alien Invasion."""
    def __init__(self, setting):
        """Initialize statistics."""
        self.setting = setting
        self.reset_stats()
        # Start Alien Invasion in an active state.
        self.game_active = False
        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.setting.ship_limit
        self.score = 0
        self.level = 1
