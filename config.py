HOMETOWN_BASELINE_ABILITY_VALUES = {
    "Blackstone" : {
        "STA" : 2,
        "POW" : 0,
        "AGI" : 0,
        "CHI" : 0,
        "WIT" : 1,
    },
    "Fangmarsh" : {
        "STA" : 1,
        "POW" : 2,
        "AGI" : 0,
        "CHI" : 0,
        "WIT" : 0,
    },
    "Leap-Creek" : {
        "STA" : 0,
        "POW" : 0,
        "AGI" : 1,
        "CHI" : 2,
        "WIT" : 0,
    },
    "Pouch" : {
        "STA" : 0,
        "POW" : 0,
        "AGI" : 0,
        "CHI" : 1,
        "WIT" : 2,
    },
    "Underclaw" : {
        "STA" : 0,
        "POW" : 1,
        "AGI" : 2,
        "CHI" : 0,
        "WIT" : 0,
    },
}

SCHOOL_NAME_QUEST_CARD_MAP = {
    "School of Hong Quan" : {
        "name": "The Walls of Blackstone",
        "description": "Learn defensive techniques by helping the laborers of Blackstone School build a defensive structure of stone and metal.",
        "step_one": {
            "description": "Carry the heavy dark stones up the ladder to the top of the new outer wall around the school.",
            "abilities": ("STA", "POW"),
        },
        "step_two": {
            "description": "Practice defensive movements by spreading the mortar quickly in the hot dry sun, and putting the stones in place.",
            "abilities": ("STA", "CHI"),
        },
        "difficulty_class": 0,
        "rewards": {
            "technique": "Stone Paw, Iron Beak",
            "stat_bonus": None
        },
    },
    "Temple of T'ai Chi Ch'uan" : {
        "name": "The Water Temple",
        "description": "Study with the monks the T'ai Chi Chuan basics to learn the skills you need to best your opponent using momentum and quick reaction.",
        "step_one": {
            "description": "Watch the way your movements effect your balance. Certain things about this study must be true of all men.",
            "abilities": ("CHI", "AGI"),
        },
        "step_two": {
            "description": "That which is internal can be brought to the surface of the body. Learn to bring your mental momentum to your extremities.",
            "abilities": ("CHI", "AGI"),
        },
        "difficulty_class": 0,
        "rewards": {
            "technique": "The Waiting Hand",
            "stat_bonus": None
        },
    },
    "School of Zui Quan" : {
        "name": "School of Wine and Shadows",
        "description": "Train with the Zui Quan students to learn the skills you need to take advantage of your opponent with unpredictability and deception.",
        "step_one": {
            "description": "To stumble is to outsmart. First learn how to deceive your opponent in games of Xiangqi. Lure and trap.",
            "abilities": ("WIT", "CHI"),
        },
        "step_two": {
            "description": "Observe a Zui Quan master juggle, toss and then hide a stone under a series of cups. A quick eye and mind will be able to see through his distractions and find the stone.",
            "abilities": ("WIT", "CHI"),
        },
        "difficulty_class": 0,
        "rewards": {
            "technique": "Deceptive Stagger",
            "stat_bonus": None
        },
    },
    "Kwoon of Pai Tong Long" : {
        "name": "The Nail and the Post",
        "description": "Use your hands and fingers to yank a red hot nail out of a wooden post right outside the Kwoon.",
        "step_one": {
            "description": "Focus all your power into your hands... and YANK out the nail. Then watch the Kwoon master hold it over a fire before handing it back to you.",
            "abilities": ("POW", "STA"),
        },
        "step_two": {
            "description": "With the power focused in your hand, drive the nail back into the post. Do not bend the red-hot nail!",
            "abilities": ("POW", "STA"),
        },
        "difficulty_class": 0,
        "rewards": {
            "technique": "Flaming Foot",
            "stat_bonus": "POW"
        },
    },
    "Kwoon of Changquan" : {
        "name": "Carve a New Path",
        "description": "In order to make more room for new families coming to town, you help the townfolk in paving a new path in the cave to expand the community.",
        "step_one": {
            "description": "Balance on the slanted rock face and chizel into the stone walls to create a new path.",
            "abilities": ("AGI", "POW"),
        },
        "step_two": {
            "description": "In order to make progress you must focus your strength into the pick axe. Raise it above your head and hammer it down hard enough to take huge chunks out of the wall.",
            "abilities": ("CHI", "POW"),
        },
        "difficulty_class": 0,
        "rewards": {
            "technique": "Crushing Avalanche Fist",
            "stat_bonus": "POW"
        },
    },
}
