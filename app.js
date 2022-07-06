const TOWN_IDS = ["#townA", "#townB", "#townD", "#townC"];
const OCCUPIED_TOWN_COLOR = '#f8cf95';
const UNOCCUPIED_TOWN_COLOR = '#ffffff'

var currentTownIndex = 0;
var currentTownId = TOWN_IDS[currentTownIndex];

$(currentTownId).css('background-color', OCCUPIED_TOWN_COLOR);

function updateTownColors(townId) {
    $(".town").css('background-color', UNOCCUPIED_TOWN_COLOR);
    $(townId).css('background-color', OCCUPIED_TOWN_COLOR);
}

$("#moveCcwButton").click(function () {
    currentTownIndex--;
    if (currentTownIndex == -1) {
        currentTownIndex = TOWN_IDS.length - 1;
    }
    var currentTownId = TOWN_IDS[currentTownIndex];
    updateTownColors(currentTownId);
})

$("#moveCwButton").click(function () {
    currentTownIndex++;
    if (currentTownIndex == TOWN_IDS.length) {
        currentTownIndex = 0;
    }
    var currentTownId = TOWN_IDS[currentTownIndex];
    updateTownColors(currentTownId);
})