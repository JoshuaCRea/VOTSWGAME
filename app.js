const LOCATION_IDS = ["#Leap-Creek", "#roadAB", "#Blackstone", "#roadBD", "#Fangmarsh", "#roadCD", "#Underclaw", "#roadAC"];
const PLAYER1_OCCUPIED_LOCATION_COLOR = '#fff700';
const PLAYER2_OCCUPIED_LOCATION_COLOR = '#0011ff';
const PLAYER3_OCCUPIED_LOCATION_COLOR = '#dc143c';
const PLAYER4_OCCUPIED_LOCATION_COLOR = '#270a47';
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

var p1CurrentLocationIndex = 1;
var p2CurrentLocationIndex = 5;
var p3CurrentLocationIndex = 3;
var p4CurrentLocationIndex = 7;

$(LOCATION_IDS[p1CurrentLocationIndex]).css('background-color', PLAYER1_OCCUPIED_LOCATION_COLOR);
$(LOCATION_IDS[p2CurrentLocationIndex]).css('background-color', PLAYER2_OCCUPIED_LOCATION_COLOR);
$(LOCATION_IDS[p3CurrentLocationIndex]).css('background-color', PLAYER3_OCCUPIED_LOCATION_COLOR);
$(LOCATION_IDS[p4CurrentLocationIndex]).css('background-color', PLAYER4_OCCUPIED_LOCATION_COLOR);
$("#towninfo").html("The Valley of the Star")

function updateLocationIndex(directionValue, player) {
    if (player == "p1") {
        p1CurrentLocationIndex = (((p1CurrentLocationIndex + directionValue) % LOCATION_IDS.length) + LOCATION_IDS.length) % LOCATION_IDS.length;
    }
    if (player == "p2") {
        p2CurrentLocationIndex = (((p2CurrentLocationIndex + directionValue) % LOCATION_IDS.length) + LOCATION_IDS.length) % LOCATION_IDS.length;
    }
    if (player == "p3") {
        p3CurrentLocationIndex = (((p3CurrentLocationIndex + directionValue) % LOCATION_IDS.length) + LOCATION_IDS.length) % LOCATION_IDS.length;
    }
    if (player == "p4") {
        p4CurrentLocationIndex = (((p4CurrentLocationIndex + directionValue) % LOCATION_IDS.length) + LOCATION_IDS.length) % LOCATION_IDS.length;
    }
}

function updateLocationColors() {
    $(".town").css('background-color', UNOCCUPIED_LOCATION_COLOR);
    $(".road").css('background-color', UNOCCUPIED_LOCATION_COLOR);

    var p1OccupiedLocationId = LOCATION_IDS[p1CurrentLocationIndex]
    var p2OccupiedLocationId = LOCATION_IDS[p2CurrentLocationIndex]
    var p3OccupiedLocationId = LOCATION_IDS[p3CurrentLocationIndex]
    var p4OccupiedLocationId = LOCATION_IDS[p4CurrentLocationIndex]
    var playerLocationIds = [p1OccupiedLocationId, p2OccupiedLocationId, p3OccupiedLocationId, p4OccupiedLocationId]

    $(p1OccupiedLocationId).css('background-color', PLAYER1_OCCUPIED_LOCATION_COLOR);
    $(p2OccupiedLocationId).css('background-color', PLAYER2_OCCUPIED_LOCATION_COLOR);
    $(p3OccupiedLocationId).css('background-color', PLAYER3_OCCUPIED_LOCATION_COLOR);
    $(p4OccupiedLocationId).css('background-color', PLAYER4_OCCUPIED_LOCATION_COLOR);

    LOCATION_IDS.forEach(locationId => {
        var counter = 0;
        playerLocationIds.forEach(playerLocationId => {
            if (playerLocationId == locationId) {
                counter++;
            }
        })
        if (counter > 1) {
            $(locationId).css('background-color', MULTIPLE_PLAYER_OCCUPIED_LOCATION_COLOR)
        }
    })
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