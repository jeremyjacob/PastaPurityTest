questions = ["Attended a lake orgy",
"Lost V-Card on Minecraft's 10th Aniversary",
"Hooked up on acid",
"Lost virginity on acid",
"Had sex on shrooms",
"Peed in a bible",
"Coke?",
"Sold sexual pictures",
"Done meth",
"Mental breakdown on molly (on molly)",
"Kissed over five people in the group",
"Gone skinny dipping",
"Toasted weed",
"Filmed a porno",
"Seen Lu's tits",
"Slept on a washing machine",
"Got black out drunk",
"Greened out",
"Kissed someone's nose",
"Cheated on significant other",
"Sexual acts platonically",
"Had a thing with Lu",
"Had a thing with Laney",
"Had a thing with Kendrick",
"Kissed Addison",
"Been on Delaney's TikTok",
"Held an ice cream cone upside down",
"Drunken ketchup through a straw",
"Fought Kendrick over toast or waffles",
"Stolen from someone in group",
"Coke shrooms?",
"Condom drip",
"Had unprotected sexual intercourse",
"Kissed over 10 people in a day",
"Had your nipple flicked",
"Had a pregnancy scare",
"Broken into a school property",
"Chugged milk through a PVC pipe",
"Used cigarettes as candles",
"Been tased by Clark",
"Said nigger",
"Cried laughing at jorps dad joke while everyone was like 😐",
"Stolen alcohol",
"Been attacked by Poppy (either one)",
"Pieced or had titties pieced",
"Melrose?",
"Pissed off Jorp",
"Pissed off Robbie",
"Spiritually fucked Addison",
"Actually fucked Addison",
"Set off explosives at Chumash Park",
"Done tipple Cs",
"Smokes a pack of stoges in one sitting",
"Smoked a Talki",
"Been in a fight",
"Soap",
"Garlic Bread",
"Pussy",
"Nyquil",
"Got kicked out of Mikey's house",
"Held Doug",
"Pet rat dog",
"Expirienced the Tilly crib",
"Rolled a J",
"Played with guns",
"Made me rock hard in class you naughty whore",
"Played the board game",
"Been slapped by huggy",
"Recharched a puff",
"Have a nicotine addiction",
"Have been an alcholic at any point",
"Have been addicted to oxys at any point",
"Yelled \"If you like PornHub you'll love PornHub live\"",
"Ripped the intergalactic jew bong™",
"Had or given head with teeth",
"Jewish?",
"Kicked someone from a groupchat",
"Stolen signs",
"Had a thing with someone 2 years older or younger",
"Own a cowboy hat",
"Bisexual",
"Possessed three or more ID cards at any time",
"Own a Virginity Rocks hoodie",
"Own a V-Card",
"Taken someone's V-Card",
"Had the acorn pancakes",
"Been forced to pee",
"Top?",
"Been jumped",
"Hooked up with somone who you don't know the name of",
"Spent over $200 on drugs",
"Had a dream about Robbie jacking off",
"Search Results",
"Web results",
"🧊😺?",
"Attended an AA Meeting",
"Attempted to make salvia tea",
"Pissed in an urinal without a dick",
"Attended elevator club",
"Going to vote Jorp Wallace 2020"]

output = ""
for index, question in enumerate(questions, start=1):
    output += f"""<li><input type="checkbox" id="{index}">
<label for="{index}"> {question}</label></li>
"""

with open('output.txt', 'w') as file:
    file.write(output)