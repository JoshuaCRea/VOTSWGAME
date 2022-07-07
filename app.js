const LOCATION_IDS = ["#Leap-Creek", "#roadAB", "#Blackstone", "#roadBD", "#Fangmarsh", "#roadCD", "#Underclaw", "#roadAC"];
const OCCUPIED_LOCATION_COLOR = '#f8cf95';
const UNOCCUPIED_LOCATION_COLOR = '#ffffff';
const CW_DIR_VALUE = 1
const CCW_DIR_VALUE = -1
const TOWN_DESCRIPTIONS = {
    "#Leap-Creek": "The Water Temple",
    "#Blackstone": "The Iron Fortress",
    "#Fangmarsh": "The Burning Bog",
    "#Underclaw": "The Hidden City",
}

var currentLocationIndex = 1;

$(LOCATION_IDS[currentLocationIndex]).css('background-color', OCCUPIED_LOCATION_COLOR);
$("#towninfo").html("The Valley of the Star")

function updateLocationIndex(directionValue) {
    currentLocationIndex = currentLocationIndex + directionValue;
    if (currentLocationIndex == LOCATION_IDS.length) {
        currentLocationIndex = 0;
    }
    if (currentLocationIndex == -1) {
        currentLocationIndex = LOCATION_IDS.length - 1;
    }
}

function updateLocationColors(occupiedLocationId) {
    $(".town").css('background-color', UNOCCUPIED_LOCATION_COLOR);
    $(".road").css('background-color', UNOCCUPIED_LOCATION_COLOR);
    $(occupiedLocationId).css('background-color', OCCUPIED_LOCATION_COLOR);
}

function updateTownInfo(){
    var locationDescription = TOWN_DESCRIPTIONS[LOCATION_IDS[currentLocationIndex]]
    if (locationDescription == undefined) {
        locationDescription = "The Valley of the Star"
    }
    $("#towninfo").html(locationDescription)
}

$("#moveCwButton").click(function () {
    updateLocationIndex(CW_DIR_VALUE);
    updateLocationColors(LOCATION_IDS[currentLocationIndex]);
    updateTownInfo();
})

$("#moveCcwButton").click(function () {
    updateLocationIndex(CCW_DIR_VALUE);
    updateLocationColors(LOCATION_IDS[currentLocationIndex]);
    updateTownInfo();
})