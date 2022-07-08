const LOCATION_IDS = ["#Leap-Creek", "#roadAB", "#Blackstone", "#roadBD", "#Fangmarsh", "#roadCD", "#Underclaw", "#roadAC"];
const MULTIPLE_PLAYER_OCCUPIED_LOCATION_COLOR = '#025b0e';
const UNOCCUPIED_LOCATION_COLOR = '#ffffff';
const CW_DIR_VALUE = 1
const CCW_DIR_VALUE = -1
const TOWN_DESCRIPTIONS = {
    "#Leap-Creek": "The Water Temple",
    "#Blackstone": "The Iron Fortress",
    "#Fangmarsh": "The Burning Bog",
    "#Underclaw": "The Hidden City",
}

var playerInfo = {
    "p1": {
        "color": "#fff700",
        "locationIndex": 1,
    },
    "p2": {
        "color": "#0011ff",
        "locationIndex": 5,
    },
    "p3": {
        "color": "#dc143c",
        "locationIndex": 3,
    },
    "p4": {
        "color": "#270a47",
        "locationIndex": 7,
    },
}

onPageLoad()

function onPageLoad() {
    Object.keys(playerInfo).forEach(player =>
        $(LOCATION_IDS[playerInfo[player]["locationIndex"]]).css('background-color', playerInfo[player]["color"]))
    $("#towninfo").html("The Valley of the Star")
}

function updateLocationIndex(directionValue, player) {
    playerInfo[player]["locationIndex"] = (((playerInfo[player]["locationIndex"] + directionValue) % LOCATION_IDS.length) + LOCATION_IDS.length) % LOCATION_IDS.length;
}

function updateLocationColors() {
    resetColors();

    Object.keys(playerInfo).forEach(player =>
        $(LOCATION_IDS[playerInfo[player]["locationIndex"]]).css('background-color', playerInfo[player]["color"]))

    LOCATION_IDS.forEach(locationId => {
        var counter = 0;
        Object.keys(playerInfo).forEach(player => {
            if (LOCATION_IDS[playerInfo[player]["locationIndex"]] == locationId) {
                counter++;
            }
        })
        if (counter > 1) {
            $(locationId).css('background-color', MULTIPLE_PLAYER_OCCUPIED_LOCATION_COLOR)
        }
    })
}

function updateTownInfo() {
    var locationDescription = TOWN_DESCRIPTIONS[LOCATION_IDS[playerInfo["p1"]["locationIndex"]]]
    if (locationDescription == undefined) {
        locationDescription = "The Valley of the Star"
    }
    $("#towninfo").html(locationDescription)
}

function resetColors() {
    $(".town").css('background-color', UNOCCUPIED_LOCATION_COLOR);
    $(".road").css('background-color', UNOCCUPIED_LOCATION_COLOR);
}

$("#p1MoveCwButton").click(function () {
    updateLocationIndex(CW_DIR_VALUE, "p1");
    updateLocationColors();
    updateTownInfo();
})

$("#p1MoveCcwButton").click(function () {
    updateLocationIndex(CCW_DIR_VALUE, "p1");
    updateLocationColors();
    updateTownInfo();
})

$("#p2MoveCwButton").click(function () {
    updateLocationIndex(CW_DIR_VALUE, "p2");
    updateLocationColors();
    updateTownInfo();
})

$("#p2MoveCcwButton").click(function () {
    updateLocationIndex(CCW_DIR_VALUE, "p2");
    updateLocationColors();
    updateTownInfo();
})

$("#p3MoveCwButton").click(function () {
    updateLocationIndex(CW_DIR_VALUE, "p3");
    updateLocationColors();
    updateTownInfo();
})

$("#p3MoveCcwButton").click(function () {
    updateLocationIndex(CCW_DIR_VALUE, "p3");
    updateLocationColors();
    updateTownInfo();
})

$("#p4MoveCwButton").click(function () {
    updateLocationIndex(CW_DIR_VALUE, "p4");
    updateLocationColors();
    updateTownInfo();
})

$("#p4MoveCcwButton").click(function () {
    updateLocationIndex(CCW_DIR_VALUE, "p4");
    updateLocationColors();
    updateTownInfo();
})