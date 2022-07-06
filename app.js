const LOCATION_IDS = ["#townA", "#roadAB", "#townB", "#roadBD", "#townD", "#roadCD", "#townC", "#roadAC"];
const OCCUPIED_LOCATION_COLOR = '#f8cf95';
const UNOCCUPIED_LOCATION_COLOR = '#ffffff';

var currentLocationIndex = 0;

$(LOCATION_IDS[currentLocationIndex]).css('background-color', OCCUPIED_LOCATION_COLOR);

function updateLocationColors(occupiedLocationId) {
    $(".town").css('background-color', UNOCCUPIED_LOCATION_COLOR);
    $(".road").css('background-color', UNOCCUPIED_LOCATION_COLOR);
    $(occupiedLocationId).css('background-color', OCCUPIED_LOCATION_COLOR);
}

$("#moveCcwButton").click(function () {
    currentLocationIndex--;
    if (currentLocationIndex == -1) {
        currentLocationIndex = LOCATION_IDS.length - 1;
    }
    updateLocationColors(LOCATION_IDS[currentLocationIndex]);
})

$("#moveCwButton").click(function () {
    currentLocationIndex++;
    if (currentLocationIndex == LOCATION_IDS.length) {
        currentLocationIndex = 0;
    }
    updateLocationColors(LOCATION_IDS[currentLocationIndex]);
})