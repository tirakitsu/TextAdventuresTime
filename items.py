"""Describes the items in the game."""
__author__ = 'Phillip Johnson'


class Item:
    """The base class for all items"""

    def __init__(self, name, description, value, canPick):
        self.name = name
        self.description = description
        self.value = value
        self.canPick = False

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Food(Item):
    def __init__(self, name, description, value, healing):
        self.healing = healing
        super().__init__(name, description, value, canPick=True)

        def __str__(self):
            return "{}\n=====\n{}\nValue: {}\nHealing: {}".format(self.name, self.description, self.value, self.healing)


class Meatpie(Food):
    def __init__(self):
        super().__init__(name="Meat Pie",
                         description="A meat pie. It tastes like chicken.",
                         value=3,
                         healing=10)


class Bagel(Food):
    def __init__(self):
        super().__init__(name="Bagel",
                         description="It is a donut-shaped bagel.",
                         value=1,
                         healing=5)


class Donut(Food):
    def __init__(self):
        super().__init__(name="Donut",
                         description="It is a bagel-shaped donut.",
                         value=1,
                         healing=5)


class Pizza(Food):
    def __init__(self):
        super().__init__(name="Pizza",
                         description="This sweet 'za is covered in many different meats and smells incredible.",
                         value=10,
                         healing=50)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value, canPick=True)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)


class WarAxe(Weapon):
    def __init__(self):
        super().__init__(name="War Axe",
                         description="The mighty war axe is made with antimony from a fallen star, rendering"
                                     " it surprisingly brittle.",
                         value=50,
                         damage=15)


class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="A longsword, engraved with the word, 'Slayer'",
                         value=30,
                         damage=20)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10)


class Armor(Item):
    def __init__(self, name, description, value, protect):
        self.protect = protect
        super().__init__(name, description, value, canPick=True)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nProtection: {}".format(self.name, self.description, self.value, self.protect)


class Chainmail(Armor):
    def __init__(self):
        super().__init__(name="Chainmail Shirt",
                         description="The chainmail t-shirt has a slogan and arrow engraved on the front: 'I\'m with"
                                     " Stupid'",
                         value=15,
                         protect=5)


class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt,
                         canPick=True)


class READMENote(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="README Note",
                         description="The README note reads, 'Welcome to the text adventure demo. Be sure to check out"
                                     " the source code to ' see how this game is put together.'",
                         value=0,
                         canPick=True)


class WornNote(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Worn Note",
                         description="The note reads: 'Wandering into the forest may sound fun, but be warned, there "
                                     "are monsters waiting to strike.'",
                         value=0,
                         canPick=True)


class ShopHowTo(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Shop HOWTO Note",
                         description="The note reads, 'When you are at a shop, you can type 'list' to show what is for "
                                     "sale. 'buy <item>' will add it to your inventory, or you can sell an item in your"
                                     " inventory with 'sell <item>'.",
                         value=0,
                         canPick=True)


class WelcomeSign(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Welcome Sign",
                         description="The welcome sign reads, 'Welcome to this text adventure demo. You can type 'help'"
                                     " for a list of commands to use.",
                         value=0,
                         canPick=False)


class WarningSign(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Warning Sign",
                         description="The warning sign reads, 'Do NOT jump into moat! There are no lifeguards on "
                                     "duty!'.",
                         value=0,
                         canPick=False)


class RoadSign(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Road Sign",
                         description="The road sign reads, '<- West to Fairville    East to Summershores ->'.",
                         value=0,
                         canPick=False)


class DoNotTakeSign(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Do Not Take Sign",
                         description="The sign reads, 'Do Not Take This Sign'",
                         value=0,
                         canPick=True)


class Fountain(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Fountain",
                         description="The water in the fountain is a bright green color. Is that... gatorade?",
                         value=0,
                         canPick=False)


class Anvil(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Anvil",
                         description="The black anvil has the word 'ACME' engraved on the side.",
                         value=0,
                         canPick=False)


class LockPicks(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Lock Picks",
                         description="A set of fine picks for picking locks.",
                         value=5,
                         canPick=True)


class CrystalBall(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Crystal Ball",
                         description="The crystal ball swirls with mystical energy, forming the words 'Answer Unclear."
                                     " Check Again Later.'",
                         value=0,
                         canPick=False)


class SillyGlasses(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Silly Glasses",
                         description="These glasses have a fake nose and mustache attached to them. The perfect "
                                     "disguise!",
                         value=2,
                         canPick=True)


class FloatingBook(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Floating Book",
                         description="This magical tome doesn\'t have a lot of pictures in it. Boring!",
                         value=0,
                         canPick=False)


class Telescope(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Telescope",
                         description="Using the telescope, you can see your house from here!",
                         value=0,
                         canPick=False)


class Deliveryboy(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Deliveryboy",
                         description="The deliveryboy turns to you and ",
                         value=0,
                         canPick=False)
