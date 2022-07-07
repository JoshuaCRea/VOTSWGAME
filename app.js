const LOCATION_IDS = ["#Leap-Creek", "#roadAB", "#Blackstone", "#roadBD", "#Fangmarsh", "#roadCD", "#Underclaw", "#roadAC"];
const PLAYER1_OCCUPIED_LOCATION_COLOR = '#fff700';
const PLAYER2_OCCUPIED_LOCATION_COLOR = '#0011ff';
const PLAYER1and2_OCCUPIED_LOCATION_COLOR = '#025b0e';
const UNOCCUPIED_LOCATION_COLOR = '#ffffff';
const CW_DIR_VALUE = 1
const CCW_DIR_VALUE = -1
const TOWN_DESCRIPTIONS = {
    "#Leap-Creek": "The Water Temple",
    "#Blackstone": "The Iron Fortress",
    "#Fangmarsh": "The Burning Bog",
    "#Underclaw": "The Hidden City",
}

var p1CurrentLocationIndex = 1;
var p2CurrentLocationIndex = 5;

var PLAYER_location_INDICES = {
    "1": 1,
    "2": 5,
}

// PLAYER_INDICES dict - key could be subbed for LOCAtiON_IDS[p#CurrentLocationIndex]

$(LOCATION_IDS[p1CurrentLocationIndex]).css('background-color', PLAYER1_OCCUPIED_LOCATION_COLOR);
$(LOCATION_IDS[p2CurrentLocationIndex]).css('background-color', PLAYER2_OCCUPIED_LOCATION_COLOR);
$("#towninfo").html("The Valley of the Star")

function updateLocationIndex(directionValue, player) {
    if (player == "p1") {
        p1CurrentLocationIndex = (((p1CurrentLocationIndex + directionValue) % LOCATION_IDS.length) + LOCATION_IDS.length) % LOCATION_IDS.length;
    }
    if (player == "p2") {
        p2CurrentLocationIndex = (((p2CurrentLocationIndex + directionValue) % LOCATION_IDS.length) + LOCATION_IDS.length) % LOCATION_IDS.length;
    }
}

function updateLocationColors() {
    var p1OccupiedLocationId = LOCATION_IDS[p1CurrentLocationIndex]
    var p2OccupiedLocationId = LOCATION_IDS[p2CurrentLocationIndex]
    $(".town").css('background-color', UNOCCUPIED_LOCATION_COLOR);
    $(".road").css('background-color', UNOCCUPIED_LOCATION_COLOR);
    if (p1OccupiedLocationId == p2OccupiedLocationId) {
        $(p2OccupiedLocationId).css('background-color', PLAYER1and2_OCCUPIED_LOCATION_COLOR);
    } else {
        $(p1OccupiedLocationId).css('background-color', PLAYER1_OCCUPIED_LOCATION_COLOR);
        $(p2OccupiedLocationId).css('background-color', PLAYER2_OCCUPIED_LOCATION_COLOR);
    }  
}

function updateTownInfo() {
    var locationDescription = TOWN_DESCRIPTIONS[LOCATION_IDS[p1CurrentLocationIndex]]
    if (locationDescription == undefined) {
        locationDescription = "The Valley of the Star"
    }
    $("#towninfo").html(locationDescription)
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