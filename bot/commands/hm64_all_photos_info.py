from bot.commands import BaseCommands


class HM64AllPhotosInfo(BaseCommands):
    def __init__(self):
        self.commands = {
            "photos": {
                "docs": "URL to All Photos PasteBin",
                "kwargs": ["photos", "photo"],
                "func": self.messageReturner("https://pastebin.com/fdyEs4pj"),
            },
            "grandpa": {
                "docs": "Grandpa's Photo Information",
                "func": self.messageReturner(
                    "Grandpa's Photo: You start the game with this Photo."
                ),
            },
            "balloon": {
                "docs": "Balloon Photo Information",
                "func": self.messageReturner(
                    "Balloon Photo: Must become Harvest King at the Harvest Festival (6% chance on Fall 12), then must ride the Balloon at the following year's Sewing Festival (Spring 8)"
                ),
            },
            "horserace": {
                "docs": "Horse Race Photo Information",
                "func": self.messageReturner(
                    "Horse Race Photo: Must win any of the Horse Races (Spring 17, Fall 28). This becomes easier and more consistent with a decent amount of affection with the horse (200 points or so). The horse loses 1 affection point per day. Talking to/Riding on the horse is +1, brushing the horse is +1, whistling for the horse is +1, for a net gain of 2 possible affection points a day."
                ),
            },
            "cow": {
                "docs": "Cow Festival Photo Information",
                "kwargs": ["cow", "cowfestival"],
                "func": self.messageReturner(
                    "Cow Festival Photo: Must win the Cow Festival (Fall 4). Requires 240 Affection with the entered cow and 60 or more milks shipped. We use a glitch to get easy maxed affection on all our cows."
                ),
            },
            "swimming": {
                "docs": "Swimming Festival Photo Information",
                "kwargs": ["swimming", "swimmingfestival"],
                "func": self.messageReturner(
                    "Swimming Festival Photo: Must win the Swimming Festival (Summer 24). Tap A at the correct pace to win, nothing special required."
                ),
            },
            "springs": {
                "docs": "Hot Springs Photo Information",
                "kwargs": ["spring", "hotspring", "springs", "hotsprings"],
                "func": self.messageReturner(
                    "Hot Springs Photo: Must help the carpenters build the Hot Springs on Winter 16 of Year 1. We will help every day for the easy money."
                ),
            },
            "dograce": {
                "docs": "Dog Race Photo Information",
                "func": self.messageReturner(
                    "Dog Race Photo: Must win the Dog Race (Winter 19). This becomes easier and more consistent with a decent amount of affection with the dog (230+ points of affection). The dog loses 1 affection point per day. Whistling, picking up the dog, and feeding the dog all give +1, for a net gain of 2 possible affection points per day. We will usually attempt to win the dog race in the 2nd year, as the Party Photo requires the dog to stay at a high affection level."
                ),
            },
            "marriage": {
                "docs": "Marriage Photo Information",
                "func": self.messageReturner(
                    "Marriage Photo: Get Married to one of the 5 eligible girls. Requires a built kitchen (5000G, 450 Lumber) and 220 affection points with your girl of choice. Propose with a Blue Feather (980G) and the marriage will happen on the following Sunday. We will be getting married to Karen or Elli no later than the end of Summer, Y2."
                ),
            },
            "baby": {
                "docs": "Baby Photo Information",
                "func": self.messageReturner(
                    "Baby Photo: Have a baby. Your wife will become pregnant after 30 days of marriage if she is at 250 affection or higher and you have a baby bed. 60 days after she becomes pregnant, the baby will be born. We will be having our baby sometime during Spring of Y3."
                ),
            },
            "maria": {
                "docs": "Maria's Photo Information",
                "func": self.messageReturner(
                    "Maria's Photo: Must have Maria at 200 Affection Points during Summer while you are unmarried. At 6PM, Maria will enter (or be waiting on) the farm screen. Talk to her, say yes, and the Photo Event will begin."
                ),
            },
            "popuri": {
                "docs": "Popuri's Photo Information",
                "func": self.messageReturner(
                    "Popuri's Photo: There is a long event to get this photo normally, however we use a glitch to get it within the first few days of the game. We water any flower on the Goddess Pond screen and leave/re-enter 3 times, then obtain the photo."
                ),
            },
            "elli": {
                "docs": "Elli's Photo Information",
                "func": self.messageReturner(
                    "Elli's Photo: Must have Elli at 200 affection on Fall 9 while you are unmarried, and it must not be raining. At 6PM, Elli will enter (or be waiting on) the farm screen. Talk to her, say yes, and the Photo Event will begin."
                ),
            },
            "ann": {
                "docs": "Ann's Photo Information",
                "func": self.messageReturner(
                    "Ann's Photo: Must have Ann at 200 affection during Winter while you are unmarried. Ann will be waiting on your farm screen as soon as she hits 200 affection (or if she already is at 200 affection, the morning of Winter 1). Talk to her, say yes, and the Photo Event will begin."
                ),
            },
            "karen": {
                "docs": "Karen's Photo Information",
                "func": self.messageReturner(
                    "Karen's Photo: Must have restored the Vineyard (Duke 38+ affection to obtain the Wine, Sprites 50+ affection, throw an offering into the goddess pond and wish to restore the Vineyard), must have Karen at 200 affection on Fall 7, must be unmarried, must not be raining. At 6PM, Karen will enter (or be waiting on) the farm screen. Talk to her, say yes, and the Photo Event will begin."
                ),
            },
            "house": {
                "docs": "House Extensions Photo Information",
                "kwargs": ["house", "extension", "extention", "houseextension"],
                "func": self.messageReturner(
                    "House Extensions Photo: Must have all 6 house extensions (48,000G, 2080 Lumber)."
                ),
            },
            "party": {
                "docs": "Party Photo Information",
                "func": self.messageReturner(
                    """Party Photo: Requires the following
- Wife 250+ Affection
- Dog 200+ Affection
- 6 Power Berries (Technically 190 Max Stamina)
- 250+ Happiness
- Your baby must exist
- All House Extensions
- 1 Adult Chicken, and it must be fed for the evaluation.
- 384 Tiles of Grass (80% of your farmland must be grass, 43 bags of Grass or 21,500G worth of grass)
- 10 Applicable Villagers (Wife excluded) at 160 affection or higher.
- 2494 total affection points across all villagers."""
                ),
            },
        }
