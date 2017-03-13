# Mr. Robot
import rgkit.rg


class Robot:
    def act(self, game):
        self.surrouded_hp = 0
        self.surrouded_bots = 0
        # Allahu-akbar
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rgkit.rg.dist(loc, self.location) <= 1:
                    if bot.hp >= 15:
                        self.surrouded_hp += 15
                    else:
                        self.surrouded_hp += bot.hp
                    self.surrouded_bots += 1
        if self.surrouded_hp > self.hp:
            return ['suicide']

        # if there are enemies around, attack them
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rgkit.rg.dist(loc, self.location) <= 1:
                        return ['attack', loc]

        # if we're in the center, stay put
        if rgkit.rg.dist(self.location, rgkit.rg.CENTER_POINT) <= 5:
            return ['guard']

        # move toward the center
        return ['move', rgkit.rg.toward(self.location, rgkit.rg.CENTER_POINT)]
