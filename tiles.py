import items, world, actions, enemies


class MapTile:
    """The base class for a tile within the world space"""

    def __init__(self, x, y):
        """Creates a new tile.
        :param x: the x-coordinate of the tile
        :param y: the y-coordinate of the tile
        """
        self.x = x
        self.y = y

    def intro_text(self):
        """Information to be displayed when the player moves into this tile."""
        raise NotImplementedError()

    def modify_player(self, the_player):
        """Process actions that change the state of the player."""
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves


class StartingRoom(MapTile):
    def intro_text(self):
        return """
        The town square is a large open space with a fountain in the center. Streets lead in all directions.
        """

    def modify_player(self, the_player):
        # Room has no action on player
        pass


class DirtRoad(MapTile):
    def intro_text(self):
        return """
        Some well-traveled road extends before you. You must forge onwards.
        """

    def modify_player(self, the_player):
        # Room has no action on player
        pass


class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """

    def modify_player(self, the_player):
        # Room has no action on player
        pass


class LootRoom(MapTile):
    """A room that adds something to the player's inventory"""

    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, the_player):
        the_player.inventory.append(self.item)

    def modify_player(self, the_player):
        self.add_loot(the_player)


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It's a dagger! You pick it up.
        """


class Road:
    def intro_text(self):
        return """
        A dirt road lies before you. Both sides are flanked by wildflowers of various bright colors, followed by 
        dense, towering trees that mark the entrance into the Wildlands Forest.
        """

class InnerCave:
    def intro_text(self):
        return """
        Looking around the cave, the only light comes from the entrance, dimly lighting the interior of this damp, 
        dark cave. Many stalactites grip tight to the roof of the room, while stalagmites sit beneath, lining either 
        side like sharp, glistening teeth.
        """

class DeliveryBoy:
    def intro_text(self):
        return """
        Sitting in the middle of the road is a tall, thin looking man. He's carrying a squat, red, square bag that 
        seems to be packed tightly with something. The man looks nervously at a piece of paper in his hand and then at
         the forest, he seems to be debating whether to walk in or to stick to the safety of the road. 
        """

class RoadSplit:
    def intro_text(self):
        return """
        You stand at a split on the road, going West and East. A road sign stands at the middle of the spilt, arrows 
        made of wood pointing at both sides of the split, detailing the towns in each direction.
        """

class TownBridge:
    def intro_text(self):
        return """
        You stand on a long wooden bridge, a deep moat lies on either side, you can see something beneath the water
         moving suspiciously.
        """


class TownSquare:
    def intro_text(self):
        return """
        The town square is a large open space with a fountain in the center. Streets lead in all directions.
        """


class Theives_Guild:
    def intro_text(self):
        return """
           You stand on a long wooden bridge, a deep moat lies on either side, you can see something beneath the water
           moving suspiciously.The Thief Guild is a dark den of unprincipled types. You clutch your purse (though
            several other people here would like to clutch your purse as well).
           """


class TownGate:
    def intro_text(self):
        return """
        You stand on a long wooden bridge, a deep moat lies on either side, you can see something beneath the water
        moving suspiciously.
        """


class Bakery:
    def intro_text(self):
        return """
        The delightful smell of meat pies fills the air, making you hungry. The baker flashes a grin, as he
         slides a box marked "Not Human Organs" under a table with his foot.
        """


class North_Y_Street:
    def intro_text(self):
        return """
        You stand on a long wooden bridge, a deep moat lies on either side, you can see something beneath the water
         moving suspiciously.
        """


class Used_Anvil_Store:
    def intro_text(self):
        return """
        The anvil store has anvils of all types and sizes, each previously-owned but still in servicable 
        condition. However, due to a bug in the way this game is designed, you can buy anvils like any other 
        item and walk around, but if you drop them they cannot be picked up since their TAKEABLE value is set to
         False. The code should be changed so that it\'s not possible for shops to sell items with TAKEABLE set
          to False.
        """


class West_X_Street:
    def intro_text(self):
        return """
        West X Street is the rich section of town. So rich, they paved the streets with gold. This probably was
         not a good idea. The thief guild opened up the next day.
        """


class South_Y_Street:
    def intro_text(self):
        return """
        The Christmas Carolers of South Y Street are famous for all legally changing their name to Carol. They
        are also famous for singing year-round, in heavy fur coats and wool mittens, even in the summer. 
        That\'s dedication to their craft!
        """


class Wizard_Tower:
    def intro_text(self):
        return """
        Zanny magical antics are afoot in the world-famous Wizard Tower. Cauldrons bubble, rats talk, and books
         float midair in this center of magical discovery.
        """


class Observation_Deck:
    def intro_text(self):
        return """
        You can see the entire town from the top of the Wizard Tower. Everybody looks like ants, especially the 
        people transformed into ants by the wizards of the tower!
        """


class Magical_Escalootor_to_Nowhere:
    def intro_text(self):
        return """
        No matter how much you climb the escalator, it doesn\'t seem to be getting you anywhere.
        """


class East_X_Street:
    def intro_text(self):
        return """
        East X Street. It\'s like X Street, except East.
        """


class Blacksmith:
    def intro_text(self):
        return """
        The blacksmith loudly hammers a new sword over her anvil. Swords, axes,and butter knives all line the walls of
         her workshop, available for a price."""


class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5))

    def intro_text(self):
        return """
        Someone dropped a 5 gold piece. You pick it up.
        """


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class SpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.CaveSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """


class TrollRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.CaveTroll())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A Cave Troll is blocking your path!
            """
        else:
            return """
            A dead troll reminds you of your triumph.
            """


class Moat(MapTile):
    def intro_text(self):
        return """
        'You jump in the water, it feels nice and refreshing on this warm day. Not too long after you feel '
        'something bump against your leg, and not a second later you are dragged under the waters surface. Looks '
        'like the town put crocs in their moat for extra protection, tough luck friend!'
        """

    def modify_player(self, player):
        player.hp = 0


class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!
        """

    def modify_player(self, player):
        player.victory = True
